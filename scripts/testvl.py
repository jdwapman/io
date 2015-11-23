#!/usr/bin/env python

import pandas  # http://pandas.pydata.org
import numpy
import json    # built-in
import os      # built-in
from subprocess import Popen, PIPE, STDOUT # built-in

## Load all JSON files into an array of dicts.
## Each array element is one JSON input file (one run).
## Each JSON input file is a dict indexed by attribute.
## If we have more than one JSON object per file:
## http://stackoverflow.com/questions/20400818/python-trying-to-deserialize-multiple-json-objects-in-a-file-with-each-object-s

jsondir = '../gunrock-output/'

json_files = [f for f in os.listdir(jsondir)
              if (os.path.isfile(jsondir + f) and
                  (os.path.splitext(f)[1] == ".json") and
                  (os.path.basename(f).startswith("BFS") or
                   os.path.basename(f).startswith("DOBFS")) and
                  not os.path.basename(f).startswith("_"))]
data_unfiltered = [json.load(open(jsondir + jf)) for jf in json_files]
df = pandas.DataFrame(data_unfiltered)
## All data is now stored in the pandas DataFrame "df".

## Let's add a new column (attribute), conditional on existing columns.
## We'll need this to pivot later.
def setParameters(row):
    return (row['algorithm'] + ', ' +
            ('un' if row['undirected'] else '') + 'directed, ' +
            ('' if row['mark_predecessors'] else 'no ') + 'mark predecessors')
df['parameters'] = df.apply(setParameters, axis=1)

## Bar graph, restricted to BFS+mark-pred+undirected
## x axis: dataset, y axis: MTEPS
df_mteps = df[df['parameters'] == "BFS, undirected, mark predecessors"]

## draw bar graph
bar = {
    "marktype": "bar",
    "encoding": {
        "y": {"scale": {"type": "log"},
              "type": "Q",
              # "type": "quantitative",
              "field": "m_teps",
              "axis": {
                  "title": "MTEPS"
              }
        },
        "x": {"type": "O",
              # "type": "ordinal",
              "field": "dataset"
        }
    }
}

# this deletes everything except dataset (index) and m_teps columns
# DataFrame cast is only to allow to_dict to run on a df instead of a series
df_mteps = pandas.DataFrame(df_mteps.set_index('dataset')['m_teps'])
# turn dataset back into a vanilla column instead of index
df_mteps = df_mteps.reset_index()

# bar now has a full vega-lite description
bar["data"] = {"values" : df_mteps.to_dict(orient='records')}
print(json.dumps(bar))          # uses double-quotes, not single

# pipe it through vl2vg to turn it into vega
f_bar = open('_g_bar.json', 'w')
p = Popen(["vl2vg"], stdout=f_bar, stdin=PIPE)
bar_vg = p.communicate(input=json.dumps(bar))[0]
f_bar.close()

df_gbar = df[['dataset','parameters','m_teps',
              'algorithm', 'undirected', 'mark_predecessors']]

gbar = {
  "marktype": "bar",
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
            "type": "ordinal"
    },
  },
}

gbar["data"] = {"values" : df_gbar.to_dict(orient='records')}
print
print
print(json.dumps(gbar))

f_gbar = open('_g_gbar.json', 'w')
p = Popen(["vl2vg"], stdout=f_gbar, stdin=PIPE)
gbar_vg = p.communicate(input=json.dumps(gbar))[0]
f_gbar.close()

gbart = gbar
# swap "x" and "row"
gbart["encoding"]["x"], gbart["encoding"]["row"] = gbart["encoding"]["row"], gbart["encoding"]["x"]

f_gbart = open('_g_gbart.json', 'w')
p = Popen(["vl2vg"], stdout=f_gbart, stdin=PIPE)
gbart_vg = p.communicate(input=json.dumps(gbart))[0]
f_gbart.close()

jsondir = '../../gunrock/output/ab/'

json_files = [f for f in os.listdir(jsondir)
              if (os.path.isfile(jsondir + f) and
                  (os.path.basename(f).startswith("DOBFS_soc")) and
                  (os.path.splitext(f)[1] == ".json") and
                  not os.path.basename(f).startswith("_"))]
data_unfiltered = [json.load(open(jsondir + jf)) for jf in json_files]
dfab = pandas.DataFrame(data_unfiltered)
## All data is now stored in the pandas DataFrame "dfab".
dfab = dfab[['dataset', 'm_teps', 'alpha', 'beta']]
## rint is numpy's vectorized round-to-int
dfab = dfab.assign(m_teps_rounded = numpy.rint(dfab['m_teps']))

print dfab

heatmap = {
    "marktype": "text",
    "encoding": {
        "row": {
            "field": "alpha",
            # "type": "ordinal",
            "type": "O"
        },
        "column": {
            "field": "beta",
            "type": "O"
            # "type": "ordinal"
        },
        "color": {
            "field": "m_teps",
            "type": "Q",
            # "type": "quantitative",
        },
        "text": {
            "field": "m_teps_rounded",
            "type": "Q",
            # "type": "quantitative",
            "format": ""
        }
    },
    "config": {
        "textCellWidth": 28, # We haven't documented this because we are considering to move this to be either encoding.col(umn).width or encoding.text.cellWidth in 0.9.
    }
}

heatmap["data"] = {"values" : dfab.to_dict(orient='records')}
f_heatmap = open('_g_heatmap.json', 'w')
p = Popen(["vl2vg"], stdout=f_heatmap, stdin=PIPE)
heatmap_vg = p.communicate(input=json.dumps(heatmap))[0]
f_heatmap.close()

print(json.dumps(heatmap))          # uses double-quotes, not single
