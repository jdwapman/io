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
from filters import *

# begin user settings for this script
roots = ['../gunrock-output']
fnFilterInputFiles = [
    fileEndsWithJSON,
]
fnPreprocessDF = [
    convertCtimeStringToDatetime,
    DOBFStoBFS,
    equateRGG,
    #     equateM40,
    normalizePRMTEPS,
    addJSONDetailsLink,
    gunrockVersionGPU,
]
fnFilterDFRows = [  # selectAnyOfTheseDates([datetime.date(2016, 11, 10),
    #                        datetime.date(2016, 11, 12),
    #                        datetime.date(2016, 11, 13),
    #                        datetime.date(2016, 11, 29)]),
    selectTag('topc_arch'),  # this is datetime.date(2016, 11, 29)
    deleteZeroMTEPS,
]
fnPostprocessDF = [
]
# end user settings for this script

# actual program logic
# do not modify

# choose input files
json_input_files = []
for root in roots:
    json_input_files = json_input_files + ([os.path.join(subdir, f)
                                            for (subdir, dirs, files)
                                            in os.walk(root) for f in files])
# filter input files
for fn in fnFilterInputFiles:
    json_input_files = filter(fn, json_input_files)

# dump input files into dataframe
data_unfiltered = [json.load(open(jf)) for jf in json_input_files]
# next call used to be df = pandas.DataFrame(data_unfiltered)
# instead, json_normalize flattens nested dicts
df = json_normalize(data_unfiltered)
# http://stackoverflow.com/questions/26666919/python-pandas-add-column-in-dataframe-from-list
df['details'] = pandas.Series(json_input_files).values

for fn in fnPreprocessDF:       # alter entries / compute new entries
    df = fn(df)
for fn in fnFilterDFRows:       # remove rows
    df = fn(df)
for fn in fnPostprocessDF:      # alter entries / compute new entries
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
    color=Color('gunrock_version_gpu:N',
                ),
    shape=Shape('gunrock_version_gpu:N',
                # legend=Legend(
                #     title='Gunrock Version / GPU',
                # ),
                ),
)
print chart.to_dict(data=False)
plotname = 'all_0304_perf'
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
