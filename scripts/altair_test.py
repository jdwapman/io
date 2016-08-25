#!/usr/bin/env python

from altair import *
import pandas  # http://pandas.pydata.org
import numpy
import json    # built-in
import os      # built-in
import copy    # built-in
from subprocess import Popen, PIPE, STDOUT, check_output, CalledProcessError

from fileops import savefile


# load data as a pandas DataFrame
cars = load_dataset('cars')

chart = Chart(cars).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
)

print chart.to_dict(data=False)
savefile(chart, name='example', fileformat='html')

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
savefile(bfs_chart, name='bfs_chart', fileformat='html')

bfs_param_chart = Chart(bfs_df).mark_point().encode(
    x=X('dataset',
        axis=Axis(title='Dataset')
        ),
    y=Y('m_teps',
        axis=Axis(title='MTEPS'),
        scale=Scale(type='log'),
        ),
    color='parameters',
)
print bfs_param_chart.to_dict(data=False)
savefile(bfs_param_chart, name='bfs_param_chart', fileformat='html')

bfs_param_t_chart = Chart(bfs_df).mark_point().encode(
    x=X('parameters',
        axis=Axis(title='Parameters')
        ),
    y=Y('m_teps',
        axis=Axis(title='MTEPS'),
        scale=Scale(type='log'),
        ),
    color='dataset',
)
print bfs_param_t_chart.to_dict(data=False)
savefile(bfs_param_t_chart, name='bfs_param_t_chart', fileformat='html')
savefile(bfs_param_t_chart, name='bfs_param_t_chart', fileformat='svg')
