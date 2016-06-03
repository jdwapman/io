#!/usr/bin/env python

import pandas  # http://pandas.pydata.org
import numpy
import json    # built-in
import os      # built-in
import copy    # built-in
from subprocess import Popen, PIPE, STDOUT  # built-in


def write_json(json_in, json_name):
    # pipe it through vl2vg to turn it into vega
    file = open('_g_%s.json' % json_name, 'w')
    p = Popen(["vl2vg"], stdout=file, stdin=PIPE)
    bar_vg = p.communicate(input=json.dumps(json_in))[0]
    file.close()


# Load all JSON files into an array of dicts.
# Each array element is one JSON input file (one run).
# Each JSON input file is a dict indexed by attribute.
# If we have more than one JSON object per file:
# http://stackoverflow.com/questions/20400818/python-trying-to-deserialize-multiple-json-objects-in-a-file-with-each-object-s

jsondir = '../gunrock-output/'

bfs_json_files = [f for f in os.listdir(jsondir)
                  if (os.path.isfile(jsondir + f) and
                      (os.path.splitext(f)[1] == ".json") and
                      (os.path.basename(f).startswith("BFS") or
                       os.path.basename(f).startswith("DOBFS")) and
                      not os.path.basename(f).startswith("_"))]
bfs_data_unfiltered = [json.load(open(jsondir + jf)) for jf in bfs_json_files]
bfs_df = pandas.DataFrame(bfs_data_unfiltered)
# All DOBFS/BFS data is now stored in the pandas DataFrame "bfs_df".

# Let's add a new column (attribute), conditional on existing columns.
# We'll need this to pivot later.


def setParameters(row):
    return (row['algorithm'] + ', ' +
            ('un' if row['undirected'] else '') + 'directed, ' +
            ('' if row['mark_predecessors'] else 'no ') + 'mark predecessors')
bfs_df['parameters'] = bfs_df.apply(setParameters, axis=1)

# Bar graph, restricted to BFS+mark-pred+undirected
# x axis: dataset, y axis: MTEPS
bfs_df_mteps = bfs_df[bfs_df['parameters']
                      == "BFS, undirected, mark predecessors"]

# draw bar graph
bar = {
    "mark": "point",
    "encoding": {
        "y": {"scale": {"type": "log"},
              "type": "quantitative",
              "field": "m_teps",
              "axis": {
                  "title": "MTEPS"
        }
        },
        "x": {"type": "ordinal",
              "field": "dataset"
              }
    }
}

# this deletes everything except dataset (index) and m_teps columns
# DataFrame cast is only to allow to_dict to run on a df instead of a series
bfs_df_mteps = pandas.DataFrame(bfs_df_mteps.set_index('dataset')['m_teps'])
# turn dataset back into a vanilla column instead of index
bfs_df_mteps = bfs_df_mteps.reset_index()

# bar now has a full vega-lite description
bar["data"] = {"values": bfs_df_mteps.to_dict(orient='records')}
print(json.dumps(bar))          # uses double-quotes, not single
write_json(bar, "bar")

# print df_mteps.to_string
# print df_mteps.to_html

df_gbar = bfs_df[['dataset', 'parameters', 'm_teps',
                  'algorithm', 'undirected', 'mark_predecessors']]

gbar = {
    "mark": "point",
    "encoding": {
        "y": {"scale": {"type": "log"},
              "field": "m_teps",
              "type": "quantitative",
              "axis": {
            "title": "MTEPS"
        }
        },
        "x": {"field": "dataset",
              "type": "nominal"
              },
        "row": {"field": "parameters",
                "type": "nominal"
                },
    },
}

gbar["data"] = {"values": df_gbar.to_dict(orient='records')}
print(json.dumps(gbar))
write_json(gbar, "gbar")

gbart = copy.deepcopy(gbar)
# swap "x" and "row"
gbart["encoding"]["x"], gbart["encoding"]["row"] = gbart[
    "encoding"]["row"], gbart["encoding"]["x"]
write_json(gbart, "gbart")

gbar1 = copy.deepcopy(gbar)
gbar1["encoding"]["color"] = gbar1["encoding"].pop("row")  # rename key
write_json(gbar1, "gbar1")

gbart1 = copy.deepcopy(gbart)
gbart1["encoding"]["color"] = gbart1["encoding"].pop("row")
write_json(gbart1, "gbart1")

abjsondir = '../gunrock-output/ab/'

json_files = [f for f in os.listdir(abjsondir)
              if (os.path.isfile(abjsondir + f) and
                  (os.path.basename(f).startswith("DOBFS_soc")) and
                  (os.path.splitext(f)[1] == ".json") and
                  not os.path.basename(f).startswith("_"))]
data_unfiltered = [json.load(open(abjsondir + jf)) for jf in json_files]
dfab = pandas.DataFrame(data_unfiltered)
# All data is now stored in the pandas DataFrame "dfab".
dfab = dfab[['dataset', 'm_teps', 'alpha', 'beta']]
# rint is numpy's vectorized round-to-int
dfab = dfab.assign(m_teps_rounded=numpy.rint(dfab['m_teps']))

print dfab

heatmap = {
    "mark": "text",
    "encoding": {
        "row": {
            "field": "alpha",
            "type": "ordinal",
        },
        "column": {
            "field": "beta",
            "type": "ordinal"
        },
        "color": {
            "field": "m_teps",
            "type": "quantitative",
        },
        "text": {
            "field": "m_teps_rounded",
            "type": "quantitative",
            "format": ""
        }
    },
    # "config": {
    #     "textCellWidth": 28, # We haven't documented this because we are considering to move this to be either encoding.col(umn).width or encoding.text.cellWidth in 0.9.
    # }
}

heatmap["data"] = {"values": dfab.to_dict(orient='records')}
f_heatmap = open('_g_heatmap.json', 'w')
p = Popen(["vl2vg"], stdout=f_heatmap, stdin=PIPE)
heatmap_vg = p.communicate(input=json.dumps(heatmap))[0]
f_heatmap.close()

print(json.dumps(heatmap))          # uses double-quotes, not single

print [f for f in os.listdir(jsondir)]
print os.listdir(jsondir)
cc_json_files = [f for f in os.listdir(jsondir)
                 if (os.path.isfile(jsondir + f) and
                     (os.path.splitext(f)[1] == ".json") and
                     os.path.basename(f).startswith("CC") and
                     not os.path.basename(f).startswith("_"))]
print cc_json_files
cc_data_unfiltered = [json.load(open(jsondir + jf)) for jf in cc_json_files]
cc_df = pandas.DataFrame(cc_data_unfiltered)
cc_bar = {
    "mark": "point",
    "encoding": {
        "y": {"scale": {"type": "log"},
              "type": "quantitative",
              "field": "m_teps",
              "axis": {
                  "title": "MTEPS"
        }
        },
        "x": {"type": "ordinal",
              "field": "dataset"
              }
    }
}

cc_df = pandas.DataFrame(cc_df.set_index('dataset')['m_teps'])
cc_df = cc_df.reset_index()
cc_bar["data"] = {"values": cc_df.to_dict(orient='records')}
print(json.dumps(cc_bar))
write_json(cc_bar, "cc_bar")

print [f for f in os.listdir(jsondir)]
print os.listdir(jsondir)
bc_json_files = [f for f in os.listdir(jsondir)
                 if (os.path.isfile(jsondir + f) and
                     (os.path.splitext(f)[1] == ".json") and
                     os.path.basename(f).startswith("BC") and
                     not os.path.basename(f).startswith("_"))]
print bc_json_files
bc_data_unfiltered = [json.load(open(jsondir + jf)) for jf in bc_json_files]
bc_df = pandas.DataFrame(bc_data_unfiltered)
bc_bar = {
    "mark": "point",
    "encoding": {
        "y": {"scale": {"type": "log"},
              "type": "quantitative",
              "field": "m_teps",
              "axis": {
                  "title": "MTEPS"
        }
        },
        "x": {"type": "ordinal",
              "field": "dataset"
              }
    }
}

bc_df = pandas.DataFrame(bc_df.set_index('dataset')['m_teps'])
bc_df = bc_df.reset_index()
bc_bar["data"] = {"values": bc_df.to_dict(orient='records')}
print(json.dumps(bc_bar))
write_json(bc_bar, "bc_bar")

print [f for f in os.listdir(jsondir)]
print os.listdir(jsondir)
sssp_json_files = [f for f in os.listdir(jsondir)
                   if (os.path.isfile(jsondir + f) and
                       (os.path.splitext(f)[1] == ".json") and
                       os.path.basename(f).startswith("SSSP") and
                       not os.path.basename(f).startswith("_"))]
print sssp_json_files
sssp_data_unfiltered = [json.load(open(jsondir + jf))
                        for jf in sssp_json_files]
sssp_df = pandas.DataFrame(sssp_data_unfiltered)
sssp_bar = {
    "mark": "point",
    "encoding": {
        "y": {"scale": {"type": "log"},
              "type": "quantitative",
              "field": "m_teps",
              "axis": {
                  "title": "MTEPS"
        }
        },
        "x": {"type": "ordinal",
              "field": "dataset"
              }
    }
}

sssp_df = pandas.DataFrame(sssp_df.set_index('dataset')['m_teps'])
sssp_df = sssp_df.reset_index()
sssp_bar["data"] = {"values": sssp_df.to_dict(orient='records')}
print(json.dumps(sssp_bar))
write_json(sssp_bar, "sssp_bar")
