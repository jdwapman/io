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
    equateNVIDIAGPUs,
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

datasets = [x.encode('ascii', 'ignore') for x in df.dataset.unique()]
gpus = [x.encode('ascii', 'ignore') for x in df['gpuinfo.name'].unique()]
chart = {}

chart['all'] = Chart(df).mark_point().encode(
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
print chart['all'].to_dict(data=False)
save(df=df,
     plotname=name,
     formats=['tablemd', 'tablehtml'],
     sortby=['algorithm', 'dataset', 'num_gpus', 'engine', 'm_teps'],
     columns=columnsOfInterest,
     )

save(chart=chart['all'],
     df=df,
     plotname=name,
     formats=['json', 'html', 'svg', 'png', 'pdf'],
     )

for dataset in datasets:
    chart[dataset] = Chart(df).mark_point().encode(
        x=X('num_gpus:N',
            axis=Axis(
                title='Number of GPUs',
            ),
            ),
        column=Column('[gpuinfo.name]:N',
                      axis=Axis(
                          title='GPU',
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
        color=Color('engine:N',
                    legend=Legend(
                        title='Engine',
                    ),
                    ),
    ).transform_data(
        filter=(expr.df.dataset == dataset)
    )
    print chart[dataset].to_dict(data=False)
    save(chart=chart[dataset],
         df=df,
         plotname=name + '_' + dataset,
         formats=['json', 'html', 'svg', 'png', 'pdf'],
         )

for gpu in gpus:
    chart[gpu] = Chart(df).mark_point().encode(
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
        color=Color('engine:N',
                    legend=Legend(
                        title='Engine',
                    ),
                    ),
    ).transform_data(
        # filter=(expr.df['gpuinfo.name'] == gpu)
        filter="datum['gpuinfo.name'] == \"%s\"" % gpu,
    )
    print chart[gpu].to_dict(data=False)
    save(chart=chart[gpu],
         df=df,
         plotname=name + '_' + gpu,
         formats=['json', 'html', 'svg', 'png', 'pdf', 'md'],
         mdtext="# %s" % gpu + wrapChartInMd(chart[gpu])
         )

save(plotname=name,
     formats=['md'],
     mdtext=("""# Groute

We noted with interest the PPoPP 2017 paper _Groute: An Asynchronous Multi-GPU Programming Model for Irregular Computations_ by Tal Ben-Nun, Michael Sutton, Sreepathi Pai, and Keshav Pingali ([DOI](http://dx.doi.org/10.1145/3018743.3018756)). This is really nice work, and we particularly admire their use of asynchronous execution. We expect (and show in the results below) that for high-diameter networks like road networks (e.g., `europe_osm`, `road_usa`), their approach is particularly beneficial. Gunrock's design is more targeted towards scale-free graphs (e.g., `kron_g500`, `soc-LiveJournal1`, `twitter-mpi`). In general, Groute generally performs better than Gunrock on high-diameter, road-network-ish graphs, and also has an excellent connected-components implementation.

In their paper, the Groute authors compared against Gunrock 0.3.1, which was current at the time of paper submission (but had been updated to 0.4 by the time of camera-ready submission). We thus ran the Groute artifact ([link](https://github.com/groute/ppopp17-artifact)) locally to compare against current Gunrock results. The graphed results below are against Gunrock 0.4.

In their paper, the Groute authors noted issues with Gunrock's accuracy on PageRank on multiple GPUs ("the evaluated version of Gunrock's multi-GPU PageRank produced incorrect results"). The Groute authors raised this issue on 17 September 2016 in a [github issue](https://github.com/gunrock/gunrock/issues/191), to which we responded on 3 October 2016. We noted in our response at that time that the issue is not an error but instead not using the proper command-line options for the desired comparison.

We made the following notes when reproducing the results from the Groute paper using the same Gunrock version as in that paper (0.3.1), but on our server equipped with Tesla K40c GPUs (not Tesla M60s, as in the paper). The primary discrepancy is that the Groute comparisons in the paper do not incorporate Gunrock's optimizations, such as direction-optimal BFS traversal.

- We could not verify the Table 3 results for BFS + soc-LiveJournal1 + Gunrock v0.3.1 (on our Nov 9, 2015 v0.3.1 release). The table reports a 99.11 ms runtime. With 2 GPUs (`--device=0,1`), we measured 40.31 ms; with `--device=0,1 --src=randomize2 --iteration-num=32 --idempotence`, we measured 29.48 ms. (We note Gunrock 0.4 has similar performance.) When we enable Gunrock's direction-optimized BFS (`--direction-optimized`), on v0.3.1, we measure ~15 ms. We don't believe that running on a M60 GPU vs. the K40c GPU would give such a large discrepancy.

- We could not verify the Table 3 results for BFS + kron21.sym (the kron-g500-n21 dataset from the 10th DIMACS Implementation Challenge). On Gunrock 0.3.1 with `--dev=0,1,2`, we measured 72.80 ms on 3x K40c; Table 3 reports 156.68 ms.  With `--device=0,1,2 --idempotence --src=randomize2 --iteration-num=32`, we measure 17.94 ms. When we enable DOBFS, we measure 3.86 ms. Again we don't believe that running on a M60 GPU vs. the K40c GPU would give such a large discrepancy.

- We believe that properly setting command-line parameters will allow several data sets to run to completion (for both Gunrock and for B40C) where the Groute paper instead reported errors or were un-runnable.
    - For example, `-src=randomize` lets B40C run the kron21 dataset properly; without a randomized source, B40C (unsuccessfully) tries to find a source that reaches more than 5 edges. Here, `-src=randomize` results in a timing of 5.49 ms, and `--src=randomize --num-gpus=4 --undirected -i=32` gives 17.49 ms for the average runtime.
    - For Gunrock + twitter, `-queue-sizing=0.1 -device=0,1,2,3` allows a successful run (735.13 ms); `market /data/gunrock_dataset/huge/twitter-mpi/twitter-mpi.mtx --device=0,1,2,3 --queue-sizing=0.1 --idempotence --src=randomize2 -iteration-num=32` measures 342.21 ms.
    - For Gunrock + connected components, we found Gunrock ran properly on kron21 even on a single GPU with no command-line parameters, and should be able to run on more GPUs as well (we successfully tested up to 4xK40c).

We note that Groute's circular work list overflowed on Tesla K40c for some PageRank runs with the twitter and kron datasets (`circular worklist has overflowed, please allocate more memory`). We haven't yet worked out the right command-line switch to allocate more memory for this case, although we're sure this is a simple fix.

The following plot has multiple GPUs on one plot. We have broken them out by GPU on individual pages here:
[ [Tesla P100](md_stats_groute__tesla__p100-_p_c_i_e-16_g_b.html)
| [Tesla K40c](md_stats_groute__tesla__k40c.html)
| [Tesla K40m](md_stats_groute__tesla__k40m.html)
| [Tesla K80](md_stats_groute__tesla__k80.html)
| [Tesla M60](md_stats_groute__tesla__m60.html)
]

""" +
             wrapChartInMd(chart['all'], anchor='%s' % name) + """
[Source data](md_stats_%s_table_html.html), with links to the output JSON for each run<br/>
""" % name
             ))
