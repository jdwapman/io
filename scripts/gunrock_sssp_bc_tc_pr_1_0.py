#!/usr/bin/env python3

import altair as alt
import pandas  # http://pandas.pydata.org
import numpy
import datetime

from fileops import save, getChartHTML
from filters import *
from logic import *

name = 'gunrock_sssp_bc_1_0'

# begin user settings for this script
roots = ['../gunrock-output/v1-0-0/sssp',
         '../gunrock-output/v1-0-0/bc',
         '../gunrock-output/v1-0-0/tc',
         '../gunrock-output/v1-0-0/pr']
fnFilterInputFiles = [
    fileEndsWithJSON,
]
fnPreprocessDF = [
    # convertCtimeStringToDatetime,
    # normalizePRMTEPS,
    mergeAlgorithmIntoPrimitive,
    SSSPtosssp,
    renameAdvanceModeWithAHyphen,
    addJSONDetailsLink,
    gunrockVersionGPU,
]
fnFilterDFRows = [
    filterOut(True, '64bit-SizeT'),
    filterOut(True, '64bit-VertexT'),
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
                     'engine',
                     # 'tag',
                     'num-vertices',
                     'num-edges',
                     'gunrock-version',
                     'gpuinfo.name',
                     'advance_mode',
                     'undirected',
                     'pull',
                     'mark-pred',
                     '64bit-SizeT',
                     '64bit-VertexT',
                     'time',
                     'details']
# would prefer a cleanup call https://github.com/altair-viz/altair/issues/183
# without this, output is gigantic
df = (keepTheseColumnsOnly(columnsOfInterest))(df)

# now make the graph

chart = {}

for primtuple in [('sssp', ''),
                  ('bc', ''),
                  ('tc', ''),
                  ('tc', 'edges'),
                  ('pr', ''),
                  ('pr', 'V100-undirected'),
                  ]:
    primitive = primtuple[0]
    dfx = df[df['primitive'] == primitive]

    my = {
        ('sssp', ''): {
            'x': ('dataset:N', 'Dataset', 'linear'),
            'y': ('avg-mteps:Q', 'MTEPS', 'log'),
            'col': ('mark-pred:O', 'Mark Predecessors'),
            'row': ('undirected:O', 'Undirected'),
            'color': ('advance_mode:N', 'Advance Mode'),
            'shape': ('[gpuinfo.name]:N', 'GPU'),
        },
        ('bc', ''): {
            'x': ('dataset:N', 'Dataset', 'linear'),
            'y': ('avg-mteps:Q', 'MTEPS', 'log'),
            'col': ('mark-pred:O', 'Mark Predecessors'),
            'row': ('undirected:O', 'Undirected'),
            'color': ('advance_mode:N', 'Advance Mode'),
            'shape': ('[gpuinfo.name]:N', 'GPU'),
        },
        ('tc', ''): {
            'x': ('dataset:N', 'Dataset', 'linear'),
            'y': ('avg-process-time:Q', 'Runtime (ms)', 'log'),
            'col': ('mark-pred:O', 'Mark Predecessors'),
            'row': ('undirected:O', 'Undirected'),
            'color': ('[gpuinfo.name]:N', 'GPU'),
            'shape': ('advance_mode:N', 'Advance Mode'),
        },
        ('tc', 'edges'): {
            'x': ('num-edges:Q', 'Number of Edges', 'log'),
            'y': ('avg-process-time:Q', 'Runtime (ms)', 'log'),
            'row': ('undirected:O', 'Undirected'),
            'col': ('mark-pred:O', 'Mark Predecessors'),
            'color': ('dataset:N', 'Dataset'),
            'shape': ('[gpuinfo.name]:N', 'GPU'),
        },
        ('pr', ''): {
            'x': ('dataset:N', 'Dataset', 'linear'),
            'y': ('avg-process-time:Q', 'Runtime (ms)', 'log'),
            'col': ('pull:O', 'Pull'),
            'row': ('undirected:O', 'Undirected'),
            'color': ('advance_mode', 'Advance Mode'),
            'shape': ('[gpuinfo.name]:N', 'GPU'),
        },
        ('pr', 'V100-undirected'): {
            'x': ('dataset:N', 'Dataset', 'linear'),
            'y': ('avg-process-time:Q', 'Runtime (ms)', 'log'),
            'color': ('advance_mode:N', 'Advance Mode'),
            'shape': ('pull:O', 'Pull'),
        },
    }
    selection = alt.selection_multi(fields=[my[primtuple]['shape'][0]],
                                    bind='legend')

    if (primtuple == ('pr', 'V100-undirected')):
        dfx = dfx[(dfx['gpuinfo.name'] == 'Quadro GV100') &
                  (dfx['undirected'] == True)
                  ]
    # https://github.com/altair-viz/altair/issues/291
    # how to alter Charts after they're created

    chart[primtuple] = alt.Chart(dfx).mark_point().encode(
        x=alt.X(my[primtuple]['x'][0],
                axis=alt.Axis(
                    title=my[primtuple]['x'][1],
        ),
            scale=alt.Scale(type=my[primtuple]['x'][2]),
        ),
        y=alt.Y(my[primtuple]['y'][0],
                axis=alt.Axis(
                    title=my[primtuple]['y'][1],
        ),
            scale=alt.Scale(type=my[primtuple]['y'][2]),
        ),
        tooltip=['primitive', 'dataset:N', '[gpuinfo.name]:N', 'num-vertices',
                 'num-edges', 'advance_mode:N',
                 'mark-pred', 'undirected', '64bit-SizeT', '64bit-VertexT',
                 'avg-mteps:Q', 'avg-process-time:Q'],
    ).interactive()
    if ('col' in my[primtuple]):
        chart[primtuple] = chart[primtuple].encode(
            column=alt.Column(my[primtuple]['col'][0],
                              header=alt.Header(title=my[primtuple]['col'][1]),
                              ))
    if ('row' in my[primtuple]):
        chart[primtuple] = chart[primtuple].encode(
            row=alt.Row(my[primtuple]['row'][0],
                        header=alt.Header(title=my[primtuple]['row'][1]),
                        ))
    selection_fields = []
    for field in ['color', 'shape']:
        if (field in my[primtuple]):
            selection_fields.append(my[primtuple][field][0])
    if selection_fields != []:
        selection = alt.selection_multi(fields=selection_fields,
                                        bind='legend')
    if ('color' in my[primtuple]):
        chart[primtuple] = chart[primtuple].encode(
            color=alt.Color(my[primtuple]['color'][0],
                            legend=alt.Legend(title=my[primtuple]['color'][1]),
                            scale=alt.Scale(scheme='dark2')
                            ))
    if ('shape' in my[primtuple]):
        chart[primtuple] = chart[primtuple].encode(
            shape=alt.Shape(my[primtuple]['shape'][0],
                            legend=alt.Legend(title=my[primtuple]['shape'][1]),
                            ))
    if selection_fields != []:
        chart[primtuple] = chart[primtuple].encode(
            opacity=alt.condition(
                selection, alt.value(1), alt.value(0.25)
            ))
        chart[primtuple] = chart[primtuple].add_selection(selection)

    plotname = '_'.join([name, primtuple[0], primtuple[1]])
    save(chart=chart[primtuple],
         df=dfx,
         plotname=plotname,
         formats=['tablehtml', 'tablemd', 'md', 'html', 'png', 'svg', 'pdf'],
         sortby=['primitive',
                 'dataset',
                 'engine',
                 'gunrock-version',
                 'undirected',
                 'mark-pred',
                 'advance_mode',
                 ],
         columns=columnsOfInterest,
         mdtext=("""
         # Data for %s

         """ % primtuple[0] +
                 getChartHTML(chart[primtuple], anchor=plotname) +
                 """
                 [Source data](tables/%s_table.html), with links to the output JSON for each run
                 """ % plotname),
         )

    #     chart[primtuple] = alt.Chart(dfx).mark_point().encode(
    #     x=alt.X(my[primtuple]['x'][0],
    #             axis=alt.Axis(
    #         title=my[primtuple]['x'][1],
    #     ),
    #         scale=alt.Scale(type=my[primtuple]['x'][2]),
    #     ),
    #     y=alt.Y(my[primtuple]['y'][0],
    #             axis=alt.Axis(
    #         title=my[primtuple]['y'][1],
    #     ),
    #         scale=alt.Scale(type=my[primtuple]['y'][2]),
    #     ),
    # ).interactive()
    # if ('column' in my[primtuple]):
    #     chart[primtuple].encode(
    #         column=alt.Column(my[primtuple]['col'][0],
    #                           header=alt.Header(title=my[primtuple]['col'][1]),
    #                           ))
    # if ('row' in my[primtuple]):
    #     chart[primtuple].encode(
    #         row=alt.Row(my[primtuple]['row'][0],
    #                     header=alt.Header(title=my[primtuple]['row'][1]),
    #                     ))
    # if ('color' in my[primtuple]):
    #     chart[primtuple].encode(
    #         color=alt.Color(my[primtuple]['color'][0],
    #                         legend=alt.Legend(title=my[primtuple]['color'][1]),
    #                         scale=alt.Scale(scheme='dark2'),
    #                         ))
    # if ('shape' in my[primtuple]):
    #     chart[primtuple].encode(
    #         shape=alt.Shape(my[primtuple]['shape'][0],
    #                         legend=alt.Legend(title=my[primtuple]['shape'][1]),
    #                         ))
    # chart[primtuple].encode(
    #     tooltip=['primitive', 'dataset:N', '[gpuinfo.name]:N', 'num-vertices',
    #              'num-edges', 'advance_mode:N',
    #              'mark-pred', 'undirected', '64bit-SizeT', '64bit-VertexT',
    #              'avg-mteps:Q', 'avg-process-time:Q']
    # )
