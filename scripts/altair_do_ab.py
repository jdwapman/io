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

name = 'do_ab'

# begin user settings for this script
roots = ['../gunrock-output/topc-param-sweeps', ]
fnFilterInputFiles = [
    fileEndsWithJSON,
]
fnPreprocessDF = [
    addJSONDetailsLink,
]
fnFilterDFRows = [
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

for dataset in ['hollywood-2009', 'indochina-2004', 'rmat_n22_e64',
                'rmat_n23_e32', 'rmat_n24_e16', 'road_usa',
                'soc-LiveJournal1', 'soc-orkut', ]:
    dfd = df[df['dataset'] == dataset]

    # format argument:
    # https://github.com/altair-viz/altair/commit/1f6d1aaaba74b807430b8452592a3635336644cf
    # https://github.com/d3/d3-format/blob/master/README.md#format
    chart = Chart(dfd).mark_text(format='d',
                                 fontSize=5,
                                 applyColorToBackground=True).encode(
        row=Row('do_a:O',
                axis=Axis(format='.1',
                          title='do_a',
                          ),
                ),
        column=Column('do_b:O',
                      axis=Axis(format='.1',
                                title='do_b',
                                ),
                      ),
        color='m_teps',
        text='m_teps',
    ).configure_scale(
        textBandWidth=20,
        bandSize=20
    )
    print chart.to_dict(data=False)
    plotname = '%s_%s' % (name, dataset)
    for fileformat in ['html', 'svg', 'png']:
        savefile(chart, name=plotname, fileformat=fileformat)

    tablefile = plotname + '_table.html'
    outfile = open(tablefile, 'w')
    # http://stackoverflow.com/questions/26277757/pandas-to-html-truncates-string-contents
    pandas.set_option('display.max_colwidth', -1)
    dfd.sort_values(['algorithm',
                     'dataset',
                     'engine',
                     'gunrock_version']).to_html(buf=outfile,
                                                 columns=['algorithm',
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
