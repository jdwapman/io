#!/usr/bin/env python

from altair import *
import pandas  # http://pandas.pydata.org
import numpy
import datetime

from fileops import save
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

# now make the graph

base = 'per_iteration_advance'
for frontier in ['input', 'output']:
    chart = Chart(df).mark_point().encode(
        x=X('%s_%s_frontier' % (base, frontier),
            axis=Axis(
                title='%s Frontier' % frontier.title(),
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
                    ),
    )
    print chart.to_dict(data=False)

    save(chart=chart,
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
