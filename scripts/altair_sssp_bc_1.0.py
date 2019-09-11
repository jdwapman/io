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
         '../gunrock-output/v1-0-0/tc']
fnFilterInputFiles = [
    fileEndsWithJSON,
]
fnPreprocessDF = [
    # convertCtimeStringToDatetime,
    # normalizePRMTEPS,
    mergeAlgorithmIntoPrimitive,
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

for primitive in ['SSSP', 'bc', 'tc']:
    dfx = df[df['primitive'] == primitive]

    xval = {'SSSP': 'dataset:N',
            'bc': 'dataset:N',
            'tc': 'num-edges:Q',
            }
    xtext = {'SSSP': 'Dataset',
             'bc': 'Dataset',
             'tc': 'Number of Edges',
             }
    xscale = {'SSSP': 'linear',
              'bc': 'linear',
              'tc': 'log',
              }
    yval = {'SSSP': 'avg-mteps:Q',
            'bc': 'avg-mteps:Q',
            'tc': 'avg-process-time:Q',
            }
    ytext = {'SSSP': 'MTEPS',
             'bc': 'MTEPS',
             'tc': 'Runtime (ms)',
             }

    chart[primitive] = alt.Chart(dfx).mark_point().encode(
        x=alt.X(xval[primitive],
                axis=alt.Axis(
                    title=xtext[primitive],
        ),
            scale=alt.Scale(type=xscale[primitive]),

        ),
        y=alt.Y(yval[primitive],
                axis=alt.Axis(
                    title=ytext[primitive],
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

    plotname = name + '_' + primitive
    save(chart=chart[primitive],
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
         # Titan V

         """ +
                 getChartHTML(chart[primitive], anchor=plotname) +
                 """
                 [Source data](tables/%s_table.html), with links to the output JSON for each run
                 """ % plotname),
         )
