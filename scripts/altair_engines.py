#!/usr/bin/env python

from altair import *
import pandas  # http://pandas.pydata.org
from pandas.io.json import json_normalize
import numpy
import json    # built-in
import os      # built-in
import copy    # built-in
import datetime
from subprocess import Popen, PIPE, STDOUT, check_output, CalledProcessError

from fileops import savefile
from filters import *

name = 'engines_topc'

# begin user settings for this script
roots = ['../gunrock-output', '../CuSha-output',
         '../Galois-output', '../Ligra-output', '../MapGraph-output']
fnFilterInputFiles = [
    fileEndsWithJSON,
]
fnPreprocessDF = [
    convertCtimeStringToDatetime,
    DOBFStoBFS,
    BFSCCtoCC,
    equateRGG,
    normalizePRMTEPS,
    addJSONDetailsLink,
    gunrockVersionGPU,
]
fnFilterDFRows = [
    selectAnyOfTheseDates([datetime.date(2016, 11, 17),
                           datetime.date(2016, 11, 18),
                           datetime.date(2016, 11, 20),
                           datetime.date(2016, 11, 29)]),
    # 2016/11/17 is gunrock-output/topc/
    # 2016/11/20 is {CuSha,Galois}-output/topc/
    # 2016/11/26 is Ligra-output/topc/
    computeOtherMTEPSFromGunrock,
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

for (data, caption) in [('m_teps', 'MTEPS'), ('elapsed', 'Elapsed time (ms)')]:

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
        y=Y(data,
            axis=Axis(
                title=caption,
            ),
            scale=Scale(type='log'),
            ),
        color=Color('sub_algorithm:N',
                    legend=Legend(
                        title='Algorithmic variant',
                    ),
                    ),
        shape=Shape('engine',
                    legend=Legend(
                        title='Engine',
                    ),
                    ),
    )
    print chart.to_dict(data=False)
    plotname = '%s_%s' % (name, data)
    for fileformat in ['html', 'svg', 'png']:
        savefile(chart, name=plotname, fileformat=fileformat)

tablefile = name + "_table.html"
outfile = open(tablefile, 'w')
# http://stackoverflow.com/questions/26277757/pandas-to-html-truncates-string-contents
pandas.set_option('display.max_colwidth', -1)
df.sort_values(['algorithm',
                'sub_algorithm',
                'dataset',
                'engine',
                'gunrock_version']).to_html(buf=outfile,
                                            columns=['algorithm',
                                                     'sub_algorithm',
                                                     'dataset',
                                                     'engine',
                                                     'm_teps',
                                                     'edges_visited',
                                                     'elapsed',
                                                     'gunrock_version',
                                                     'gpuinfo.name',
                                                     'details'],
                                            index=False,
                                            escape=False)
outfile.close()
