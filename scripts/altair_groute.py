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
     mdtext=("""# Groute performance vs. Gunrock

We noted with interest the PPoPP 2017 paper _Groute: An Asynchronous Multi-GPU Programming Model for Irregular Computations_ by Tal Ben-Nun, Michael Sutton, Sreepathi Pai, and Keshav Pingali ([DOI](http://dx.doi.org/10.1145/3018743.3018756)). This is really nice work, and we particularly admire their use of asynchronous execution. We expect (and show in the results below) that for high-diameter networks like road networks (e.g., `europe_osm`, `road_usa`), their approach is particularly beneficial. Gunrock's design is more targeted towards scale-free graphs (e.g., `kron_g500`, `soc-LiveJournal1`, `twitter-mpi`). In general, Groute generally performs better than Gunrock on high-diameter, road-network-ish graphs, and also has an excellent connected-components implementation.

In their paper, the Groute authors compared against Gunrock 0.3.1 (released 9 November 2015), which was the most recent release at the time of paper submission (but had been updated to 0.4 by the time of camera-ready submission). Between the Gunrock 0.3.1 release and the time of Groute paper submission, the Gunrock team had made significant performance improvements to Gunrock. We ran the [Groute PPoPP artifact](https://github.com/groute/ppopp17-artifact) locally to compare against two versions of Gunrock ([methodology discussion](https://github.com/gunrock/io/issues/31)). The first is the Gunrock github version of 11 July 2016 (several weeks before Groute's paper submission). The second is the Gunrock 0.4 release of 10 November 2016 (two months before Groute's camera-ready submission).

The graphs at the bottom of the page use Gunrock 0.4 and [Groute's PPoPP artifact](https://github.com/groute/ppopp17-artifact) and _only_ reflect Gunrock's (non-direction-optimized) BFS performance. In general, Gunrock's direction-optimized (DOBFS) BFS results on scale-free graphs are significantly better than its non-direction-optimized BFS results. We believe this comparison against Gunrock 0.4's BFS is the most appropriate comparison at the time of Groute's camera-ready submission (January 2017).

## Gunrock BFS on soc-LiveJournal1

The Groute paper reported Gunrock's best BFS time on soc-LiveJournal1 of 99.11 ms (Groute's Table 3) on M60 GPUs. Gunrock 0.4's BFS achieves [23.95 ms](https://github.com/gunrock/io/blob/master/gunrock-output/Groute_Comparison/BFS_soc-LiveJournal1_Thu%20Feb%20%209%20185702%202017.json) on this dataset on M60 GPUs.

For the 11 July 2016 version of Gunrock, we measure the following results on K40 and K80 GPUs (which achieve similar runtimes as M60s in our experiments):

### Non-idempotent, not direction-optimized

- K40+METIS: [avg: 40.49 ms, min: 40.00 ms, max: 51.54 ms](https://github.com/gunrock/io/blob/master/gunrock-output/20170303/bfs_k40mx2_metis_soc-LiveJournal1.txt)
- K40+random: [avg: 37.45ms, min: 37.02ms, max: 47.80ms](https://github.com/gunrock/io/blob/master/gunrock-output/20170303/bfs_k40mx2_rand_soc-LiveJournal1.txt)
- K80+METIS: [avg: 38.01 ms, min: 33.80ms, max: 61.02 ms](https://github.com/gunrock/io/blob/master/gunrock-output/20170303/bfs_k80x2_metis_soc-LiveJournal1.txt)
- K80+random: [avg: 35.43 ms, min: 31.67 ms, max: 57.12 ms](https://github.com/gunrock/io/blob/master/gunrock-output/20170303/bfs_k80x2_rand_soc-LiveJournal1.txt)

### Idempotent, not direction optimized:

- K40+METIS+idempotent: [avg: 29.53 ms, min: 27.63 ms, max: 38.99 ms](https://github.com/gunrock/io/blob/master/gunrock-output/20170303/bfs-idem_k40mx2_metis_soc-LiveJournal1.txt)
- K40+random+idempotent: [avg: 29.26 ms, min: 28.12 ms, max: 38.59 ms](https://github.com/gunrock/io/blob/master/gunrock-output/20170303/bfs-idem_k40mx2_rand_soc-LiveJournal1.txt)
- K80+METIS+idempotent+Market: [avg: 32.96 ms, min: 30.78 ms, max: 49.34 ms](https://github.com/gunrock/io/blob/master/gunrock-output/20170303/bfs-idem_k80x2_metis_soc-LiveJournal1.txt)
- K80+random+idempotent: [avg: 31.35 ms, min: 25.89 ms, max: 52.96 ms](https://github.com/gunrock/io/blob/master/gunrock-output/20170303/bfs-idem_k80x2_rand_soc-LiveJournal1.txt)

Yuechao notes that he fixed a correctness bug in idempotence mode on 4 October 2016 (https://github.com/gunrock/gunrock/commit/23490d30fb330c984ba9cb3239838d5dbe2d155d). For our testing in idempotence mode only, we measured Gunrock versions both immediately before and immediately after this bug was fixed ("the performance differences were very small"). We believe running on any July-October Gunrock build would give similar performance results.

### DOBFS

Multi-GPU DOBFS was enabled in Gunrock's BFS, and single-GPU direction-optimizing BFS was removed, as of 26 April 2016 (https://github.com/gunrock/gunrock/commit/1fbbc85ab07fcbb0d418202fcd5a77290b6df508). Gunrock's DOBFS has different behavior to Groute's (or anyone else's) BFS, which makes performance differences more challenging to explain.

- K40+DOBFS: [avg: 27.29 ms, min: 26.18ms, max: 27.84 ms](https://github.com/gunrock/io/blob/master/gunrock-output/20170303/dobfs_k40mx1_soc-LiveJournal1.txt)
- K80+DOBFS: [avg: 31.20 ms, min: 26.45 ms, max: 39.19 ms](https://github.com/gunrock/io/blob/master/gunrock-output/20170303/dobfs_k80x1_soc-LiveJournal1.txt)
- K40+DOBFS+idempotence: [avg: 23.40 ms, min: 19.95 ms, max: 24.65 ms](https://github.com/gunrock/io/blob/master/gunrock-output/20170303/dobfs-idem_k40mx1_soc-LiveJournal1.txt)
- K80+DOBFS+idempotence: [avg: 23.13 ms, min: 21.77 ms, max: 24.94 ms](https://github.com/gunrock/io/blob/master/gunrock-output/20170303/dobfs-idem_k80x1_soc-LiveJournal1.txt)

## Gunrock BFS on kron21

The Groute paper reported Gunrock's best BFS time on kron21 of 156.68 ms (Groute's Table 3) on M60 GPUs. Gunrock 0.4 achieves [19.315 ms](https://github.com/gunrock/io/blob/master/gunrock-output/Groute_Comparison/BFS_kron_g500-logn21_Thu%20Feb%20%209%20184323%202017.json) on this dataset running BFS (not DOBFS) on M60 GPUs. If we switch to DOBFS, Gunrock 0.4 achieves [4.53 ms](https://github.com/gunrock/io/blob/master/gunrock-output/20170303/dobfs-idem_k80x1_kron_g500-logn21.txt) on one K80 GPU.

For the 11 July 2016 version of Gunrock, we measure the following results on K40 and K80 GPUs (which achieve similar runtimes as M60s in our experiments):

- 3xK80+METIS: [avg: 120.67ms, min: 114.33ms, max: 216.01ms](https://github.com/gunrock/io/blob/master/gunrock-output/20170303/bfs_k80x3_metis_kron_g500-logn21.txt)
- 3xK80+random: [avg: 67.70 ms, min: 55.24 ms, max: 143.39 ms](https://github.com/gunrock/io/blob/master/gunrock-output/20170303/bfs_k80x3_rand_kron_g500-logn21.txt)
- 3xK80+idempotence+METIS+market: [avg: 35.34 ms, min: 26.75 ms, max: 78.21 ms](https://github.com/gunrock/io/blob/master/gunrock-output/20170303/bfs-idem_k80x3_metis_kron_g500-logn21.txt)
- 3xK80+idempotence+random+market: [avg: 22.70ms, min: 16.68ms, max: 56.84ms](https://github.com/gunrock/io/blob/master/gunrock-output/20170303/bfs-idem_k80x3_rand_kron_g500-logn21.txt)

## Other notes

In their paper, the Groute authors noted issues with Gunrock's accuracy on PageRank on multiple GPUs ("the evaluated version of Gunrock's multi-GPU PageRank produced incorrect results"). The Groute authors raised this issue on 17 September 2016 in a [github issue](https://github.com/gunrock/gunrock/issues/191), to which we responded on 3 October 2016. We noted in our response at that time that the issue is not an error but instead not using the proper command-line options for the desired comparison.

- We believe that properly setting command-line parameters will allow several data sets to run to completion (for both Gunrock and for B40C) where the Groute paper instead reported errors or were un-runnable.
    - For example, `-src=randomize` lets B40C run the kron21 dataset properly; without a randomized source, B40C (unsuccessfully) tries to find a source that reaches more than 5 edges. Here, `-src=randomize` results in a timing of 5.49 ms, and `--src=randomize --num-gpus=4 --undirected -i=32` gives 17.49 ms for the average runtime.
    - For Gunrock + twitter, `-queue-sizing=0.1 -device=0,1,2,3` allows a successful run (735.13 ms); `market /data/gunrock_dataset/huge/twitter-mpi/twitter-mpi.mtx --device=0,1,2,3 --queue-sizing=0.1 --idempotence --src=randomize2 -iteration-num=32` measures 342.21 ms.
    - For Gunrock + connected components, we found Gunrock ran properly on kron21 even on a single GPU with no command-line parameters, and should be able to run on more GPUs as well (we successfully tested up to 4xK40c).

We note that Groute's circular work list overflowed on Tesla K40c for some PageRank runs with the twitter and kron datasets (`circular worklist has overflowed, please allocate more memory`). We haven't yet worked out the right command-line switch to allocate more memory for this case, although we're sure this is a simple fix.

## Full performance comparison

The following plot compares Gunrock 0.4 with Groute's PPoPP artifact. It has multiple GPUs on one plot. We have broken them out by GPU on individual pages here:
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
