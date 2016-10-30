#!/usr/bin/env python

from altair import *
import pandas  # http://pandas.pydata.org
import numpy
import json    # built-in
import os      # built-in
import copy    # built-in
from subprocess import Popen, PIPE, STDOUT, check_output, CalledProcessError

from fileops import savefile


root = '../gunrock-output/new/'

for prim in ['BC', 'PageRank', 'CC', 'SSSP']:

    json_files = [os.path.join(subdir, f) for (subdir, dirs, files)
                  in os.walk(root) for f in files]

    def filterFiles(f):
        return (os.path.isfile(f) and
                (os.path.splitext(f)[1] == ".json") and
                os.path.basename(f).startswith(prim) and
                not os.path.basename(f).startswith("_"))

    json_files = filter(filterFiles, json_files)

    data_unfiltered = [json.load(open(jf)) for jf in json_files]
    df = pandas.DataFrame(data_unfiltered)
    # All prim-specific data is now stored in the pandas DataFrame "df".

    # Unfortunately, some of the runs in the repo have no dataset. Filter them
    # out.
    df = df[df['dataset'] != ""]

    # filter out 64bit-SizeT
    df = df[~df['command_line'].str.contains('64bit-SizeT')]
    # filter out undirected=false
    df = df[df['undirected']]
    # filter out mark_predecessors=true
    df = df[~df['mark_predecessors']]

    chart = Chart(df).mark_bar().encode(
        x=X('traversal_mode:N',
            axis=False,
            ),
        column=Column('dataset',
                      axis=Axis(
                          title='Dataset',
                          orient='bottom',
                      )
                      ),
        y=Y('m_teps',
            axis=Axis(
                title='MTEPS',
            ),
            # scale=Scale(type='log'),
            ),
        color=Color('traversal_mode:N',
                    legend=Legend(title='Traversal Mode'),
                    ),
    )
    print chart.to_dict(data=False)
    savefile(chart, name='%s_trav_chart' % prim, fileformat='html')
    savefile(chart, name='%s_trav_chart' % prim, fileformat='svg')
    savefile(chart, name='%s_trav_chart' % prim, fileformat='png')
