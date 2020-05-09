#!/usr/bin/env python3

import altair as alt
import pandas  # http://pandas.pydata.org
import numpy
import datetime

from fileops import save, getChartHTML
from filters import *
from logic import *

alt.data_transformers.disable_max_rows()

name = "gunrock_primitives"

# begin user settings for this script
roots = [
    "../gunrock-output/v1-0-0/sssp",
    "../gunrock-output/v1-0-0/bc",
    "../gunrock-output/v1-0-0/tc",
    "../gunrock-output/v1-0-0/pr",
    "../gunrock-output/v1-0-0/bfs",
    "../gunrock-output/launch_bounds_comparison",
    "../gunrock-output/cuda_arch_comparison",
]
fnFilterInputFiles = [
    fileEndsWithJSON,
]
fnPreprocessDF = [
    # convertCtimeStringToDatetime,
    # normalizePRMTEPS,
    mergeAlgorithmIntoPrimitive,
    SSSPtosssp,
    renameAdvanceModeWithAHyphen,
    addJSONDetailsLink,
    gunrockVersionGPU,
]
fnFilterDFRows = [
    filterOut(True, "64bit-SizeT"),
    filterOut(True, "64bit-VertexT"),
]
fnPostprocessDF = [
    equateNVIDIAGPUs,
    copyQueuedToVisitedForPR,
    computeMTEPSFromEdgesAndElapsed10,
    mergeMaxIterationIntoMaxIter,
    normalizePRByIterations,
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

columnsOfInterest = [
    "primitive",
    "dataset",
    "avg-mteps",
    "avg-process-time",
    "engine",
    # 'tag',
    "num-vertices",
    "num-edges",
    "nodes-visited",
    "edges-visited",
    "search-depth",
    "gunrock-version",
    "gpuinfo_name",
    "gpuinfo_name_full",
    "advance_mode",
    "undirected",
    "pull",
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
    "max(avg-mteps)": "quantitative",
    "avg-process-time": "quantitative",
    "min(avg-process-time)": "quantitative",
    "num-vertices": "quantitative",
    "num-edges": "quantitative",
    "nodes-visited": "quantitative",
    "edges-visited": "quantitative",
    "search-depth": "quantitative",
    "mark-pred": "ordinal",
    "undirected": "ordinal",
    "advance_mode": "nominal",
    "gpuinfo_name": "nominal",
    "gpuinfo_name_full": "nominal",
    "primitive": "nominal",
    "pull": "nominal",
}

chart = {}

my = {}

for prim in ["bfs", "sssp", "tc", "bc", "pr"]:
    my[(prim, "mteps")] = {
        "mark": "point",
        "x": ("dataset", "Dataset", "linear"),
        "y": ("max(avg-mteps)", "MTEPS", "log"),
        "row": ("undirected", "Undirected"),
        "color": ("gpuinfo_name", "GPU"),
        "shape": ("gpuinfo_name", "GPU"),
        # "prim=prim" forces "prim" to bind to the primitive in the above loop
        # otherwise it binds when it's called, that's bad
        "filter": lambda df, prim=prim: df[df["primitive"] == prim],
    }
    if prim == "sssp" or prim == "bfs":
        # for SSSP/BFS, mark-pred is significant, but not for the others
        my[(prim, "mteps")]["col"] = ("mark-pred", "Mark Predecessors")

    # avg-process-time is identical except pick the min
    my[(prim, "avg-process-time")] = my[(prim, "mteps")].copy()
    my[(prim, "avg-process-time")]["y"] = (
        # pr has a normalized runtime per iteration (already computed),
        # but fix the caption
        "min(avg-process-time)",
        "Per-iteration runtime (ms)" if prim == "pr" else "Runtime (ms)",
        "log",
    )

    my[(prim, "advance_mode")] = {
        "mark": "point",
        "x": ("dataset", "Dataset", "linear"),
        "y": ("max(avg-mteps)", "MTEPS", "log"),
        "row": ("undirected", "Undirected"),
        "color": ("advance_mode", "Advance Mode"),
        "shape": ("advance_mode", "Advance Mode"),
        "filter": lambda df, prim=prim: df[df["primitive"] == prim],
    }
    if prim == "sssp" or prim == "bfs":
        my[(prim, "advance_mode")]["col"] = ("mark-pred", "Mark Predecessors")
    my[(prim, "edges")] = my[(prim, "avg-process-time")].copy()
    my[(prim, "edges")]["x"] = ("num-edges", "Number of Edges", "log")

my[("all-V100", "edges-visited-vs-num-edges")] = {
    "mark": "point",
    "x": ("num-edges", "Number of Edges", "log"),
    "y": ("edges-visited", "Number of Edges Visited/Queued", "log"),
    "row": ("undirected", "Undirected"),
    "color": ("primitive", "Primitive"),
    "shape": ("primitive", "Primitive"),
    "filter": lambda df: df[
        (df["edges-visited"] > 0) & (df["gpuinfo_name"] == "Tesla V100")
    ],
}

my[("all-V100", "vertices-visited-vs-num-vertices")] = {
    "mark": "point",
    "x": ("num-vertices", "Number of Vertices", "log"),
    "y": ("nodes-visited", "Number of Vertices Visited/Queued", "log"),
    "row": ("undirected", "Undirected"),
    "color": ("primitive", "Primitive"),
    "shape": ("primitive", "Primitive"),
    "filter": lambda df: df[
        (df["nodes-visited"] > 0) & (df["gpuinfo_name"] == "Tesla V100")
    ],
}

my[("all-V100", "search-depth")] = {
    "mark": "point",
    "x": ("search-depth", "Search Depth", "log"),
    "y": ("avg-process-time", "Runtime (ms)", "log"),
    "row": ("undirected", "Undirected"),
    "color": ("primitive", "Primitive"),
    "shape": ("primitive", "Primitive"),
    "filter": lambda df: df[
        (df["search-depth"] > 0) & (df["gpuinfo_name"] == "Tesla V100")
    ],
}


for plot in my.keys():
    # if plot[0] != "all-V100":
    # continue
    print(f"*** Processing {plot} ***")

    primitive = plot[0]
    if "filter" in my[plot]:
        dfx = my[plot]["filter"](df)
    else:
        dfx = df

    selection = {}

    chart[plot] = (
        alt.Chart(dfx, mark=my[plot]["mark"])
        .encode(
            x=alt.X(
                my[plot]["x"][0],
                type=datatypes[my[plot]["x"][0]],
                axis=alt.Axis(title=my[plot]["x"][1],),
                scale=alt.Scale(type=my[plot]["x"][2]),
            ),
            y=alt.Y(
                my[plot]["y"][0],
                type=datatypes[my[plot]["y"][0]],
                # aggregate=my[plot].get("y_aggregate", alt.Undefined),
                axis=alt.Axis(title=my[plot]["y"][1],),
                scale=alt.Scale(type=my[plot]["y"][2]),
            ),
            tooltip=[my[plot]["y"][0]]
            + [
                "primitive",
                "dataset",
                "gpuinfo_name",
                "gpuinfo_name_full",
                "num-vertices",
                "num-edges",
                "nodes-visited",
                "edges-visited",
                "search-depth",
                "64bit-SizeT",
                "64bit-VertexT",
            ],
        )
        .interactive()
    )
    if "col" in my[plot]:
        chart[plot] = chart[plot].encode(
            column=alt.Column(
                my[plot]["col"][0],
                type=datatypes[my[plot]["col"][0]],
                header=alt.Header(title=my[plot]["col"][1]),
            )
        )
    if "row" in my[plot]:
        chart[plot] = chart[plot].encode(
            row=alt.Row(
                my[plot]["row"][0],
                type=datatypes[my[plot]["row"][0]],
                header=alt.Header(title=my[plot]["row"][1]),
            )
        )
    if "color" in my[plot]:
        color = stripShorthand(my[plot]["color"][0])
        chart[plot] = chart[plot].encode(
            color=alt.Color(
                color,
                type=datatypes[color],
                legend=alt.Legend(title=my[plot]["color"][1]),
                # scale=alt.Scale(scheme="dark2"),
            )
        )
        selection["color"] = alt.selection_multi(fields=[color], bind="legend")
        chart[plot] = chart[plot].add_selection(selection["color"])

    if "shape" in my[plot]:
        shape = stripShorthand(my[plot]["shape"][0])
        chart[plot] = chart[plot].encode(
            shape=alt.Shape(
                shape,
                type=datatypes[shape],
                legend=alt.Legend(title=my[plot]["shape"][1]),
            )
        )
        selection["shape"] = alt.selection_multi(fields=[shape], bind="legend")
        chart[plot] = chart[plot].add_selection(selection["shape"])

    if plot[1] == "sel":
        # input_checkbox = alt.binding_checkbox()
        # checkbox_selection = alt.selection_single(bind=input_checkbox, name="Big Budget Films")
        # size_checkbox_condition = alt.condition(checkbox_selection,
        #                                         alt.SizeValue(25),
        #                                         alt.Size('Hundred_Million_Production')
        # )
        checkbox = {}
        checkbox_selection = {}
        for box in ["undirected"]:
            for l in [box + "_on", box + "off"]:
                checkbox_selection[l] = alt.selection_single(
                    bind=alt.binding_checkbox(), name=l
                )
                chart[plot] = chart[plot].add_selection(checkbox_selection[l])

    plotname = "_".join(filter(lambda x: bool(x), [name, plot[0], plot[1]]))
    save(
        chart=chart[plot],
        df=dfx,
        plotname=plotname,
        formats=["tablehtml", "tablemd", "md", "html", "png", "pdf"],
        sortby=[
            "primitive",
            "dataset",
            "engine",
            "gunrock-version",
            "undirected",
            "mark-pred",
            "advance_mode",
        ],
        columns=columnsOfInterest,
        mdtext=(
            """
         # Data for %s

         """
            % plot[0]
            + getChartHTML(chart[plot], anchor=plotname)
            + """
                 [Source data](tables/%s_table.html), with links to the output JSON for each run
                 """
            % plotname
        ),
    )
