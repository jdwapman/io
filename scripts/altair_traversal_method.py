#!/usr/bin/env python

from altair import *
import pandas  # http://pandas.pydata.org
import numpy
import json    # built-in
import os      # built-in
import copy    # built-in
import datetime
from subprocess import Popen, PIPE, STDOUT, check_output, CalledProcessError

from fileops import savefile


root = '../gunrock-output/'

for prim in ['BFS', 'BC', 'PageRank', 'CC', 'SSSP']:

    all_json_files = [os.path.join(subdir, f) for (subdir, dirs, files)
                      in os.walk(root) for f in files]

    def filterFiles(f):
        return (os.path.isfile(f) and
                (os.path.splitext(f)[1] == ".json") and
                os.path.basename(f).startswith(prim) and
                not os.path.basename(f).startswith("_"))

    all_json_files = filter(filterFiles, all_json_files)

    # Filter only modified in Oct 2016
    def filterOct16(f):
        mtime = datetime.datetime.fromtimestamp(os.path.getmtime(f)).date()
        return ((mtime > datetime.date(2016, 9, 30)) and
                (mtime < datetime.date(2016, 11, 1)))

    # Filter only modified on 7 Nov 2016
    def filter7Nov16(f):
        mtime = datetime.datetime.fromtimestamp(os.path.getmtime(f)).date()
        return mtime == datetime.date(2016, 11, 7)

    json_files_oct16 = filter(filterOct16, all_json_files)
    json_files_7nov16 = filter(filter7Nov16, all_json_files)

    data_unfiltered = [json.load(open(jf)) for jf in json_files_oct16]
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
                    legend=Legend(title='%s / Traversal Mode' % prim),
                    ),
    )
    print chart.to_dict(data=False)
    plotname = '%s_trav_chart'
    for fileformat in ['html', 'svg', 'png']:
        savefile(chart, name=plotname % prim, fileformat=fileformat)

    # Average node degree chart
    files = [(json_files_oct16, 'Real-World')]
    if (prim == 'BFS'):
        files.append((json_files_7nov16, 'RGG+RMAT'))
    for file in files:
        data_unfiltered = [json.load(open(jf)) for jf in file[0]]
        df = pandas.DataFrame(data_unfiltered)

        # "graph_type": "grmat",
        # "graph_type": "rgg",

        df['avg_node_degree'] = df['edges_visited'] / df['nodes_visited']
        chart = Chart(df).mark_point().encode(
            x=X('avg_node_degree',
                axis=Axis(
                    title='Average node degree',
                ),
                ),
            y=Y('m_teps',
                axis=Axis(
                    title='MTEPS',
                ),
                # scale=Scale(type='log'),
                ),
            color=Color('traversal_mode:N',
                        legend=Legend(
                            title='%s / %s / Traversal Mode' % (file[1], prim)),
                        ),
        )
        # also kludgey: why do this twice?
        if file[1] == 'RGG+RMAT':
            # this is kludgey
            # http://stackoverflow.com/questions/19913659/pandas-conditional-creation-of-a-series-dataframe-column
            df['RGG_vs_RMAT'] = ['RMAT' if gt ==
                                 'grmat' else 'RGG' for gt in df['graph_type']]
            chart = Chart(df).mark_text().encode(
                x=X('avg_node_degree',
                    axis=Axis(
                        title='Average node degree',
                    ),
                    ),
                y=Y('m_teps',
                    axis=Axis(
                        title='MTEPS',
                    ),
                    # scale=Scale(type='log'),
                    ),
                color=Color('traversal_mode:N',
                            legend=Legend(
                                title='%s / %s / Traversal Mode' % (file[1], prim)),
                            ),
                text='RGG_vs_RMAT:N',
            )
        plotname = '%s_%s_avg_node_degree'
        for fileformat in ['html', 'svg', 'png']:
            savefile(chart,
                     name=plotname % (file[1], prim),
                     fileformat=fileformat)
