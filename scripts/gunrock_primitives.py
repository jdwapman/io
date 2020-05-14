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
    BFStoDOBFS10,
    copyQueuedToVisitedForPR,
    computeMTEPSFromEdgesAndElapsed10,
    mergeMaxIterationIntoMaxIter,
    normalizePRByIterations,
    renameColumnsWithMinus,
    # get rid of all tc + directed
    lambda df: df[(df["primitive"] != "tc") | (df["undirected"] == True)],
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
    "pull",
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
    "bfs": "BFS",
    "dobfs": "DOBFS",
    "sssp": "SSSP",
    "tc": "Triangle Counting",
    "bc": "Betweenness Centrality",
    "pr": "PageRank",
}

datatypes = {
    "dataset": "nominal",
    "avg_mteps": "quantitative",
    "max(avg_mteps)": "quantitative",
    "avg_process_time": "quantitative",
    "min(avg_process_time)": "quantitative",
    "num_vertices": "quantitative",
    "num_edges": "quantitative",
    "nodes_visited": "quantitative",
    "edges_visited": "quantitative",
    "search_depth": "quantitative",
    "mark_pred": "ordinal",
    "undirected": "ordinal",
    "advance_mode": "nominal",
    "gpuinfo_name": "nominal",
    "gpuinfo_name_full": "nominal",
    "primitive": "nominal",
    "pull": "nominal",
}

chart = {}

my = {}

for prim in ["bfs", "dobfs", "sssp", "tc", "bc", "pr"]:
    my[(prim, "mteps")] = {
        "mark": "point",
        "x": ("dataset", "Dataset", "linear"),
        "y": ("max(avg_mteps)", "MTEPS", "log"),
        "row": ("undirected", "Undirected"),
        "color": ("gpuinfo_name", "GPU"),
        "shape": ("gpuinfo_name", "GPU"),
        # "prim=prim" forces "prim" to bind to the primitive in the above loop
        # otherwise it binds when it's called, that's bad
        "filter": lambda df, prim=prim: df[df["primitive"] == prim],
        "title": f"{prim_fullname[prim]}: Fastest Gunrock 1.0+ runs (measured in MTEPS)",
    }
    if prim == "sssp" or prim == "bfs" or prim == "dobfs":
        # for SSSP/BFS/DOBFS, mark_pred is significant, but not for the others
        my[(prim, "mteps")]["col"] = ("mark_pred", "Mark Predecessors")

    # avg_process_time is identical except pick the min
    my[(prim, "avg_process_time")] = my[(prim, "mteps")].copy()
    my[(prim, "avg_process_time")]["y"] = (
        # pr has a normalized runtime per iteration (already computed),
        # but fix the caption
        "min(avg_process_time)",
        "Per_iteration runtime (ms)" if prim == "pr" else "Runtime (ms)",
        "log",
    )
    my[(prim, "avg_process_time")][
        "title"
    ] = f"{prim_fullname[prim]}: Fastest Gunrock 1.0+ runs (measured in ms)"

    if prim == "tc":
        del my[(prim, "mteps")]  # we don't have MTEPS for tc
        del my[(prim, "avg_process_time")]["row"]  # only undirected

    my[(prim, "advance_mode")] = {
        "mark": "point",
        "x": ("dataset", "Dataset", "linear"),
        "y": ("max(avg_mteps)", "MTEPS", "log"),
        "row": ("undirected", "Undirected"),
        "color": ("advance_mode", "Advance Mode"),
        "shape": ("advance_mode", "Advance Mode"),
        "filter": lambda df, prim=prim: df[
            (df["primitive"] == prim) & (df["gpuinfo_name"] == "Tesla V100")
        ],
        "title": f"{prim_fullname[prim]}: Fastest Gunrock 1.0+ runs, per advance mode, measured on V100",
    }
    if prim == "sssp" or prim == "bfs" or prim == "dobfs":
        my[(prim, "advance_mode")]["col"] = ("mark_pred", "Mark Predecessors")
    if prim == "tc":
        del my[(prim, "advance_mode")]  # we don't have MTEPS for tc
    my[(prim, "edges")] = my[(prim, "avg_process_time")].copy()
    my[(prim, "edges")]["x"] = ("num_edges", "Number of Edges", "log")
    my[(prim, "edges")]["title"] = f"{prim_fullname[prim]}: Runtime vs. Number of Edges"

my[("all_V100", "edges_visited_vs_num_edges")] = {
    "mark": "point",
    "x": ("num_edges", "Number of Edges", "log"),
    "y": ("edges_visited", "Number of Edges Visited/Queued", "log"),
    "row": ("undirected", "Undirected"),
    "color": ("primitive", "Primitive"),
    "shape": ("primitive", "Primitive"),
    "filter": lambda df: df[
        (df["edges_visited"] > 0) & (df["gpuinfo_name"] == "Tesla V100")
    ],
    "title": "Edges Visited vs. Number of Edges, measured on V100",
}

my[("all_V100", "vertices_visited_vs_num_vertices")] = {
    "mark": "point",
    "x": ("num_vertices", "Number of Vertices", "log"),
    "y": ("nodes_visited", "Number of Vertices Visited/Queued", "log"),
    "row": ("undirected", "Undirected"),
    "color": ("primitive", "Primitive"),
    "shape": ("primitive", "Primitive"),
    "filter": lambda df: df[
        (df["nodes_visited"] > 0) & (df["gpuinfo_name"] == "Tesla V100")
    ],
    "title": "Vertices Visited vs. Number of Vertices, measured on V100",
}

my[("all_V100", "search_depth")] = {
    "mark": "point",
    "x": ("search_depth", "Search Depth", "log"),
    "y": ("avg_process_time", "Runtime (ms)", "log"),
    "row": ("undirected", "Undirected"),
    "color": ("primitive", "Primitive"),
    "shape": ("primitive", "Primitive"),
    "filter": lambda df: df[
        (df["search_depth"] > 0) & (df["gpuinfo_name"] == "Tesla V100")
    ],
    "title": "Runtime vs. Search Depth, measured on V100",
}


for plot in my.keys():
    # if plot[0] != "all_V100":
    # continue
    print(f"*** Processing {plot} ***")

    primitive = plot[0]
    if "filter" in my[plot]:
        dfx = my[plot]["filter"](df)
    else:
        dfx = df

    selection = {}

    # we assume that the only aggregate is max or min in the y channel
    def generateTooltip2(field, y):
        mmin = re.match(r"min\((.*)\)$", y)
        mmax = re.match(r"max\((.*)\)$", y)
        if mmin:
            return alt.Tooltip(
                field, alt.Aggregate(alt.ArgminDef(argmin=mmin.group(1)))
            )
        elif mmax:
            return alt.Tooltip(
                field, alt.Aggregate(alt.ArgmaxDef(argmax=mmax.group(1)))
            )
        else:
            return field

    # this is currying. will it bind correctly?
    def generateTooltip(field):
        return generateTooltip2(field=field, y=my[plot]["y"][0])

    tooltip = [
        "primitive",
        "dataset",
        generateTooltip("avg_mteps"),
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
        # tooltip |= {my[plot]["col"][0]}
    if "row" in my[plot]:
        chart[plot] = chart[plot].encode(
            row=alt.Row(
                my[plot]["row"][0],
                type=datatypes[my[plot]["row"][0]],
                header=alt.Header(title=my[plot]["row"][1]),
            )
        )
        # tooltip |= {my[plot]["row"][0]}
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
        # tooltip |= {my[plot]["color"][0]}
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
        # tooltip |= {my[plot]["shape"][0]}
        selection["shape"] = alt.selection_multi(fields=[shape], bind="legend")
        chart[plot] = chart[plot].add_selection(selection["shape"])

    if "title" in my[plot]:
        chart[plot] = chart[plot].properties(title=my[plot]["title"])

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
