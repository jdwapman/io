#!/usr/bin/env python3

import altair as alt
import pandas  # http://pandas.pydata.org
import numpy
import datetime

from fileops import save, getChartHTML
from filters import *
from logic import *

name = 'gunrock_bfs_1_0'

# begin user settings for this script
roots = ['../gunrock-output/v1-0-0/bfs/P100']
fnFilterInputFiles = [
    fileEndsWithJSON,
]
fnPreprocessDF = [
    convertCtimeStringToDatetime,
    normalizePRMTEPS,
    addJSONDetailsLink,
    gunrockVersionGPU,
    thirtyTwoBitOnly,
    directionOptimizedOnly,
    renameAdvanceModeWithAHyphen,
    collapseAdvanceMode,
    # mergeMHyphenTEPSIntoAvgMTEPS,
    renameGunrockVersionWithAHyphen,
    undirectedAndIdempotenceAndMarkPred,
    # renameGpuinfoname,  # now it's gpuinfo_name
]
fnFilterDFRows = [
    # selectTags(['topc_arch', 'TitanV-Updated-CUDA-Properties',
    # 'V100-Updated-CUDA-Properties']),
    deleteZeroMTEPS,
    # keepLatest(['algorithm', 'dataset', 'gunrock_version'  # , 'gpuinfo.name'
    # ]),
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
                     'tag',
                     'gunrock_version',
                     'gpuinfo.name',
                     'advance_mode',
                     'undirected',
                     'idempotence',
                     'mark-pred',
                     'undirected_idempotence_markpred',
                     '64bit-SizeT',
                     '64bit-VertexT',
                     '64bit-ValueT',
                     'direction-optimized',
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
    y=alt.Y('avg-mteps',
            axis=alt.Axis(
                title='MTEPS',
            ),
            scale=alt.Scale(type='log'),
            ),
    color=alt.Color('advance_mode:N',  # brackets allow . in the field name
                    legend=alt.Legend(
                        title='Advance Mode',
                    ),
                    ),
    shape=alt.Shape('undirected_idempotence_markpred:N',
                    legend=alt.Legend(
                        title='Undirected / Idempotence / Mark Predecessors',
                    ),
                    ),
    tooltip=['avg-mteps', 'avg-process-time',
             'advance_mode, [gpuinfo.name]:N',
             'undirected', 'idempotence', 'mark-pred', 'tag',
             ],
).interactive()

print([(key, value)
       for key, value in chart['full'].to_dict().items() if key not in ['data']])
# was: print(chart.to_dict(data=False))

chart['lb'] = alt.Chart(df).mark_point().encode(
    x=alt.X('dataset:N',
            axis=alt.Axis(
                title='Dataset',
            ),
            ),
    y=alt.Y('avg-mteps',
            axis=alt.Axis(
                title='MTEPS',
            ),
            scale=alt.Scale(type='log'),
            ),
    color=alt.Color('advance_mode:N',
                    legend=alt.Legend(
                        title='Advance Mode',
                    ),
                    ),
    shape=alt.Shape('[gpuinfo.name]:N',
                    legend=alt.Legend(
                        title='GPU',
                    ),
                    ),
    tooltip=['avg-mteps', 'avg-process-time',
             'advance_mode, [gpuinfo.name]:N',
             'undirected', 'idempotence', 'mark-pred', 'tag',
             ],
).transform_filter(
    # ['mark-pred'] because datum.mark-pred doesn't parse
    alt.datum.undirected == True & alt.datum.idempotence == True & alt.datum[
        'mark-pred'] == True
).interactive()


print([(key, value)
       for key, value in chart['lb'].to_dict().items() if key not in ['data']])
# was: print(chart.to_dict(data=False))
for key in list(chart):
    save(chart=chart[key],
         df=df,
         plotname=name + '_' + key,
         formats=['tablehtml', 'tablemd', 'md', 'html', 'svg', 'png', 'pdf'],
         sortby=['primitive',
                 'dataset',
                 'engine',
                 'gunrock_version',
                 # 'advance_mode',
                 'undirected',
                 'idempotence',
                 'mark-pred',
                 ],
         columns=columnsOfInterest,
         mdtext=("""
         # BFS

         """ +
                 getChartHTML(chart['full'], anchor=name) +
                 getChartHTML(chart['lb'], anchor=name) +
                 """
                 [Source data](tables/%s_table.html), with links to the output JSON for each run
                 """ % name),
         )
