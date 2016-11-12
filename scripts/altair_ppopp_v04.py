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

all_json_files_1011nov16 = []

for prim in ['BFS', 'BC', 'PageRank', 'CC', 'SSSP']:

    all_json_files = [os.path.join(subdir, f) for (subdir, dirs, files)
                      in os.walk(root) for f in files]

    def filterFiles(f):
        return (os.path.isfile(f) and
                (os.path.splitext(f)[1] == ".json") and
                (os.path.basename(f).startswith(prim) or
                 os.path.basename(f).startswith('DO' + prim)) and
                not os.path.basename(f).startswith("_"))

    all_json_files = filter(filterFiles, all_json_files)

    # Filter only modified on 10 Nov 2016 (this is the ppopp re-run, v0.4)
    def filter10Nov16(f):
        mtime = datetime.datetime.fromtimestamp(os.path.getmtime(f)).date()
        return mtime == datetime.date(2016, 11, 10)

    json_files_10nov16 = filter(filter10Nov16, all_json_files)
    all_json_files_1011nov16.extend(json_files_10nov16)

    # Filter only modified on 11 Nov 2016 (this is the ppopp re-run, v0.3)
    def filter11Nov16(f):
        mtime = datetime.datetime.fromtimestamp(os.path.getmtime(f)).date()
        return mtime == datetime.date(2016, 11, 12)  # total hack

    json_files_11nov16 = filter(filter11Nov16, all_json_files)
    all_json_files_1011nov16.extend(json_files_11nov16)

    data_unfiltered = [json.load(open(jf)) for jf in json_files_10nov16]
    df = pandas.DataFrame(data_unfiltered)
    # All prim-specific data is now stored in the pandas DataFrame "df".

    is_PR = False
    if prim == 'PageRank':
        # normalize per iteration
        is_PR = True
        df['m_teps_normalized'] = df['m_teps'] / df['search_depth']

    chart = Chart(df).mark_bar().encode(
        x=X('dataset:N',
            axis=Axis(
                title='Dataset',
            )
            ),
        y=Y('m_teps' if not is_PR else 'm_teps_normalized',
            axis=Axis(
                title='MTEPS' if not is_PR else 'MTEPS (normalized)',
            ),
            ),
    )
    print chart.to_dict(data=False)
    plotname = '%s_perf'
    for fileformat in ['html', 'svg', 'png']:
        savefile(chart, name=plotname % prim, fileformat=fileformat)

data_unfiltered = [json.load(open(jf)) for jf in all_json_files_1011nov16]
df = pandas.DataFrame(data_unfiltered)
# All prim-specific data is now stored in the pandas DataFrame "df".
df.loc[df.algorithm == 'DOBFS', 'algorithm'] = 'BFS'

chart = Chart(df).mark_point().encode(
    x=X('dataset:N',
        ),
    column=Column('algorithm:N',
                  axis=Axis(
                      title='Primitive',
                      orient='top',
                  )
                  ),
    y=Y('m_teps',
        axis=Axis(
            title='MTEPS',
        ),
        scale=Scale(type='log'),
        ),
    color=Color('algorithm:N',
                legend=Legend(
                    title='Primitive',
                ),
                ),
    shape=Shape('gunrock_version:N',
                legend=Legend(
                    title='Gunrock Version',
                ),
                ),
)
print chart.to_dict(data=False)
plotname = 'all_perf'
for fileformat in ['html', 'svg', 'png']:
    savefile(chart, name=plotname, fileformat=fileformat)
