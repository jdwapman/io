#!/usr/bin/env python

from altair import *
import pandas  # http://pandas.pydata.org
import numpy
import datetime

from fileops import save, wrapChartInMd
from filters import *
from logic import *

from scipy.stats import gmean

name = 'groute'

# begin user settings for this script
roots = ['../gunrock-output/Groute_Comparison/', '../Groute-output/']
# oddly this order is important since the first arg has more info than
# the second, so mashing the second into the first preserves more columns
fnFilterInputFiles = [
    fileEndsWithJSON,
]
fnPreprocessDF = [
]
fnFilterDFRows = [
]
fnPostprocessDF = [
    equateK40,
    computeMTEPSFromEdgesAndElapsed,
    keepFastest(columns=['algorithm', 'dataset', 'engine', 'num_gpus', 'gpuinfo.name'],
                sortBy='m_teps'),
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
                     'elapsed',
                     'm_teps',
                     'num_gpus',
                     'gpuinfo.name',
                     'engine',
                     'time',
                     'details']
# would prefer a cleanup call https://github.com/altair-viz/altair/issues/183
# without this, output is gigantic
df = (keepTheseColumnsOnly(columnsOfInterest))(df)
# now make the graph

chart = Chart(df).mark_point().encode(
    x=X('num_gpus:N',
        axis=Axis(
            title='Number of GPUs',
        ),
        ),
    column=Column('dataset:N',
                  axis=Axis(
                      title='Dataset',
                      orient='top',
                  )
                  ),
    row=Row('algorithm:N',
            axis=Axis(
                title='Primitive',
            )
            ),
    y=Y('m_teps',
        axis=Axis(
            title='MTEPS',
        ),
        scale=Scale(type='log'),
        ),
    shape=Shape('engine:N',
                legend=Legend(
                    title='Engine',
                ),
                ),
    color=Color('[gpuinfo.name]:N',
                legend=Legend(
                    title='GPU',
                ),
                ),
)
print chart.to_dict(data=False)
save(df=df,
     plotname=name,
     formats=['tablemd', 'tablehtml'],
     sortby=['algorithm', 'dataset', 'num_gpus', 'engine', 'm_teps'],
     columns=columnsOfInterest,
     )

save(chart=chart,
     df=df,
     plotname=name,
     formats=['json', 'html', 'svg', 'png', 'pdf'],
     )

save(plotname=name,
     formats=['md'],
     mdtext=("""
# Groute

We noted with interest the PPoPP 2017 paper _Groute: An Asynchronous Multi-GPU Programming Model for Irregular Computations_ by Tal Ben-Nun, Michael Sutton, Sreepathi Pai, and Keshav Pingali ([DOI](http://dx.doi.org/10.1145/3018743.3018756)). This is really nice work, and we particularly admire their use of asynchronous execution. We expect (and show in the results below) that for high-diameter networks like road networks, their approach is particularly beneficial.

In their paper, the Groute authors compared against Gunrock 0.31, which was current at the time of paper submission (but had been updated to 0.4 by the time of camera-ready submission). We thus ran the Groute artifact ([link](https://github.com/groute/ppopp17-artifact)) locally to compare against current Gunrock results.

The Groute authors noted issues with Gunrock's accuracy on PageRank on multiple GPUs ("the evaluated version of Gunrock's multi-GPU PageRank produced incorrect results"). The Groute authors raised this issue on 17 September 2016 in a [github issue](https://github.com/gunrock/gunrock/issues/191), to which we responded on 3 October 2016. We noted in our response that the issue is not an error but instead not using the proper command-line options for the desired comparison.

""" +
             wrapChartInMd(chart, anchor='%s' % name) + """
[Source data](md_stats_%s_table_html.html), with links to the output JSON for each run<br/>
""" % name
             ))
