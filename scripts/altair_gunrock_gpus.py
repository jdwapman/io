#!/usr/bin/env python

from altair import *
import pandas  # http://pandas.pydata.org
import numpy
import datetime

from fileops import save, wrapChartInMd
from filters import *
from logic import *

name = 'gunrock_gpus'

# begin user settings for this script
roots = ['../gunrock-output']
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
    renameGpuinfoname,  # now it's gpuinfo_name
]
fnFilterDFRows = [
    selectTag('topc_arch'),
    deleteZeroMTEPS,
    keepLatest(['algorithm', 'dataset', 'gunrock_version', 'gpuinfo_name']),
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
                     'engine',
                     'gunrock_version',
                     'gpuinfo_name',
                     'time',
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
                  axis=Axis(
                      title='Primitive',
                      orient='top',
                  )
                  ),
    y=Y('m_teps',
        axis=Axis(
            title='MTEPS',
        ),
        scale=Scale(type='log'),
        ),
    color=Color('gpuinfo_name:N',
                legend=Legend(
                    title='GPU',
                ),
                ),
    shape=Shape('gpuinfo_name:N',
                legend=Legend(
                    title='GPU',
                ),
                ),
)
print chart.to_dict(data=False)
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
             wrapChartInMd(chart, anchor=name) +
             """
[Source data](md_stats_%s_table_html.html), with links to the output JSON for each run
""" % name),
     )
