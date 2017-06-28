#!/usr/bin/env python

from altair import *
import pandas  # http://pandas.pydata.org
import numpy
import datetime

# excellent brewer color palettes https://jiffyclub.github.io/palettable/
from palettable import colorbrewer as cb

from fileops import save, wrapChartInMd
from filters import *
from logic import *

name = 'frontier'

# begin user settings for this script
roots = ['../gunrock-output/', ]
fnFilterInputFiles = [
    fileEndsWithJSON,
]
fnPreprocessDF = [
]
fnFilterDFRows = [
    selectTag('per_iter_stats'),
    # selectOneDataset('road_usa'),
    undirectedOnly,
    idempotentOnly,
    flattenArrays(['per_iteration_advance_input_frontier',
                   'per_iteration_advance_mteps',
                   'per_iteration_advance_output_frontier',
                   'per_iteration_advance_runtime',
                   ],
                  sample=True,
                  ),
]
fnPostprocessDF = [
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
# foo = open('log.html', 'w')
# foo.write(df.to_html())
# foo.close()

# end actual program logic

columnsOfInterest = ['algorithm',
                     'traversal_mode',
                     'dataset',
                     'engine',
                     'per_iteration_advance_input_frontier',
                     'per_iteration_advance_output_frontier',
                     'per_iteration_advance_mteps',
                     'per_iteration_advance_runtime',
                     'edges_visited',
                     'gunrock_version',
                     'gpuinfo.name',
                     'time',
                     'details']
# would prefer a cleanup call https://github.com/altair-viz/altair/issues/183
# without this, output is gigantic
df = (keepTheseColumnsOnly(columnsOfInterest))(df)


# now make the graph

chart = {}
base = 'per_iteration_advance'
for frontier in ['input', 'output']:
    chart[frontier] = Chart(df).mark_point().encode(
        x=X('%s_%s_frontier' % (base, frontier),
            axis=Axis(
                title='%s Frontier Size' % frontier.title(),
        ),
            scale=Scale(type='log'),
        ),
        y=Y('%s_mteps' % base,
            axis=Axis(
                title='Per-iteration MTEPS',
            ),
            scale=Scale(type='log'),
            ),

        shape=Shape('dataset',
                    ),
        color=Color('dataset',
                    scale=Scale(range=cb.diverging.Spectral_8.hex_colors),
                    ),
    )
    print chart[frontier].to_dict(data=False)

    save(chart=chart[frontier],
         df=df,
         plotname='%s_%s' % (frontier, name),
         formats=['html', 'svg', 'png', 'pdf', 'tablehtml'],
         sortby=['algorithm',
                 'dataset',
                 'engine',
                 'gunrock_version'],
         columns=['algorithm',
                  'dataset',
                  'engine',
                  '%s_%s_frontier' % (base, frontier),
                  '%s_mteps' % base,
                  '%s_runtime' % base,
                  'edges_visited',
                  'traversal_mode',
                  'gunrock_version',
                  'gpuinfo.name',
                  'details']
         )

save(df=df,
     plotname=name,
     formats=['tablemd', 'tablehtml'],
     sortby=['dataset'],
     columns=columnsOfInterest,
     )

save(plotname=name,
     formats=['md'],
     mdtext=("""
# Throughput vs. Frontier Size

While running BFS on several datasets, we extracted the MTEPS (throughput)
that we achieve on each iteration. What is our performance as a function
of the size of the input and output frontier?

Ideally, throughput is independent of the size of the input or output
frontier, but in practice, the GPU requires a significant amount of work
to become fully utilized. So for relatively small frontiers, as the size
of the frontier increases, so does the performance. Eventually we reach
maximum throughput. This is a significant reason why road-network-ish
graphs demonstrate a much smaller throughput (MTEPS) than scale-free
graphs; road networks just don't generate frontiers that are large
enough to fully utilize the GPU.

It appears from the results that the output frontier size is a better
predictor of performance than the input frontier size.

""" +
             wrapChartInMd(chart['input'], anchor='input_frontier') +
             wrapChartInMd(chart['output'], anchor='output_frontier') +
             """
[Source data](md_stats_%s_table_html.html), with links to the output JSON for each run
""" % name),
     )
