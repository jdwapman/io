#!/usr/bin/env python3

import altair as alt
import pandas  # http://pandas.pydata.org
import numpy
import datetime

from fileops import save, getChartHTML
from filters import *
from logic import *

name = "gunrock_version_compare"
prims = ["bc", "bfs", "pr", "sssp"]
gpus = ["Tesla V100", "Tesla K40/80"]

# begin user settings for this script
roots = [
    "../gunrock-output/",
]
fnFilterInputFiles = [
    fileEndsWithJSON,
    fileNotInArchiveDir,
]
fnPreprocessDF = [
    # convertCtimeStringToDatetime,
    # normalizePRMTEPS,
    selectAnyOfThese("engine", ["Gunrock"]),  # only Gunrock
    lambda df: df[df["num_gpus"].isnull() | (df["num_gpus"] == 1)],  # single GPU only
    mergeAlgorithmIntoPrimitive,
    mergeAllUpperCasePrimitives,
    selectAnyOfThese("primitive", prims),
    mergeIdempotentToIdempotence,
    mergeMarkPredecessors,
    mergeMHyphenTEPSIntoAvgMTEPS,
    mergeElapsedIntoAvgProcessTime,
    mergeMaxIterationIntoMaxIter,
    mergeTraversalModeWithUnderscoreIntoAdvanceModeWithHyphen,
    deleteZero("avg-process-time"),
    mergeMinusSignsIntoUnderscores,
    normalizePRByIterations,
    renameColumnsWithMinus,
    undirectedAndIdempotenceAndMarkPred,
    undirectedAndMarkPred,
    undirectedAndPull,
    # all col names at this point should be 1.0+ schema and underscores only
]
fnFilterDFRows = [
    filterOut(True, "64bit_SizeT"),
    filterOut(True, "64bit_VertexT"),
]
fnPostprocessDF = [
    equateNVIDIAGPUs,
    selectAnyOfThese("gpuinfo_name", gpus),
    combineGunrock1Plus,
    keepFastestAvgProcessTime(
        columns=["primitive", "dataset", "gunrock_version", "gpuinfo_name"],
        sortBy="avg_process_time",
    ),
    normalizeToGunrock1Plus(
        dest="speedup_vs_10+",
        quantityToNormalize="avg_process_time",
        columnsToGroup=["primitive", "dataset", "gpuinfo_name"],
    ),
    addJSONDetailsLink,
    gunrockVersionGPU,
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
    "avg_process_time_10+",
    "speedup_vs_10+",
    "engine",
    "gunrock_version",
    "gpuinfo_name",
    "gpuinfo_name_full",
    # 'tag',
    "num_vertices",
    "num_edges",
    "nodes_visited",
    "edges_visited",
    "search_depth",
    "advance_mode",
    "idempotence",
    "undirected",
    "mark_pred",
    "undirected_idempotence_markpred",
    "undirected_markpred",
    "undirected_pull",
    "pull",
    "64bit_SizeT",
    "64bit_VertexT",
    "time",
    "details",
]
# would prefer a cleanup call https://github.com/altair-viz/altair/issues/183
# without this, output is gigantic
df = (keepTheseColumnsOnly(columnsOfInterest))(df)

prim_fullname = {
    "bfs": "BFS",
    "sssp": "SSSP",
    "tc": "Triangle Counting",
    "bc": "Betweenness Centrality",
    "pr": "PageRank",
}

datatypes = {
    "advance_mode": "nominal",
    "avg_mteps": "quantitative",
    "avg_process_time": "quantitative",
    "avg_process_time_10+": "quantitative",
    "dataset": "nominal",
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
    "speedup_vs_10+": "quantitative",
    "undirected": "nominal",
    "undirected_idempotence_markpred": "nominal",
    "undirected_markpred": "nominal",
    "undirected_pull": "nominal",
}

specific = {
    "bc": ("undirected", "Undirected"),
    "bfs": (
        "undirected_idempotence_markpred",
        "Undirected / Idempotence / Mark Predecessors",
    ),
    "pr": ("undirected_pull", "Undirected / Pull"),
    "sssp": ("undirected_markpred", "Undirected / Mark Predecessors"),
}


# now make the graph

chart = {}

my = {}

for prim in prims:
    for gpu in gpus:
        my[(prim, gpu, "all")] = {
            "mark": "point",
            "x": ("dataset", "Dataset", "linear"),
            "y": ("speedup_vs_10+", "Speedup, normalized to Gunrock 1.0+", "log"),
            "color": ("gunrock_version", "Gunrock Version"),
            "shape": ("gunrock_version", "Gunrock Version"),
            # "prim=prim" forces "prim" to bind to the primitive in the above loop
            # otherwise it binds when it's called, that's bad
            "filter": lambda df, prim=prim, gpu=gpu: df[
                (df["primitive"] == prim) & (df["gpuinfo_name"] == gpu)
            ],
            "title": f"{prim_fullname[prim]}: Normalized Performance on {gpu}",
        }
        my[(prim, gpu, specific[prim][0])] = my[(prim, gpu, "all")].copy()
        my[(prim, gpu, specific[prim][0])]["row"] = specific[prim]


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
        generateTooltip("avg_process_time"),
        generateTooltip("avg_process_time_10+"),
        generateTooltip("speedup_vs_10+"),
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
        generateTooltip("pull"),
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
                    # scale=alt.Scale(scheme="dark2"),
                ),
                opacity=alt.condition(selection["color"], alt.value(1), alt.value(0.2)),
            )
            .add_selection(selection["color"])
        )

    if "shape" in my[plot]:
        shape = stripShorthand(my[plot]["shape"][0])
        chart[plot] = chart[plot].encode(
            shape=alt.Shape(
                shape,
                type=datatypes[shape],
                legend=alt.Legend(title=my[plot]["shape"][1]),
            )
        )
        # commented out b/c I don't know what to do with shape selection
        # selection["shape"] = alt.selection_multi(fields=[shape], bind="legend")
        # chart[plot] = chart[plot].add_selection(selection["shape"])

    if "title" in my[plot]:
        chart[plot] = chart[plot].properties(title=my[plot]["title"])

    chart[plot] = chart[plot].encode(tooltip=list(tooltip))

    plotname = (
        "_".join(filter(lambda x: bool(x), [name, plot[0], plot[1], plot[2]]))
        .replace("/", "_")
        .replace(" ", "_")
    )  # gpu names might have a '/' or ' ' in them
    save(
        chart=chart[plot],
        df=dfx,
        plotname=plotname,
        outputdir="../plots",
        formats=["json", "tablehtml", "tablemd", "html", "png", "pdf"],
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
    )
