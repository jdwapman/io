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
roots = ['../gunrock-output/v1-0-0/bfs/V100']
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
    renameMarkPredecessors,
    collapseAdvanceMode,
    renameMTEPSWithAHyphen,
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

columnsOfInterest = ['algorithm',
                     'dataset',
                     'm_teps',
                     'elapsed',
                     'engine',
                     # 'tag',
                     'gunrock_version',
                     # 'gpuinfo.name',
                     'advance_mode',
                     'undirected',
                     'idempotence',
                     'mark_predecessors',
                     'undirected_idempotence_markpred',
                     '64bit-SizeT',
                     '64bit-VertexT',
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
    y=alt.Y('m_teps',
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
    # tooltip=['[gpuinfo.name]:N', 'm_teps', 'elapsed', 'tag'],
    tooltip=['m_teps', 'elapsed'],
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
    y=alt.Y('m_teps',
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
    shape=alt.Shape('advance_mode:N',
                    legend=alt.Legend(
                        title='Advance Mode',
                    ),
                    ),
    # tooltip=['[gpuinfo.name]:N', 'm_teps', 'elapsed', 'tag'],
    tooltip=['m_teps', 'elapsed', 'advance_mode'],
).transform_filter(
    (alt.datum.undirected == '1') & (alt.datum.idempotence == "true") & (
        alt.datum.mark_predecessors == "false")
).interactive()


print([(key, value)
       for key, value in chart['lb'].to_dict().items() if key not in ['data']])
# was: print(chart.to_dict(data=False))
for key in list(chart):
    save(chart=chart[key],
         df=df,
         plotname=name + '_' + key,
         formats=['tablehtml', 'tablemd', 'md', 'html', 'svg', 'png', 'pdf'],
         sortby=['algorithm',
                 'dataset',
                 'engine',
                 'gunrock_version',
                 # 'advance_mode',
                 'undirected',
                 'idempotence',
                 'mark_predecessors',
                 ],
         columns=columnsOfInterest,
         mdtext=("""
         # V100

         """ +
                 getChartHTML(chart['full'], anchor=name) +
                 getChartHTML(chart['lb'], anchor=name) +
                 """
                 [Source data](tables/%s_table.html), with links to the output JSON for each run
                 """ % name),
         )
