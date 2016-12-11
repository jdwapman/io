#!/usr/bin/env python

from altair import *
import pandas  # http://pandas.pydata.org
import numpy
import datetime

from fileops import save
from filters import *
from logic import *

name = 'do_ab_random'

# begin user settings for this script
roots = ['../gunrock-output/', ]
fnFilterInputFiles = [
    fileEndsWithJSON,
]
fnPreprocessDF = [
    addJSONDetailsLink,
    selectTag('do_sweep2'),
]
fnFilterDFRows = [
    deleteZeroMTEPS,
]

fnPostprocessDF = [
    computeNewMTEPSFromProcessTimes,
    roundSig('do_a'),
    roundSig('do_b'),
    # formatColumn('do_a', 'do_a', '{:,.0g}'),
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
dfab = pandas.DataFrame()

for dataset in ['hollywood-2009', 'indochina-2004', 'rmat_n22_e64',
                'rmat_n23_e32', 'rmat_n24_e16', 'road_usa',
                'soc-LiveJournal1', 'soc-orkut', ]:
    dfd = df[df['dataset'] == dataset]
    # Some edges_visited are small because the last run hit a small
    # component of the graph. However, the runtimes are correct,
    # because we threw out all small runtimes. So set edges_visited
    # for every run to max(edges_visited) and recompute MTEPS.
    dfd = recomputeMTEPSFromMax(dfd)

    if (dataset != 'road_usa'):
        dfab = dfab.append(dfd.loc[dfd.m_teps == max(dfd['m_teps'])])

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
                                labelAngle=-90.0,
                                labelAlign='left',
                                labelBaseline='middle',
                                offset=0.0,
                                ),
                      ),
        color=Color('m_teps',
                    scale=colormap,
                    legend=Legend(title='%s / MTEPS' % dataset),
                    ),
        text=Text(value=' '),
    ).configure_scale(
        textBandWidth=20,
        bandSize=20
    )
    print chart.to_dict(data=False)
    # foo = open('%s_%s.json' % (name, dataset), 'w')
    # foo.write(df.to_json())
    # foo.close()

    save(chart=chart,
         df=dfd,
         plotname='%s_%s' % (name, dataset),
         formats=['html', 'svg', 'png', 'pdf', 'tablehtml'],
         sortby=['algorithm',
                 'dataset',
                 'engine',
                 'gunrock_version'],
         columns=['algorithm',
                  'dataset',
                  'do_a',
                  'do_b',
                  'm_teps',
                  'edges_visited',
                  'elapsed',
                  'engine',
                  'gunrock_version',
                  'gpuinfo.name',
                  'details']
         )
dfab = dfab[['dataset', 'do_a', 'do_b', 'num_edges', 'num_vertices', 'm_teps']]
dfab['average_degree'] = dfab['num_edges'] / dfab['num_vertices']
print dfab

for y_axis in ['do_a', 'do_b']:
    chart = Chart(dfab).mark_point().encode(
        y=Y(y_axis,
            axis=Axis(format='.1',
                      title=y_axis,
                      ),
            scale=Scale(type='log'),
            ),
        x=X('average_degree',
            ),
        color='dataset',
    )
    save(chart=chart,
         df=dfab,
         plotname='%s_%s' % (name, y_axis),
         formats=['html', 'svg', 'png', 'pdf', 'tablehtml'],
         sortby=['dataset', 'do_a', 'do_b', 'num_edges',
                 'num_vertices', 'average_degree'],
         columns=['dataset', 'do_a', 'do_b', 'm_teps', 'num_edges',
                  'num_vertices', 'average_degree'],
         )
