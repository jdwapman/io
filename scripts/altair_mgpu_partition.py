#!/usr/bin/env python

from altair import *
import pandas  # http://pandas.pydata.org
import numpy
import datetime

from fileops import save, wrapChartInMd
from filters import *
from logic import *

name = 'mgpu_partition'

# begin user settings for this script
roots = ['../gunrock-output/ipdps17/eval_fig2']
fnFilterInputFiles = [
    fileEndsWithJSON,
]
fnPreprocessDF = [
]
fnFilterDFRows = [
]
fnPostprocessDF = [
    BFStoDOBFS,
    algorithmDataset,
    normalizeBy1GPU('speedup', 'elapsed',
                    ['algorithm', 'dataset', 'partition_method']),
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
                     'algorithm_dataset',
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

# now make the graph

chart = Chart(df).mark_point().encode(
    x=X('algorithm_dataset:N',
        axis=Axis(
            title='Algorithm / Dataset',
        ),
        ),
    y=Y('speedup',
        axis=Axis(
            title='Speedup',
        ),
        # scale=Scale(type='log'),
        ),
    shape=Shape('partition_method',
                legend=Legend(
                    title='Partition Method',
                ),
                ),
    color=Color('partition_method',
                legend=Legend(
                    title='Partition Method',
                ),
                ),
).transform_data(
    filter=(expr.df.num_gpus == 4)
)
print chart.to_dict(data=False)
save(chart=chart,
     df=df,
     plotname=name,
     formats=['json', 'html', 'svg', 'png', 'pdf'],
     )

save(df=df,
     plotname=name,
     formats=['tablemd', 'tablehtml'],
     sortby=['algorithm',
             'dataset',
             'partition_method',
             'num_gpus'
             ],
     columns=columnsOfInterest,
     )

save(plotname=name,
     formats=['md'],
     mdtext=("""
# Speedup for different partition methods

Below are comparative results on 5 primitives times 9 datasets in terms
of graph throughput (millions of edges per second, MTEPS) ...
""" +
             wrapChartInMd(chart, anchor='partition_methods') +
             """
[Source data](md_stats_%s_table_html.html), with links to the output JSON for each run
""" % name),
     )
