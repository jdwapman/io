#!/usr/bin/env python

from altair import *
import pandas  # http://pandas.pydata.org
import numpy
import datetime

from fileops import save, wrapChartInMd
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
chart = {}
datasets = ['hollywood-2009', 'indochina-2004', 'rmat_n22_e64',
            'rmat_n23_e32', 'rmat_n24_e16', 'road_usa',
            'soc-LiveJournal1', 'soc-orkut', ]
columnsOfInterest = ['algorithm',
                     'dataset',
                     'do_a',
                     'do_b',
                     'm_teps',
                     'edges_visited',
                     'elapsed',
                     'engine',
                     'gunrock_version',
                     'gpuinfo.name',
                     'num_vertices',
                     'num_edges',
                     'details']
# would prefer a cleanup call https://github.com/altair-viz/altair/issues/183
# without this, output is gigantic
df = (keepTheseColumnsOnly(columnsOfInterest))(df)

for dataset in datasets:
    # This copy avoids a view-vs-copy warning:
    # http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
    # because the recomputeMTEPSFromMax changes the dataframe, and
    # because dfd is a view, those changes won't propagate back to the
    # original df. If we wanted the changes to propagate back to the
    # original df, we should probably change recomputeMTEPSFromMax to
    # operate on the entire dataframe (rather than this subset) and
    # use groupBy on the dataset to compute max per dataset.
    dfd = df[df['dataset'] == dataset].copy()

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
    chart[dataset] = Chart(dfd).mark_text(applyColorToBackground=True).encode(
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
    print chart[dataset].to_dict(data=False)
    # foo = open('%s_%s.json' % (name, dataset), 'w')
    # foo.write(df.to_json())
    # foo.close()

    save(chart=chart[dataset],
         df=dfd,
         plotname='%s_%s' % (name, dataset),
         formats=['html', 'svg', 'png', 'pdf', 'tablehtml', 'tablemd'],
         sortby=['algorithm',
                 'dataset',
                 'engine',
                 'gunrock_version'],
         columns=[item for item in columnsOfInterest if item not in [
             'num_vertices', 'num_edges']]
         )
dfab = dfab[['dataset', 'do_a', 'do_b', 'num_edges', 'num_vertices', 'm_teps']]
dfab['average_degree'] = dfab['num_edges'] / dfab['num_vertices']
print dfab

for y_axis in ['do_a', 'do_b']:
    chart[y_axis] = Chart(dfab).mark_point().encode(
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
    save(chart=chart[y_axis],
         df=dfab,
         plotname='%s_%s' % (name, y_axis),
         formats=['html', 'svg', 'png', 'pdf', 'tablehtml', 'tablemd'],
         sortby=['dataset', 'do_a', 'do_b', 'num_edges',
                 'num_vertices', 'average_degree'],
         columns=['dataset', 'do_a', 'do_b', 'm_teps', 'num_edges',
                  'num_vertices', 'average_degree'],
         )

mdtext = """
# Setting Parameters for Direction-Optimized BFS

Beamer et al.'s direction-optimized breadth first search defined two tuning parameters, alpha and beta. Alpha indicates where to switch from top-down to bottom-up; beta indicates where to switch back to top-down at the end. These parameters are architecture- and dataset-dependent.

S. Beamer, K. Asanovic, and D. Patterson, _Direction-optimizing breadth-first search_, SC '12: Proceedings of the International Conference on High Performance Computing, Networking, Storage and Analysis, 2012. [DOI](http://dx.doi.org/10.1109/SC.2012.50)

In Beamer et al.'s implementation (on multi-socket CPU servers), alpha and beta were relatively insensitive to the dataset. Gunrock's alpha and beta (which we call `do_a` and `do_b`) are considerably more dependent on the dataset. The following experiments show performance, measured in MTEPS, when we sweep `do_a` and `do_b` on 8 datasets: hollywood-2009, indochina-2004, rmat_n22_e64, rmat_n23_e32, rmat_n24_e16, road_usa, soc-LiveJournal1, and soc-orkut.

Note that while the "islands" of high performance (the dark regions) for each dataset are relatively large, they are in different regions of `do_a` and `do_b` for different datasets. It appears to be an interesting research problem to automatically set these two tuning parameters in Gunrock, with possible approaches to pursue either a static decision (given static characteristics of a graph like vertex and edge count) or a dynamic decision (as the computation is running).
"""

for dataset in datasets:
    mdtext += wrapChartInMd(chart[dataset], anchor=dataset)
    mdtext += "\n[%s source data](md_stats_%s_%s_table_html.html)\n" % (
        dataset, name, dataset)

save(plotname=name,
     formats=['md'],
     mdtext=mdtext
     )
