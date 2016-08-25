#!/usr/bin/env python

from altair import *
import pandas  # http://pandas.pydata.org
import numpy
import json    # built-in
import os      # built-in
import copy    # built-in
from subprocess import Popen, PIPE, STDOUT, check_output, CalledProcessError

# load data as a pandas DataFrame
cars = load_dataset('cars')

chart = Chart(cars).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
)

print chart.to_dict(data=False)
open('example.html', 'w').write(chart.to_html(local_file=False))

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
open('bfs_chart.html', 'w').write(bfs_chart.to_html(local_file=False))

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
open('bfs_param_chart.html', 'w').write(
    bfs_param_chart.to_html(local_file=False))

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
open('bfs_param_t_chart.html', 'w').write(
    bfs_param_t_chart.to_html(local_file=False))


def buildPlot(input_json, verbose=False):
    """builds the actual visual plot. """
    # call vg2png to turn JSON it into png
    try:
        p = check_output(['vg2svg', input_json, ''])
        # if(verbose): print("Created " + output_svg_file)
        return p
    except CalledProcessError as e:
        print e.output


def pipe_vl2vg(json_in):
    """Pipes the vega-lite json through vl2vg to generate the vega json output

        Returns: vega-spec json string"""
    p = Popen(["vl2vg"], stdout=PIPE, stdin=PIPE, shell=True)
    vg = p.communicate(input=json.dumps(json_in))[0]
    # f = open('log.json','w')
    # f.write(json.dumps(json_in))
    # f.close()
    return vg


def write2tempfile(input):
    """a helper function that creates a temp file and stores the input passed to it in the file """
    import tempfile
    temp = tempfile.NamedTemporaryFile(delete=False)
    temp.write(input)
    temp.close()
    return temp

# builder = vega2pic.SVGBuilder(temp_file.name)
tmp = write2tempfile(pipe_vl2vg(bfs_param_t_chart.to_dict()))
svg = buildPlot(tmp.name)
file = open('bfs_param_t_chart.svg', 'w')
file.write(svg)
file.close()
