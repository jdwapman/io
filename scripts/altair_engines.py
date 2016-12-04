#!/usr/bin/env python

from altair import *
import pandas  # http://pandas.pydata.org
import numpy
import datetime

from fileops import save
from filters import *
from logic import *

name = 'engines_topc'

# begin user settings for this script
roots = ['../gunrock-output', '../CuSha-output',
         '../Galois-output', '../Ligra-output', '../MapGraph-output']
fnFilterInputFiles = [
    fileEndsWithJSON,
]
fnPreprocessDF = [
    convertCtimeStringToDatetime,
    DOBFStoBFS,
    BFSCCtoCC,
    equateRGG,
    normalizePRMTEPS,
    addJSONDetailsLink,
    gunrockVersionGPU,
]
fnFilterDFRows = [
    selectAnyOfTheseDates([datetime.date(2016, 11, 17),
                           datetime.date(2016, 11, 18),
                           datetime.date(2016, 11, 20),
                           datetime.date(2016, 11, 28),
                           datetime.date(2016, 11, 29)]),
    # 2016/11/17 is gunrock-output/topc/
    # 2016/11/20 is Galois-output/topc/
    # 2016/11/26 is Ligra-output/topc/
    # 2016/11/28 is CuSha-output/topc/
    deselectTag('topc_arch'),
    deselectTag('do_sweep'),
    computeOtherMTEPSFromGunrock,
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

for (data, caption) in [('m_teps', 'MTEPS'), ('elapsed', 'Elapsed time (ms)')]:

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
        y=Y(data,
            axis=Axis(
                title=caption,
            ),
            scale=Scale(type='log'),
            ),
        color=Color('sub_algorithm:N',
                    legend=Legend(
                        title='Algorithmic variant',
                    ),
                    ),
        shape=Shape('engine',
                    legend=Legend(
                        title='Engine',
                    ),
                    ),
    )
    print chart.to_dict(data=False)
    save(chart=chart,
         df=df,
         plotname='%s_%s' % (name, data),
         formats=['html', 'svg', 'png', 'pdf'],
         )

save(df=df,
     plotname=name,
     formats=['tablehtml'],
     sortby=['algorithm',
             'sub_algorithm',
             'dataset',
             'engine',
             'gunrock_version'],
     columns=['algorithm',
              'sub_algorithm',
              'dataset',
              'engine',
              'm_teps',
              'edges_visited',
              'elapsed',
              'gunrock_version',
              'gpuinfo.name',
              'details'],
     )
