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
    print chart[algorithm].to_dict(data=False)
    save(df=dfplot,
         plotname=name + '_' + algorithm,
         formats=['tablemd', 'tablehtml'],
         sortby=['algorithm', 'scalability', 'dataset', 'gpuinfo.name'],
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
# Speedup on multiple GPUs

We demonstrate multiple-GPU ("mGPU") speedup over 1GPU performance for six algorithms: BC, BFS, CC, DOBFS, PR and SSSP. We show both speedups on individual datasets and geometric means of runtime speedup over all datasets. These experiments are on NVIDIA Tesla K40m GPUs.

Most of the algorithms scale fairly well from 1 to 6 GPUs. The exception is DOBFS, which (unlike the other experiments) is primarily limited by communication overhead.

""" +
             wrapChartInMd(chart['BFS'], anchor='%s_BFS' % name) +
             wrapChartInMd(chart['BFS'], anchor='%s_BFS' % name) +
             wrapChartInMd(chart['BFS'], anchor='%s_BFS' % name) + """
[Source data](md_stats_%s_%s_table_html.html), with links to the output JSON for each run<br/>
""" % (name, 'all') + """
[Geomean source data](md_stats_%s_%s_table_html.html)
""" % (name, 'geomean')
     ))
