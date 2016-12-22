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
# first list does not have gpuinfo.name, second list does
# see comment below on "this weird double call"
rootslists = [['../CuSha-output', '../Galois-output', '../Ligra-output',
               '../HardwiredBC-output',
               '../HardwiredCC-output',
               ],
              ['../gunrock-output',
               '../MapGraph-output',
               '../HardwiredBFS-output',
               ]
              ]
fnFilterInputFiles = [
    fileEndsWithJSON,
]
fnPreprocessDF = [
    convertCtimeStringToDate,
    DOBFStoBFS,
    BFSCCtoCC,
    equateRGG,
    normalizePRMTEPS,
    addJSONDetailsLink,
    gunrockVersionGPU,
    replaceWith(src='Hardwired-BC', dest='Hardwired', column='engine'),
    replaceWith(src='Hardwired-CC', dest='Hardwired', column='engine'),
    replaceWith(src='Hardwired-BFS', dest='Hardwired', column='engine'),
]
fnFilterDFRows = [
    selectAnyOfTheseDates([datetime.date(2016, 11, 17),
                           datetime.date(2016, 11, 18),
                           datetime.date(2016, 11, 20),
                           datetime.date(2016, 11, 25),
                           datetime.date(2016, 11, 26),
                           datetime.date(2016, 11, 28),
                           datetime.date(2016, 11, 29),
                           datetime.date(2016, 11, 30),
                           ]),
    # 2016/11/17 is gunrock-output/topc/
    # 2016/11/20 is Galois-output/topc/
    # 2016/11/{25,30} is MapGraph-output/topc/
    # 2016/11/{25,26} is hardwired/topc/
    # 2016/11/26 is Ligra-output/topc/
    # 2016/11/28 is CuSha-output/topc/
    deselectTag('topc_arch'),
    deselectTag('do_sweep'),
    deselectTag('do_sweep2'),
    computeOtherMTEPSFromGunrock,
    deleteZeroMTEPS,
    deleteZeroElapsed,
    # pagerank has more m_teps than pagerankdelta.
    filterOut(value='pagerankdelta', column='sub_algorithm'),
    # Yeah, bitvector and radii can be removed.
    filterOut(value='bfs-bitvector', column='sub_algorithm'),
    filterOut(value='radii', column='sub_algorithm'),
    filterOut(value='Tesla P100-PCIE-16GB', column='gpuinfo.name'),
    keepFastest(['algorithm', 'dataset', 'engine']),
]

fnPostprocessDF = [
]
# end user settings for this script

# actual program logic
# do not modify

# choose input files
# this weird double call to filesToDF is because json_normalize doesn't
# appear to be doing the right thing when some but not all rows have
# nested schema
df = pandas.DataFrame()
for roots in rootslists:
    dfx = filesToDF(roots=roots,
                    fnFilterInputFiles=fnFilterInputFiles)
    df = df.append(dfx)

df = df.reset_index()

for fn in fnPreprocessDF:       # alter entries / compute new entries
    df = fn(df)
for fn in fnFilterDFRows:       # remove rows
    df = fn(df)
for fn in fnPostprocessDF:      # alter entries / compute new entries
    df = fn(df)

# end actual program logic

# now patch this up.
# replace all Gunrock/PR results with
# `gunrock/io/gunrock-output/topc/optimization-switch`, tag `optimization_test_LB`.

dfpatch = filesToDF(roots=['../gunrock-output/topc/optimization-switch'],
                    fnFilterInputFiles=fnFilterInputFiles)
for fn in [convertCtimeStringToDate,
           selectTag('optimization_test_LB'),
           selectAnyOfThese(column='algorithm', these=['PageRank']),
           normalizePRMTEPS,
           addJSONDetailsLink,
           gunrockVersionGPU,
           deleteZeroMTEPS,
           ]:
    dfpatch = fn(dfpatch)

df.to_csv('df0.csv')
df = df.append(dfpatch)
# next line should filter the duplicate PRs
df = (keepFastest(['algorithm', 'dataset', 'engine']))(df)

df.to_csv('df1.csv')
dfpatch.to_csv('dfpatch.csv')

# now make the graph

save(df=df,
     plotname=name,
     formats=['tablehtml'],
     sortby=['algorithm',
             'dataset',
             'sub_algorithm',
             'engine',
             'gunrock_version'],
     columns=['algorithm',
              'dataset',
              'sub_algorithm',
              'engine',
              'm_teps',
              'elapsed',
              'edges_visited',
              'gunrock_version',
              # 'gpuinfo.name',
              'time',
              'details'],
     )

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
        # color=Color('sub_algorithm:N',
        #             legend=Legend(
        #                 title='Algorithmic variant',
        #             ),
        #             ),
        shape=Shape('engine',
                    legend=Legend(
                        title='Engine',
                    ),
                    ),
        color=Color('engine',
                    legend=Legend(
                        title='Engine',
                    ),
                    ),
    )
    print chart.to_dict(data=False)
    save(chart=chart,
         df=df,
         plotname='%s_%s' % (name, data),
         formats=['json', 'html', 'svg', 'png', 'pdf'],
         )

save(df=df,
     plotname=name,
     formats=['tablehtml'],
     sortby=['algorithm',
             'dataset',
             'do_a',
             'do_b'],
     columns=['algorithm',
              'sub_algorithm',
              'dataset',
              'engine',
              'm_teps',
              'elapsed',
              'gunrock_version',
              'gpuinfo.name',
              'details']
     )
