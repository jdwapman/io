#!/usr/bin/env python3

import altair as alt
import pandas  # http://pandas.pydata.org
import numpy
import datetime

from fileops import save, getChartHTML
from filters import *
from logic import *

name = 'gunrock_sssp_1_0'

# begin user settings for this script
roots = ['../gunrock-output/v1-0-0/sssp']
fnFilterInputFiles = [
    fileEndsWithJSON,
]
fnPreprocessDF = [
    # convertCtimeStringToDatetime,
    # normalizePRMTEPS,
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

columnsOfInterest = ['algorithm',
                     'dataset',
                     'avg-mteps',
                     'avg-process-time',
                     'engine',
                     # 'tag',
                     'gunrock-version',
                     # 'gpuinfo.name',
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

chart['full'] = alt.Chart(df).mark_point().encode(
    x=alt.X('dataset:N',
            axis=alt.Axis(
                title='Dataset',
            ),
            ),
    y=alt.Y('avg-mteps:Q',
            axis=alt.Axis(
                title='MTEPS',
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
    shape=alt.Shape('advance-mode:N',
                    legend=alt.Legend(
                        title='Advance Mode',
                    ),
                    ),
    tooltip=['avg-mteps:Q', 'avg-process-time:Q'],
).interactive()

print([(key, value)
       for key, value in chart['full'].to_dict().items() if key not in ['data']])
# was: print(chart.to_dict(data=False))

for key in list(chart):
    save(chart=chart[key],
         df=df,
         plotname=name + '_' + key,
         formats=['tablehtml', 'tablemd', 'md', 'html', 'png', 'svg', 'pdf'],
         sortby=['algorithm',
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
                 getChartHTML(chart['full'], anchor=name) +
                 """
                 [Source data](tables/%s_table.html), with links to the output JSON for each run
                 """ % name),
         )
