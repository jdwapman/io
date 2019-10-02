#!/usr/bin/env python3

import altair as alt
import pandas  # http://pandas.pydata.org
import numpy
import datetime

from fileops import save, getChartHTML
from filters import *
from logic import *

name = 'gunrock_sssp_bc_1_0'

# begin user settings for this script
roots = ['../gunrock-output/v1-0-0/sssp',
         '../gunrock-output/v1-0-0/bc',
         '../gunrock-output/v1-0-0/tc',
         '../gunrock-output/v1-0-0/pr']
fnFilterInputFiles = [
    fileEndsWithJSON,
]
fnPreprocessDF = [
    # convertCtimeStringToDatetime,
    # normalizePRMTEPS,
    mergeAlgorithmIntoPrimitive,
    SSSPtosssp,
    addJSONDetailsLink,
    gunrockVersionGPU,
]
fnFilterDFRows = [
    filterOut(True, '64bit-SizeT'),
    filterOut(True, '64bit-VertexT'),
]
fnPostprocessDF = [
]
# end user settings for this script

# actual program logic
# do not modify

# choose input files
df = filesToDF(roots=roots,
               fnFilterInputFiles=fnFilterInputFiles)
for fn in fnPreprocessDF:       # alter entries / compute new entries
    df = fn(df)
for fn in fnFilterDFRows:       # remove rows
    df = fn(df)
for fn in fnPostprocessDF:      # alter entries / compute new entries
    df = fn(df)

# end actual program logic

columnsOfInterest = ['primitive',
                     'dataset',
                     'avg-mteps',
                     'avg-process-time',
                     'engine',
                     # 'tag',
                     'num-vertices',
                     'num-edges',
                     'gunrock-version',
                     'gpuinfo.name',
                     'advance-mode',
                     'undirected',
                     'mark-pred',
                     '64bit-SizeT',
                     '64bit-VertexT',
                     'time',
                     'details']
# would prefer a cleanup call https://github.com/altair-viz/altair/issues/183
# without this, output is gigantic
df = (keepTheseColumnsOnly(columnsOfInterest))(df)

# now make the graph

chart = {}

for primtuple in [('sssp', ''), ('bc', ''), ('tc', ''),  ('tc', 'edges'),
                  ('pr', '')]:
    primitive = primtuple[0]
    dfx = df[df['primitive'] == primitive]

    xval = {('sssp', ''): 'dataset:N',
            ('bc', ''): 'dataset:N',
            ('tc', ''): 'dataset:N',
            ('tc', 'edges'): 'num-edges:Q',
            ('pr', ''): 'dataset:N',
            }
    xtext = {('sssp', ''): 'Dataset',
             ('bc', ''): 'Dataset',
             ('tc', ''): 'Dataset',
             ('tc', 'edges'): 'Number of Edges',
             ('pr', ''): 'Dataset',
             }
    xscale = {('sssp', ''): 'linear',
              ('bc', ''): 'linear',
              ('tc', ''): 'linear',
              ('tc', 'edges'): 'log',
              ('pr', ''): 'linear',
              }
    yval = {('sssp', ''): 'avg-mteps:Q',
            ('bc', ''): 'avg-mteps:Q',
            ('tc', ''): 'avg-process-time:Q',
            ('tc', 'edges'): 'avg-process-time:Q',
            ('pr', ''): 'avg-process-time:Q',
            }
    ytext = {('sssp', ''): 'MTEPS',
             ('bc', ''): 'MTEPS',
             ('tc', ''): 'Runtime (ms)',
             ('tc', 'edges'): 'Runtime (ms)',
             ('pr', ''): 'Runtime (ms)',
             }

    chart[primtuple] = alt.Chart(dfx).mark_point().encode(
        x=alt.X(xval[primtuple],
                axis=alt.Axis(
                    title=xtext[primtuple],
        ),
            scale=alt.Scale(type=xscale[primtuple]),

        ),
        y=alt.Y(yval[primtuple],
                axis=alt.Axis(
                    title=ytext[primtuple],
        ),
            scale=alt.Scale(type='log'),
        ),
        column=alt.Column('mark-pred:O',
                          header=alt.Header(title='Mark Predecessors'),
                          ),
        row=alt.Row('undirected:O',
                    header=alt.Header(title='Undirected'),
                    ),
        color=alt.Color('advance-mode:N',
                        legend=alt.Legend(
                            title='Advance Mode',
                        ),
                        scale=alt.Scale(scheme='dark2'),
                        ),
        shape=alt.Shape('[gpuinfo.name]:N',
                        legend=alt.Legend(
                            title='GPU',
                        ),
                        ),
        tooltip=['primitive', 'dataset:N', '[gpuinfo.name]:N', 'num-vertices',
                 'num-edges', 'advance-mode:N',
                 'mark-pred', 'undirected', '64bit-SizeT', '64bit-VertexT',
                 'avg-mteps:Q', 'avg-process-time:Q'],
    ).interactive()

    plotname = name + '_' + primtuple[0] + primtuple[1]
    save(chart=chart[primtuple],
         df=dfx,
         plotname=plotname,
         formats=['tablehtml', 'tablemd', 'md', 'html', 'png', 'svg', 'pdf'],
         sortby=['primitive',
                 'dataset',
                 'engine',
                 'gunrock-version',
                 'undirected',
                 'mark-pred',
                 'advance-mode',
                 ],
         columns=columnsOfInterest,
         mdtext=("""
         # Multiple GPUs

         """ +
                 getChartHTML(chart[primtuple], anchor=plotname) +
                 """
                 [Source data](tables/%s_table.html), with links to the output JSON for each run
                 """ % plotname),
         )
