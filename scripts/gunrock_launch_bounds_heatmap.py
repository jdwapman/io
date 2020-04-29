#!/usr/bin/env python3

import altair as alt
import pandas  # http://pandas.pydata.org
import numpy
import datetime

from fileops import save, getChartHTML
from filters import *
from logic import *

name = "gunrock_launch_bounds_heatmap"

# begin user settings for this script
roots = ["../gunrock-output/launch_bounds_comparison"]
fnFilterInputFiles = [
    fileEndsWithJSON,
]
fnPreprocessDF = [
    # convertCtimeStringToDatetime,
    # normalizePRMTEPS,
    addJSONDetailsLink,
]
fnFilterDFRows = []
fnPostprocessDF = [
    extractCTAThreadsFromTag,
    concatFields(
        "variant",
        ["undirected", "mark-pred", "64bit-SizeT", "64bit-VertexT"],
        abbrev=True,
    ),
]
# end user settings for this script

# actual program logic
# do not modify

# choose input files
df = filesToDF(roots=roots, fnFilterInputFiles=fnFilterInputFiles)
for fn in fnPreprocessDF:  # alter entries / compute new entries
    df = fn(df)
for fn in fnFilterDFRows:  # remove rows
    df = fn(df)
for fn in fnPostprocessDF:  # alter entries / compute new entries
    df = fn(df)

# end actual program logic

print(df["variant"])

columnsOfInterest = [
    "primitive",
    "dataset",
    "avg-mteps",
    "avg-process-time",
    "engine",
    "tag",
    "tag_cta",
    "tag_threads",
    "num-vertices",
    "num-edges",
    "gunrock-version",
    "gpuinfo_name",
    "variant",
    "undirected",
    "mark-pred",
    "64bit-SizeT",
    "64bit-VertexT",
    "time",
    "details",
]
# would prefer a cleanup call https://github.com/altair-viz/altair/issues/183
# without this, output is gigantic
df = (keepTheseColumnsOnly(columnsOfInterest))(df)

# now make the graph

datatypes = {
    "dataset": "nominal",
    "avg-mteps": "quantitative",
    "avg-process-time": "quantitative",
    "num-edges": "quantitative",
    "mark-pred": "ordinal",
    "undirected": "ordinal",
    "advance_mode": "nominal",
    "gpuinfo_name": "nominal",
    "pull": "nominal",
    "tag_cta": "ordinal",
    "tag_threads": "ordinal",
    "variant": "nominal",
}

chart = {}

colormap = alt.Scale(range=["#e8e8e8", "#171717"])

for primtuple in [
    ("bounds", ""),
]:
    my = {
        ("bounds", ""): {
            "x": ("tag_cta", "CTA", "linear"),
            "y": ("tag_threads", "Threads", "linear"),
            "color": ("avg-process-time", "Runtime (ms)"),
            "row": ("variant", "Undirected / Mark Pred / 64b Size / 64b Vertex"),
        },
    }

    selection = {}

    chart[primtuple] = (
        alt.Chart(df)
        .mark_rect()
        .encode(
            x=alt.X(
                my[primtuple]["x"][0],
                type=datatypes[my[primtuple]["x"][0]],
                axis=alt.Axis(title=my[primtuple]["x"][1],),
                scale=alt.Scale(type=my[primtuple]["x"][2]),
            ),
            y=alt.Y(
                my[primtuple]["y"][0],
                type=datatypes[my[primtuple]["y"][0]],
                axis=alt.Axis(title=my[primtuple]["y"][1],),
                scale=alt.Scale(type=my[primtuple]["y"][2]),
            ),
            tooltip=[
                "primitive",
                "dataset",
                "gpuinfo_name",
                "num-vertices",
                "num-edges",
                "tag",
                "mark-pred",
                "undirected",
                "64bit-SizeT",
                "64bit-VertexT",
                "avg-mteps",
                "avg-process-time",
            ],
        )
        .interactive()
    )
    if "col" in my[primtuple]:
        chart[primtuple] = chart[primtuple].encode(
            column=alt.Column(
                my[primtuple]["col"][0],
                type=datatypes[my[primtuple]["col"][0]],
                header=alt.Header(title=my[primtuple]["col"][1]),
            )
        )
    if "row" in my[primtuple]:
        chart[primtuple] = chart[primtuple].encode(
            row=alt.Row(
                my[primtuple]["row"][0],
                type=datatypes[my[primtuple]["row"][0]],
                header=alt.Header(title=my[primtuple]["row"][1]),
            )
        )
    if "color" in my[primtuple]:
        color = stripShorthand(my[primtuple]["color"][0])
        chart[primtuple] = chart[primtuple].encode(
            color=alt.Color(
                color,
                type=datatypes[color],
                legend=alt.Legend(title=my[primtuple]["color"][1]),
                scale=colormap,
            )
        )
        # selection['color'] = alt.selection_multi(fields=[color],
        # bind='legend')
        # chart[primtuple] = chart[primtuple].add_selection(selection['color'])

    if "shape" in my[primtuple]:
        shape = stripShorthand(my[primtuple]["shape"][0])
        chart[primtuple] = chart[primtuple].encode(
            shape=alt.Shape(
                shape,
                type=datatypes[shape],
                legend=alt.Legend(title=my[primtuple]["shape"][1]),
            )
        )
        # selection['shape'] = alt.selection_multi(fields=[shape],
        #                                          bind='legend')
        # chart[primtuple] = chart[primtuple].add_selection(selection['shape'])

    plotname = "_".join(filter(lambda x: bool(x), [name, primtuple[0], primtuple[1]]))
    save(
        chart=chart[primtuple],
        df=df,
        plotname=plotname,
        formats=["tablehtml", "tablemd", "md", "html", "png", "svg", "pdf"],
        sortby=[
            "primitive",
            "dataset",
            "engine",
            "gunrock-version",
            "undirected",
            "mark-pred",
        ],
        columns=columnsOfInterest,
        mdtext=(
            """
         # Data for %s

         """
            % primtuple[0]
            + getChartHTML(chart[primtuple], anchor=plotname)
            + """
                 [Source data](tables/%s_table.html), with links to the output JSON for each run
                 """
            % plotname
        ),
    )
