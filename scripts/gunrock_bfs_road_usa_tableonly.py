#!/usr/bin/env python3

import altair as alt
import pandas  # http://pandas.pydata.org
import numpy
import datetime

from fileops import save, getChartHTML
from filters import *
from logic import *

name = 'gunrock_results'
prims = ['bfs',  # 'sssp', 'pr', 'cc'
         ]
datasets = [  # 'soc-orkut',
    'road_usa', ]
advance_modes = ['LB', 'TWC', 'LB_CULL', ]
gpus = ['Tesla V100-DGXS-32GB', 'Quadro GV100', 'Tesla V100-PCIE-32GB']

# begin user settings for this script
roots = ['../gunrock-output/',
         ]
fnFilterInputFiles = [
    fileEndsWithJSON,
    fileNotInArchiveDir,
]
fnPreprocessDF = [
    # convertCtimeStringToDatetime,
    # normalizePRMTEPS,
    selectAnyOfThese('engine', ['Gunrock']),  # only Gunrock
    selectAnyOfThese('dataset', datasets),
    # selectAnyOfThese('gpuinfo_name', gpus),
    mergeAlgorithmIntoPrimitive,
    mergeAllUpperCasePrimitives,
    selectAnyOfThese('primitive', prims),
    mergeTraversalModeWithUnderscoreIntoAdvanceModeWithHyphen,
    renameAdvanceModeWithAHyphen,
    mergeGunrockVersionWithUnderscoreIntoHyphen,
    mergeIdempotentToIdempotence,
    mergeElapsedIntoAvgProcessTime,
    mergePostprocessTimeUnderscoreIntoHyphen,
    selectAnyOfThese('advance_mode', advance_modes),
    insertMissing('mark-pred', False),
    # tupleify('tag'),
    keepFastestAvgProcessTime(
        ['primitive', 'dataset', 'advance_mode', 'undirected', 'gunrock-version', 'gpuinfo_name']),
    addJSONDetailsLink,
    gunrockVersionGPU,
]
fnFilterDFRows = [
    # filterOut(True, '64bit-SizeT'),
    # filterOut(True, '64bit-VertexT'),
]
fnPostprocessDF = [
]
# end user settings for this script

# actual program logic
# do not modify

# choose input files
df = filesToDF(roots=roots,
               fnFilterInputFiles=fnFilterInputFiles)
for fn in fnPreprocessDF:       # alter entries / compute new entries
    df = fn(df)
for fn in fnFilterDFRows:       # remove rows
    df = fn(df)
for fn in fnPostprocessDF:      # alter entries / compute new entries
    df = fn(df)

# end actual program logic

columnsOfInterest = ['primitive',
                     'dataset',
                     'avg-mteps',
                     'avg-process-time',
                     'postprocess-time',
                     'engine',
                     'gunrock-version',
                     'gpuinfo_name',
                     'tag',
                     'num-vertices',
                     'num-edges',
                     'advance_mode',
                     'undirected',
                     'mark-pred',
                     '64bit-SizeT',
                     '64bit-ValueT',
                     '64bit-VertexT',
                     'idempotence',
                     'do-a',
                     'do-b',
                     'time',
                     'details']
# would prefer a cleanup call https://github.com/altair-viz/altair/issues/183
# without this, output is gigantic
df = (keepTheseColumnsOnly(columnsOfInterest))(df)

c = alt.Chart(df)
plotname = name

save(chart=c,
     df=df,
     plotname=plotname,
     formats=['tablehtml', 'tablemd', ],
     sortby=['dataset',
             'primitive',
             'advance_mode',
             'gpuinfo_name',
             'gunrock-version',
             'undirected',
             'mark-pred',
             ],
     columns=columnsOfInterest,
     )
