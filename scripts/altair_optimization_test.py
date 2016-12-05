#!/usr/bin/env python

from altair import *
import pandas  # http://pandas.pydata.org
import numpy
import datetime

from fileops import save
from filters import *
from logic import *

name = 'optimization_test'

# begin user settings for this script
roots = ['../gunrock-output/', ]
fnFilterInputFiles = [
    fileEndsWithJSON,
]
fnPreprocessDF = [
]
fnFilterDFRows = [
    selectAnyOfThese('tag', ['optimization_test_LBCULL_idem_dir',
                             'optimization_test_LBCULL_dir',
                             'optimization_test_LBCULL_idem',
                             'optimization_test_LBCULL'
                             ]),
    replaceFromDict({'optimization_test_LBCULL_idem_dir': 'idempotent and direction-optimized',
                     'optimization_test_LBCULL_dir': 'direction-optimized',
                     'optimization_test_LBCULL_idem': 'idempotent',
                     'optimization_test_LBCULL': '-'
                     },
                    in_column='tag', out_column='tag'),
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
# end actual program logic

# now make the graph

chart = Chart(df).mark_bar().encode(
    x=X('tag:N',
        axis=False,
        ),
    column=Column('dataset',
                  axis=Axis(
                      title='Dataset',
                      orient='bottom',
                  )
                  ),
    y=Y('m_teps',
        axis=Axis(
            title='MTEPS',
        ),
        scale=Scale(type='log'),
        ),
    color=Color('tag:N',
                legend=Legend(title='Optimizations'),
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
              'engine',
              'tag',
              'm_teps',
              'edges_visited',
              'traversal_mode',
              'gunrock_version',
              'gpuinfo.name',
              'details']
     )
