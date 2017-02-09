#!/usr/bin/env python

from altair import *
import pandas  # http://pandas.pydata.org
import numpy
import datetime

from fileops import save, wrapChartInMd
from filters import *
from logic import *

from scipy.stats import gmean

name = 'mgpu_scalability'


def labelScalability(df):
    d = {
        "rmat_1048576_e256": ["weak edge"],
        "rmat_1572864_e256": ["weak edge"],
        "rmat_2097152_e256": ["weak edge"],
        "rmat_2621440_e256": ["weak edge"],
        "rmat_3145728_e256": ["weak edge"],
        "rmat_3670016_e256": ["weak edge"],
        "rmat_4194304_e255": ["weak edge"],
        "rmat_524288_e256": ["weak edge"],
        "rmat_n19_e1024": ["weak vertex"],
        "rmat_n19_e1280": ["weak vertex"],
        "rmat_n19_e1536": ["weak vertex"],
        "rmat_n19_e1792": ["weak vertex"],
        "rmat_n19_e2047": ["weak vertex"],
        "rmat_n19_e256": ["weak edge", "weak vertex"],
        "rmat_n19_e512": ["weak vertex"],
        "rmat_n19_e768": ["weak vertex"],
        "rmat_n24_e32": ["strong"],
    }
    for s in ['weak edge', 'weak vertex', 'strong']:
        df[s] = df.apply(lambda row: s in d[row['dataset']], axis=1)
        m = df[s] == True
        df.loc[m, 'scalability'] = s
    return df


def scalabilityGPU(df):
    df['scalability_gpu'] = df['scalability'] + " / " + df['gpuinfo.name']
    return df

# begin user settings for this script
roots = ['../gunrock-output/ipdps17/eval_fig5']
fnFilterInputFiles = [
    fileEndsWithJSON,
]
fnPreprocessDF = [
]
fnFilterDFRows = [
]
fnPostprocessDF = [
    BFStoDOBFS,
    labelScalability,
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
                     'idempotent',
                     'num_gpus',
                     'scalability',
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

chart = {}
for algorithm in ['BFS', 'DOBFS', 'PageRank']:
    dfplot = df[df['algorithm'] == algorithm]
    if (algorithm == 'DOBFS'):
        dfplot = dfplot[dfplot['idempotent'] == False]
    chart[algorithm] = Chart(dfplot).mark_point().encode(
        x=X('num_gpus:N',
            axis=Axis(
                title='Number of GPUs',
            ),
            ),
        y=Y('m_teps',
            axis=Axis(
                title='MTEPS',
            ),
            # scale=Scale(type='log'),
            ),
        color=Color('[gpuinfo.name]:N',
                    legend=Legend(
                        title='GPU',
                    ),
                    ),
        shape=Shape('scalability:N',
                    legend=Legend(
                        title='Scalability Type',
                    ),
                    ),
    ).transform_data()
    # filter=((expr.df.algorithm != 'DOBFS') or
    # (expr.df.idempotent == False))
    # @TODO https://github.com/altair-viz/altair/issues/298
    print chart[algorithm].to_dict(data=False)
    save(df=dfplot,
         plotname=name + '_' + algorithm,
         formats=['tablemd', 'tablehtml'],
         sortby=['algorithm', 'scalability', 'dataset',
                 'gpuinfo.name', 'num_gpus', 'idempotent'],
         columns=columnsOfInterest,
         )

    save(chart=chart[algorithm],
         df=dfplot,
         plotname=name + '_' + algorithm,
         formats=['json', 'html', 'svg', 'png', 'pdf'],
         )

save(plotname=name,
     formats=['md'],
     mdtext=("""
# Scalability on multiple GPUs

Scalability of DOBFS, BFS, and PR. {Strong, weak edge, weak vertex} scaling use rmat graphs with {2<sup>24</sup>, 2<sup>19</sup>, 2<sup>19</sup>&nbsp;&times;&nbsp;|GPUs|} vertices and edge factor {32, 256&nbsp;&times;&nbsp;|GPUs|, 256} respectively. DOBFS runs have idempotence disabled, though results with idempotence enabled have similar runtimes.

While providing both weak-vertex and -edge scaling, DOBFS doesn't have good strong scaling, because its computation and communication are both roughly on the order of O(|V<sub>i</sub>|). This effect is more obvious on P100, as computation is faster but inter-GPU bandwidth stays mostly the same. BFS and PR achieve almost linear weak and strong scaling from 1 to 8 GPUs.

""" +
             wrapChartInMd(chart['DOBFS'], anchor='%s_DOBFS' % name) +
             wrapChartInMd(chart['BFS'], anchor='%s_BFS' % name) +
             wrapChartInMd(chart['PageRank'], anchor='%s_PageRank' % name) + """
[[%s source data](md_stats_%s_%s_table_html.html)] [[%s source data](md_stats_%s_%s_table_html.html)] [[%s source data](md_stats_%s_%s_table_html.html)], with links to the output JSON for each run<br/>
""" % ('DOBFS', name, 'DOBFS', 'BFS', name, 'BFS', 'PageRank', name, 'PageRank')
     ))
