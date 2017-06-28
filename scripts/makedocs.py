#!/usr/bin/env python

# Current workflow:
# - Use this file to produce "md" output, which embeds an HTML snippet in markdown.
# - Copy the md file into the master branch of gunrock/doc/stats
# - Still in master branch, run releasedoc.sh
# - Switch to gh-pages branch, push
# - Switch back to master branch

# @TODOS
# - savefile's md output needs to also take md strings so it doesn't just make a plot only
# - Support for multiple graphs on one page
# - Top-level file that records all the output md files and makes a master file that links to all of them
# - README.md in gunrock master branch needs to have a link to that master file
# - Auto-copy into master branch of gunrock/doc/stats
# - Output raw data in a table (link from the graph page?)

# @TODOS waiting for altair/vega/vega-lite features
# - When 'cleanup_data' is available in altair, do that
#   https://github.com/ellisonbg/altair/issues/183
# - When vg2{svg,png} can take a pipe in, remove tempfiles
#   https://github.com/vega/vega/issues/612

from altair import *
import pandas  # http://pandas.pydata.org
import numpy
import json    # built-in
import os      # built-in

from fileops import savefile, savefile_df

jsondir = '../gunrock-output/'

bfs_json_files = [f for f in os.listdir(jsondir)
                  if (os.path.isfile(jsondir + f) and
                      (os.path.splitext(f)[1] == ".json") and
                      (os.path.basename(f).startswith("BFS") or
                       os.path.basename(f).startswith("DOBFS")) and
                      not os.path.basename(f).startswith("_"))]
bfs_data_unfiltered = [json.load(open(jsondir + jf)) for jf in bfs_json_files]
bfs_df = pandas.DataFrame(bfs_data_unfiltered)
# All DOBFS/BFS data is now stored in the pandas DataFrame "bfs_df".

# Unfortunately, some of the runs in the repo have no dataset. Filter them out.
bfs_df = bfs_df[bfs_df['dataset'] != ""]

# Let's add a new column (attribute), conditional on existing columns.
# We'll need this to pivot later.


def setParameters(row):
    return (row['algorithm'] + ', ' +
            ('un' if row['undirected'] else '') + 'directed, ' +
            ('' if row['mark_predecessors'] else 'no ') + 'mark predecessors')
bfs_df['parameters'] = bfs_df.apply(setParameters, axis=1)


bfs_chart = Chart(bfs_df).mark_bar().encode(
    x=X('dataset',
        axis=Axis(title='Dataset')
        ),
    y=Y('m_teps',
        axis=Axis(title='MTEPS'),
        scale=Scale(type='log'),
        ),
)
print bfs_chart.to_dict(data=False)
# print bfs_chart.to_dict(data=False, cleanup_data=True)
# print bfs_chart.to_dict(data=True)
savefile(bfs_chart, name='bfs_chart', fileformat='html')
savefile(bfs_chart, name='bfs_chart', fileformat='json')
savefile(bfs_chart, name='bfs_chart', fileformat='md')
savefile_df(bfs_df, name='bfs_chart', fileformat='html')
