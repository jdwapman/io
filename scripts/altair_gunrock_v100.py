#!/usr/bin/env python3

from altair import *
import pandas  # http://pandas.pydata.org
import numpy
import datetime

from fileops import save, getChartHTML
from filters import *
from logic import *

name = 'gunrock_v100'

# begin user settings for this script
roots = ['../gunrock-output/5Apps.ubuntu16.04_v100x1_dev_sha-b8949e8',
         '../gunrock-output/5Apps.ubuntu16.04_TitanVx1_dev_sha-b8949e8',
         '../gunrock-output/cuda10/',
         ]
fnFilterInputFiles = [
    fileEndsWithJSON,
]
fnPreprocessDF = [
    convertCtimeStringToDatetime,
    DOBFStoBFS,
    equateRGG,
    #     equateM40,
    normalizePRMTEPS,
    addJSONDetailsLink,
    gunrockVersionGPU,
    # renameGpuinfoname,  # now it's gpuinfo_name
]
fnFilterDFRows = [
    deleteZeroMTEPS,
    keepLatest(['algorithm', 'dataset',
                'gunrock_version', 'gpuinfo.name', 'tag']),
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
                     'gunrock_version',
                     'gpuinfo.name',
                     'time',
                     'tag',
                     'details']
# would prefer a cleanup call https://github.com/altair-viz/altair/issues/183
# without this, output is gigantic
df = (keepTheseColumnsOnly(columnsOfInterest))(df)

# now make the graph

chart = Chart(df).mark_point().encode(
    x=X('dataset:N',
        axis=Axis(
            title='Dataset',
        ),
        ),
    column=Column('algorithm:N',
                  header=Header(
                      title='Primitive'
                  ),
                  # for 'top' below: "I think we haven't implemented it yet as we switched from scales to Vega layouts for faceting. We will add it back eventually."
                  # https://github.com/altair-viz/altair/issues/720#issuecomment-379589240
                  # axis=Axis(
                  #     title='Primitive',
                  #     orient='top',
                  # )
                  ),
    y=Y('m_teps',
        axis=Axis(
            title='MTEPS',
        ),
        scale=Scale(type='log'),
        ),
    color=Color('tag:N',  # brackets allow . in the field name
                legend=Legend(
                    title='Tag',
                ),
                ),
    shape=Shape('tag:N',
                legend=Legend(
                    title='Tag',
                ),
                ),
    tooltip=['[gpuinfo.name]:N', 'm_teps', 'elapsed', 'tag'],
).interactive()

print([(key, value)
       for key, value in chart.to_dict().items() if key not in ['data']])
# was: print(chart.to_dict(data=False))
save(chart=chart,
     df=df,
     plotname=name,
     formats=['tablehtml', 'tablemd', 'md', 'html', 'svg', 'png', 'pdf'],
     sortby=['algorithm',
             'dataset',
             'engine',
             'gunrock_version'],
     columns=columnsOfInterest,
     mdtext=("""
# Comparison on Different GPUs

We ran Gunrock on several GPUs on 5 primitives times 9 datasets. As the compute and memory bandwidth capabilities of the GPUs increase, so does Gunrock's performance.
""" +
             getChartHTML(chart, anchor=name) +
             """
[Source data](tables/%s_table.html), with links to the output JSON for each run
""" % name),
     )
