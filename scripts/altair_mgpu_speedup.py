#!/usr/bin/env python3

from altair import *
import pandas  # http://pandas.pydata.org
import numpy
import datetime

from fileops import save, getChartHTML
from filters import *
from logic import *

from scipy.stats import gmean

name = 'mgpu_speedup'

# begin user settings for this script
roots = ['../gunrock-output/ipdps17/eval_fig4']
fnFilterInputFiles = [
    fileEndsWithJSON,
]
fnPreprocessDF = [
]
fnFilterDFRows = [
    selectAnyOfThese('gpuinfo.name', ['Tesla K40m']),
    deleteZeroElapsed,          # prefer not to do this
]
fnPostprocessDF = [
    BFStoDOBFS,
    normalizeBy1GPU('speedup', 'elapsed',
                    ['algorithm', 'dataset', 'gpuinfo.name']),
    addJSONDetailsLink,
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
                     'direction_optimized',
                     'num_gpus',
                     'partition_method',
                     'speedup',
                     'engine',
                     'm_teps',
                     'elapsed',
                     'gunrock_version',
                     'gpuinfo.name',
                     'time',
                     'details']
# would prefer a cleanup call https://github.com/altair-viz/altair/issues/183
# without this, output is gigantic
df = (keepTheseColumnsOnly(columnsOfInterest))(df)
gmean_columns = ['algorithm', 'num_gpus']
# http://stackoverflow.com/questions/30795858/add-calculated-row-to-pandas-dataframe
dfgmean = df.groupby(gmean_columns).agg(lambda x: gmean(list(x)))
dfgmean = dfgmean.reset_index()
save(df=dfgmean,
     plotname='%s_gmean' % name,
     formats=['tablehtml'],
     sortby=gmean_columns,
     columns=gmean_columns + ['speedup']
     )

# now make the graph

chart = {}
sortby_dict = {'all': ['algorithm',
                       'dataset',
                       'partition_method',
                       'num_gpus'
                       ],
               'geomean': ['algorithm',
                           'num_gpus',
                           ]
               }
columnsOfInterest_dict = {'all': columnsOfInterest,
                          'geomean': sortby_dict['geomean'] + ['speedup'],
                          }
for data in ['all', 'geomean']:
    if (data == 'all'):
        dfplot = df
        chart[data] = Chart(dfplot).mark_point().encode(
            x=X('num_gpus:N',
                axis=Axis(
                    title='Number of GPUs',
                ),
                ),
            column=Column('algorithm:N',
                          header=Header(
                              title='Primitive'
                          ),
                          ),
            y=Y('speedup',
                axis=Axis(
                    title='%sSpeedup over 1 GPU' % ('Geomean ' if (
                        data == 'geomean') else ''),
                ),
                # scale=Scale(type='log'),
                ),
            shape=Shape('dataset',
                        legend=Legend(
                            title='Dataset',
                        ),
                        ),
            color=Color('dataset',
                        legend=Legend(
                            title='Dataset',
                        ),
                        ),
        ).transform_filter(
            datum.num_gpus != 1
        )
    if (data == 'geomean'):
        dfplot = dfgmean
        chart[data] = Chart(dfplot).mark_point().encode(
            x=X('num_gpus:N',
                axis=Axis(
                    title='Number of GPUs',
                ),
                ),
            column=Column('algorithm:N',
                          header=Header(
                              title='Primitive'
                          ),
                          ),
            y=Y('speedup',
                axis=Axis(
                    title='%sSpeedup over 1 GPU' % ('Geomean ' if (
                        data == 'geomean') else ''),
                ),
                # scale=Scale(type='log'),
                ),
        ).transform_filter(
            datum.num_gpus != 1
        )
    print([(key, value)
           for key, value in chart[data].to_dict().items() if key not in ['data']])
    save(df=dfplot,
         plotname=name + '_' + data,
         formats=['tablemd', 'tablehtml'],
         sortby=sortby_dict[data],
         columns=columnsOfInterest_dict[data],
         )

    save(chart=chart[data],
         df=dfplot,
         plotname=name + '_' + data,
         formats=['json', 'html', 'svg', 'png', 'pdf'],
         )

save(plotname=name,
     formats=['md'],
     mdtext=("""
# Speedup on multiple GPUs

We demonstrate multiple-GPU ("mGPU") speedup over 1GPU performance for six primitives: BC, BFS, CC, DOBFS, PR and SSSP. We show both speedups on individual datasets and geometric means of runtime speedup over all datasets. These experiments are on NVIDIA Tesla K40m GPUs.

Most of the primitives scale fairly well from 1 to 6 GPUs. The exception is DOBFS, which (unlike the other experiments) is primarily limited by communication overhead.

""" +
             getChartHTML(chart['all'], anchor='%s_all' % name) +
             getChartHTML(chart['geomean'], anchor='%s_geomean' % name) + """
[Source data](tables/%s_%s_table.html), with links to the output JSON for each run<br/>
""" % (name, 'all') + """
[Geomean source data](tables/%s_%s_table.html)
""" % (name, 'geomean')
     ))
