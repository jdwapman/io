#!/usr/bin/env python

from altair import *
import pandas  # http://pandas.pydata.org
import numpy
import datetime

from fileops import save, wrapChartInMd
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
               '../NVGraph-output',
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
                           datetime.date(2016, 12, 23),
                           ]),
    # 2016/11/17 is gunrock-output/topc/
    # 2016/11/20 is Galois-output/topc/
    # 2016/11/{25,30} is MapGraph-output/topc/
    # 2016/11/{25,26} is hardwired/topc/
    # 2016/11/26 is Ligra-output/topc/
    # 2016/11/28 is CuSha-output/topc/
    # 2016/12/23 is NVGraph-output/topc/
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

df = df.append(dfpatch)
# next line should filter the duplicate PRs
df = (keepFastest(['algorithm', 'dataset', 'engine']))(df)
# then let's compute 'speedup'
df = normalizeByGunrock('speedup', 'elapsed',
                        ['algorithm', 'dataset'])(df)

columnsOfInterest = ['algorithm',
                     'sub_algorithm',
                     'dataset',
                     'engine',
                     'm_teps',
                     'elapsed',
                     'speedup',
                     'gunrock_version',
                     'gpuinfo.name',
                     'time',
                     'details']
# would prefer a cleanup call https://github.com/altair-viz/altair/issues/183
# without this, output is gigantic
df = (keepTheseColumnsOnly(columnsOfInterest))(df)

# now make the graph

chart = {}
for (data, caption) in [('m_teps', 'MTEPS'), ('elapsed', 'Elapsed time (ms)')]:

    chart[data] = Chart(df).mark_point().encode(
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
    print chart[data].to_dict(data=False)
    save(chart=chart[data],
         df=df,
         plotname='%s_%s' % (name, data),
         formats=['json', 'html', 'svg', 'png', 'pdf'],
         )

# https://github.com/altair-viz/altair/issues/289#issuecomment-270949488
# Maybe like this?
# Mark: symbol
# Y: Dataset
# Row: Library
# X: Speedup (log scale axis)
# Column: Algorithm
# Color: Speedup < 1
data = 'speedup'
chart[data] = Chart(df[df['engine'] != 'Gunrock']).mark_point().encode(
    y=Y('dataset:N',
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
    row=Row('engine',
            ),
    x=X('speedup',
        axis=Axis(
            title="Gunrock's speedup",
        ),
        scale=Scale(type='log'),
        ),
    color=Color('faster_or_slower:N',
                scale=Scale(
                    range=['#a0a0a0', '#101010'],
                ),
                legend=Legend(
                    title="Gunrock's speedup",
                ),
                ),
).transform_data(
    calculate=[Formula(
        expr='datum.speedup < 1 ? "< 1" : ">= 1"',
        field='faster_or_slower',
    )],
)
print chart[data].to_dict(data=False)
save(chart=chart[data],
     df=df,
     plotname='%s_%s' % (name, data),
     formats=['json', 'html', 'svg', 'png', 'pdf'],
     )


save(df=df,
     plotname=name,
     formats=['tablemd', 'tablehtml'],
     sortby=['algorithm',
             'dataset',
             'engine', ],
     columns=columnsOfInterest,
     )

save(plotname=name,
     formats=['md'],
     mdtext=("""
# Comparison with Other Engines

We compared Gunrock against several other engines for graph analytics:

- [CuSha (GPU)](http://farkhor.github.io/CuSha/)
- [Galois (CPU)](http://iss.ices.utexas.edu/?p=projects/galois)
- Hardwired (primitive-specific) (GPU)
- [Ligra (CPU)](http://jshun.github.io/ligra/)
- [MapGraph (GPU)](https://www.blazegraph.com/mapgraph-technology/)
- [nvGRAPH (GPU)](https://developer.nvidia.com/nvgraph)

Below are comparative results on 5 primitives times 9 datasets in terms
of graph throughput (millions of edges per second, MTEPS) ...
""" +
             wrapChartInMd(chart['m_teps'], anchor='MTEPS') +
             """
... and elapsed time (ms).
""" +
             wrapChartInMd(chart['elapsed'], anchor='elapsed') +
             """
Here's a "Small Multiple Dot Plot" ([design by Joe Mako](https://policyviz.com/hmv_post/run-time-column-chart/)) that shows Gunrock speedup over different engines on different primitives and datasets:
""" +
             wrapChartInMd(chart['speedup'], anchor='speedup') +
             """
[Source data](md_stats_%s_table_html.html), with links to the output JSON for each run
""" % name),
     )
