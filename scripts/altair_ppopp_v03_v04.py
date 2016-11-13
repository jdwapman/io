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

# possible filtering functions


def fileEndsWithJSON(f):
    return (os.path.isfile(f) and
            (os.path.splitext(f)[1] == ".json") and
            not os.path.basename(f).startswith("_"))


def convertCtimeStringToDatetime(df):
    # 'time' column is in (text) ctime format
    # datetime.strptime(jsonobj['time'], "%a %b %d %H:%M:%S %Y\n")
    # or
    # http://stackoverflow.com/questions/26763344/convert-pandas-column-to-datetime
    # normalize() resets the time to midnight (so it can be == vs. dates)
    df['time'] = df['time'].apply(
        lambda x: pandas.to_datetime(x,
                                     infer_datetime_format=True).normalize())
    return df


def DOBFStoBFS(df):
    df.loc[df.algorithm == 'DOBFS', 'algorithm'] = 'BFS'
    return df


def equateRGG(df):
    df.loc[df.dataset == 'rgg_n_2_24_s0', 'dataset'] = 'rgg_n24_0.000548'
    return df


def normalizePRMTEPS(df):
    df.loc[df.algorithm == 'PageRank', 'm_teps'] = df[
        'm_teps'] * df['search_depth']
    return df


def selectAnyOfTheseDates(dates):
    return lambda df: df[df['time'].isin(dates)]


# user settings for this script
root = '../gunrock-output/'
fnFilterInputFiles = [fileEndsWithJSON]
fnPreprocessDF = [convertCtimeStringToDatetime,
                  DOBFStoBFS, equateRGG, normalizePRMTEPS]
fnFilterDFRows = [selectAnyOfTheseDates([datetime.date(2016, 11, 10),
                                         datetime.date(2016, 11, 12)])]
# end user settings for this script

# actual program logic
# do not modify

# choose input files
json_input_files = [os.path.join(subdir, f) for (subdir, dirs, files)
                    in os.walk(root) for f in files]
# filter input files
for fn in fnFilterInputFiles:
    json_input_files = filter(fn, json_input_files)

# dump input files into dataframe
data_unfiltered = [json.load(open(jf)) for jf in json_input_files]
df = pandas.DataFrame(data_unfiltered)
for fn in fnPreprocessDF:       # alter entries / compute new entries
    df = fn(df)
for fn in fnFilterDFRows:       # remove rows
    df = fn(df)

chart = Chart(df).mark_point().encode(
    x=X('dataset:N',
        axis=Axis(
            title='Dataset',
        ),
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
plotname = 'all_0304_perf'
for fileformat in ['html', 'svg', 'png']:
    savefile(chart, name=plotname, fileformat=fileformat)
