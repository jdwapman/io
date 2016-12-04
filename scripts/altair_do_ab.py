#!/usr/bin/env python

from altair import *
import pandas  # http://pandas.pydata.org
import numpy
import datetime

from fileops import save
from filters import *
from logic import *

name = 'do_ab'

# begin user settings for this script
roots = ['../gunrock-output/topc-param-sweeps', ]
fnFilterInputFiles = [
    fileEndsWithJSON,
]
fnPreprocessDF = [
    addJSONDetailsLink,
]
fnFilterDFRows = [
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

colormap = Scale(range=['#e8e8e8', '#171717'])

for dataset in ['hollywood-2009', 'indochina-2004', 'rmat_n22_e64',
                'rmat_n23_e32', 'rmat_n24_e16', 'road_usa',
                'soc-LiveJournal1', 'soc-orkut', ]:
    dfd = df[df['dataset'] == dataset]

    # format argument:
    # https://github.com/altair-viz/altair/commit/1f6d1aaaba74b807430b8452592a3635336644cf
    # https://github.com/d3/d3-format/blob/master/README.md#format
    chart = Chart(dfd).mark_text(applyColorToBackground=True).encode(
        row=Row('do_a:O',
                axis=Axis(format='.1',
                          title='do_a',
                          ),
                ),
        column=Column('do_b:O',
                      axis=Axis(format='.1',
                                title='do_b',
                                ),
                      ),
        color=Color('m_teps',
                    scale=colormap,
                    ),
        text=Text(value=' '),
    ).configure_scale(
        textBandWidth=20,
        bandSize=20
    )
    print chart.to_dict(data=False)
    save(chart=chart,
         df=dfd,
         plotname='%s_%s' % (name, dataset),
         formats=['html', 'svg', 'png', 'pdf', 'tablehtml'],
         sortby=['algorithm',
                 'dataset',
                 'do_a',
                 'do_b'],
         columns=['algorithm',
                  'dataset',
                  'do_a',
                  'do_b',
                  'm_teps',
                  'engine',
                  'edges_visited',
                  'elapsed',
                  'gunrock_version',
                  'gpuinfo.name',
                  'details']
         )
