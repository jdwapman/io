#!/usr/bin/env python

from altair import *
import pandas  # http://pandas.pydata.org
import numpy
import datetime

from fileops import save
from filters import *
from logic import *

name = 'all_0304_perf'

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
]
fnFilterDFRows = [  # selectAnyOfTheseDates([datetime.date(2016, 11, 10),
    #                        datetime.date(2016, 11, 12),
    #                        datetime.date(2016, 11, 13),
    #                        datetime.date(2016, 11, 29)]),
    selectTag('topc_arch'),  # this is datetime.date(2016, 11, 29)
    deleteZeroMTEPS,
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
    color=Color('gunrock_version_gpu:N',
                legend=Legend(
                    title='Gunrock Version / GPU',
                ),
                ),
    shape=Shape('gunrock_version_gpu:N',
                legend=Legend(
                    title='Gunrock Version / GPU',
                ),
                ),
)
print chart.to_dict(data=False)
save(chart=chart,
     df=df,
     plotname=name,
     formats=['html', 'svg', 'png', 'pdf', 'tablehtml'],
     sortby=['algorithm',
             'dataset',
             'engine',
             'gunrock_version'],
     columns=['algorithm',
              'dataset',
              'm_teps',
              'gunrock_version',
              'gpuinfo.name',
              'details'],
     )
