#!/usr/bin/env python

from altair import *
import pandas  # http://pandas.pydata.org
from pandas.io.json import json_normalize
import numpy
import re      # built-in
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


def gunrockVersionGPU(df):
    df['gunrock_version_gpu'] = df[
        'gunrock_version'] + " / " + df['gpuinfo.name']
    return df


def addJSONDetailsLink(df):
    df['details'] = pandas.Series(json_input_files).values
    df['details'] = df['details'].apply(lambda s: re.sub(
        r'.*gunrock-output',
        '<a href="https://github.com/gunrock/io/tree/master/gunrock-output',
        s) + '">JSON output</a>')
    return df


def selectAnyOfTheseDates(dates):
    return lambda df: df[df['time'].isin(dates)]


def deleteZeroMTEPS(df):
    return df[df['m_teps'] != 0]


# user settings for this script
root = '../gunrock-output/'
fnFilterInputFiles = [fileEndsWithJSON,
                      ]
fnPreprocessDF = [convertCtimeStringToDatetime,
                  DOBFStoBFS,
                  equateRGG,
                  normalizePRMTEPS,
                  addJSONDetailsLink,
                  gunrockVersionGPU,
                  ]
fnFilterDFRows = [selectAnyOfTheseDates([datetime.date(2016, 11, 17),
                                         datetime.date(2016, 11, 18)]),
                  # 2016/11/17 is gunrock-output/topc/
                  deleteZeroMTEPS,
                  ]
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
# next call used to be df = pandas.DataFrame(data_unfiltered)
# instead, json_normalize flattens nested dicts
df = json_normalize(data_unfiltered)
# http://stackoverflow.com/questions/26666919/python-pandas-add-column-in-dataframe-from-list

for fn in fnPreprocessDF:       # alter entries / compute new entries
    df = fn(df)
for fn in fnFilterDFRows:       # remove rows
    df = fn(df)

# end actual program logic

# now make the graph

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
    shape=Shape('gunrock_version_gpu:N',
                legend=Legend(
                    title='Gunrock Version / GPU',
                ),
                ),
)
print chart.to_dict(data=False)
plotname = 'topc'
for fileformat in ['html', 'svg', 'png']:
    savefile(chart, name=plotname, fileformat=fileformat)

tablefile = plotname + "_table.html"
outfile = open(tablefile, 'w')
# http://stackoverflow.com/questions/26277757/pandas-to-html-truncates-string-contents
pandas.set_option('display.max_colwidth', -1)
df.sort_values(['algorithm',
                'dataset',
                'gunrock_version']).to_html(buf=outfile,
                                            columns=['algorithm',
                                                     'dataset',
                                                     'm_teps',
                                                     'gunrock_version',
                                                     'gpuinfo.name',
                                                     'details'],
                                            index=False,
                                            escape=False)
outfile.close()
