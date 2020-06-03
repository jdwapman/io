#!/usr/bin/env python3

import altair as alt
import pandas  # http://pandas.pydata.org
import numpy
import datetime

from fileops import save, getChartHTML
from filters import *
from logic import *

alt.data_transformers.disable_max_rows()

name = "gunrock_dobfs_heatmaps"

# begin user settings for this script
roots = [
    "../gunrock-output/v1-0-0/dobfs_parameter_sweep",
]
fnFilterInputFiles = [
    fileEndsWithJSON,
]
fnPreprocessDF = [
    addJSONDetailsLink,
]
fnFilterDFRows = [
    filterOut(True, "64bit-SizeT"),
    filterOut(True, "64bit-VertexT"),
]
fnPostprocessDF = [
    BFStoDOBFS10,
    equateNVIDIAGPUs,
    renameColumnsWithMinus,
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
    "avg_mteps",
    "avg_process_time",
    "engine",
    # 'tag',
    "do_a",
    "do_b",
    "num_vertices",
    "num_edges",
    "nodes_visited",
    "edges_visited",
    "search_depth",
    "gunrock_version",
    "gpuinfo_name",
    "gpuinfo_name_full",
    "advance_mode",
    "undirected",
    "mark_pred",
    "idempotence",
    "64bit_SizeT",
    "64bit_VertexT",
    "time",
    "details",
]
# would prefer a cleanup call https://github.com/altair_viz/altair/issues/183
# without this, output is gigantic
df = (keepTheseColumnsOnly(columnsOfInterest))(df)

# now make the graph

prim_fullname = {
    "bfs": "Forward-Only BFS",
    "dobfs": "Direction-Optimized BFS",
    "sssp": "SSSP",
    "tc": "Triangle Counting",
    "bc": "Betweenness Centrality",
    "pr": "PageRank",
}

datatypes = {
    "advance_mode": "nominal",
    "avg_mteps": "quantitative",
    "avg_process_time": "quantitative",
    "dataset": "nominal",
    "do_a": "ordinal",
    "do_b": "ordinal",
    "edges_visited": "quantitative",
    "gpuinfo_name": "nominal",
    "gpuinfo_name_full": "nominal",
    "gunrock_version": "nominal",
    "idempotence": "nominal",
    "mark_pred": "nominal",
    "max(avg_mteps)": "quantitative",
    "min(avg_process_time)": "quantitative",
    "nodes_visited": "quantitative",
    "num_edges": "quantitative",
    "num_vertices": "quantitative",
    "primitive": "nominal",
    "pull": "nominal",
    "search_depth": "quantitative",
    "undirected": "nominal",
    "undirected_markpred": "nominal",
}

chart = {}

my = {}

# set up all the plots; each entry in "my" becomes a plot

for dataset in df["dataset"].unique():
    max_mteps = df[df["dataset"] == dataset].loc[df["avg_mteps"].idxmax()]
    my[(dataset, "do_ab")] = {
        "mark": "rect",
        "x": ("do_a", "do_a", "linear"),
        "y": ("do_b", "do_b", "linear"),
        "color": ("avg_mteps", "MTEPS"),
        # "prim=prim" forces "prim" to bind to the primitive in the above loop
        # otherwise it binds when it's called, that's bad
        "filter": lambda df, dataset=dataset: df[df["dataset"] == dataset],
        "title": f"Throughput (MTEPS) on {dataset}; max MTEPS = {max_mteps['avg_mteps']:.0f} at (do_a, do_b) = ({max_mteps['do_a']:.0e}, {max_mteps['do_b']:.0e})",
    }

for plot in my.keys():
    print(f"*** Processing {plot} ***")

    primitive = plot[0]
    if "filter" in my[plot]:
        dfx = my[plot]["filter"](df)
    else:
        dfx = df

    # filter the dataframe to only contain the aggregate (do the aggregation in
    # Pandas not Altair, otherwise the resulting dataframe table is huge)
    # y_aggregate is simply the aggregation function (e.g., min, max)
    if "y_aggregate" in my[plot]:
        # what are our groupbys? They're our encodings in the plot.
        columns = [
            my[plot][field][0]
            for field in ["x", "row", "col", "color", "shape"]
            if field in my[plot]
        ]
        # keep only those rows that match the aggregate
        idx = (
            dfx.groupby(columns)[my[plot]["y"][0]].transform(my[plot]["y_aggregate"])
            == dfx[my[plot]["y"][0]]
        )
        dfx = dfx[idx]

    selection = {}

    # we assume that the only aggregate is max or min in the y channel
    def generateTooltip2(field, y):
        mmin = re.match(r"min\((.*)\)$", y)
        mmax = re.match(r"max\((.*)\)$", y)
        if mmin:
            return alt.Tooltip(
                field=field,
                type=datatypes[field],
                aggregate=alt.Aggregate(alt.ArgminDef(argmin=mmin.group(1))),
            )
        elif mmax:
            return alt.Tooltip(
                field=field,
                type=datatypes[field],
                aggregate=alt.Aggregate(alt.ArgmaxDef(argmax=mmax.group(1))),
            )
        else:
            return alt.Tooltip(field=field, type=datatypes[field])

    # this is currying. will it bind correctly?
    def generateTooltip(field):
        return generateTooltip2(field=field, y=my[plot]["y"][0])

    tooltip = [
        "primitive",
        "dataset",
        generateTooltip("avg_mteps"),
        generateTooltip("do_a"),
        generateTooltip("do_b"),
        generateTooltip("avg_process_time"),
        generateTooltip("advance_mode"),
        generateTooltip("gpuinfo_name"),
        generateTooltip("gpuinfo_name_full"),
        generateTooltip("gunrock_version"),
        generateTooltip("num_vertices"),
        generateTooltip("nodes_visited"),
        generateTooltip("num_edges"),
        generateTooltip("edges_visited"),
        generateTooltip("search_depth"),
        generateTooltip("undirected"),
        generateTooltip("mark_pred"),
        generateTooltip("idempotence"),
        "64bit_SizeT",
        "64bit_VertexT",
    ]

    # Altair
    # tooltip=[alt.Tooltip(c, type='quantitative') for c in columns]
    # Vega_Lite
    # {
    #   "type": "nominal",
    #   "field": "Fighting Style",
    #   "aggregate": {"argmin": "Place"}
    # }
    #
    # so:
    #
    # alt.Tooltip(field, alt.aggregate(alt.ArgmaxDef(argmax=argmaxfield?)))

    chart[plot] = (
        alt.Chart(dfx, mark=my[plot]["mark"])
        .encode(
            x=alt.X(
                my[plot]["x"][0],
                type=datatypes[my[plot]["x"][0]],
                axis=alt.Axis(title=my[plot]["x"][1], format=".1",),
                scale=alt.Scale(type=my[plot]["x"][2]),
            ),
            y=alt.Y(
                my[plot]["y"][0],
                type=datatypes[my[plot]["y"][0]],
                # aggregate=my[plot].get("y_aggregate", alt.Undefined),
                axis=alt.Axis(title=my[plot]["y"][1], format=".1",),
                scale=alt.Scale(type=my[plot]["y"][2]),
            ),
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
        selection["color"] = alt.selection_multi(fields=[color], bind="legend")
        chart[plot] = (
            chart[plot]
            .encode(
                color=alt.Color(
                    color,
                    type=datatypes[color],
                    legend=alt.Legend(title=my[plot]["color"][1]),
                    scale=alt.Scale(scheme="viridis"),
                ),
            )
            .add_selection(selection["color"])
        )

    if "shape" in my[plot]:
        shape = stripShorthand(my[plot]["shape"][0])
        selection["shape"] = alt.selection_multi(fields=[shape], bind="legend")
        chart[plot] = (
            chart[plot]
            .encode(
                shape=alt.Shape(
                    shape,
                    type=datatypes[shape],
                    legend=alt.Legend(title=my[plot]["shape"][1]),
                ),
            )
            .add_selection(selection["shape"])
        )

    # https://github.com/altair-viz/altair/issues/1890
    # how to handle both color and shape selection
    # won't work properly until https://github.com/vega/vega-lite/issues/5553
    #   is fixed
    if ("color" in my[plot]) and ("shape" in my[plot]):
        chart[plot] = chart[plot].encode(
            opacity=alt.condition(
                selection["color"] & selection["shape"], alt.value(1), alt.value(0.2)
            )
        )
    elif "color" in my[plot]:
        chart[plot] = chart[plot].encode(
            opacity=alt.condition(selection["color"], alt.value(1), alt.value(0.2))
        )
    elif "shape" in my[plot]:
        chart[plot] = chart[plot].encode(
            opacity=alt.condition(selection["shape"], alt.value(1), alt.value(0.2))
        )

    if "title" in my[plot]:
        chart[plot] = chart[plot].properties(title=my[plot]["title"])

    chart[plot] = chart[plot].encode(tooltip=list(tooltip))

    plotname = "_".join(filter(lambda x: bool(x), [name, plot[0], plot[1]]))
    save(
        chart=chart[plot],
        df=dfx,
        plotname=plotname,
        outputdir="../plots",
        formats=["json", "tablehtml", "tablemd", "md", "html", "png", "pdf"],
        sortby=[
            "primitive",
            "dataset",
            "engine",
            "gunrock_version",
            "advance_mode",
            "undirected",
            "mark_pred",
            "idempotence",
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
