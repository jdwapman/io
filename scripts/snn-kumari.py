#!/usr/bin/env python3

import altair as alt
import pandas  # http://pandas.pydata.org
import numpy
import datetime

from fileops import save, getChartHTML
from filters import *
from logic import *

name = 'gunrock_snn_kumari'

# begin user settings for this script
roots = ['../gunrock-output/snn-eurpar',
         ]
fnFilterInputFiles = [
    fileEndsWithJSON,
]
fnPreprocessDF = [
    # convertCtimeStringToDatetime,
    # normalizePRMTEPS,
    tupleify('tag'),
    selectTags([
        ('GUNROCK_SNN_KNN',),
        ('KUMARI_R_SNN_KNN',)
    ]
    ),
    mergeAlgorithmIntoPrimitive,
    addJSONDetailsLink,
    gunrockVersionGPU,
]
fnFilterDFRows = [
]
fnPostprocessDF = [
    addInto('elapsed', 'avg-process-time', 'knn-elapsed'),
    mergeSNNElapsedIntoElapsed,
    keepFastestAvgProcessTime(
        ['primitive', 'dataset', 'tag'], sortBy='elapsed')
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
                     'knn-elapsed',
                     'elapsed',
                     'engine',
                     'tag',
                     'gunrock-version',
                     'gpuinfo_name',
                     'n',
                     'time',
                     'details']
# would prefer a cleanup call https://github.com/altair-viz/altair/issues/183
# without this, output is gigantic
df = (keepTheseColumnsOnly(columnsOfInterest))(df)

# now make the graph

datatypes = {
    'advance_mode': 'nominal',
    'avg-mteps': 'quantitative',
    'avg-process-time': 'quantitative',
    'dataset': 'nominal',
    'elapsed': 'quantitative',
    'engine': 'nominal',
    'gpuinfo_name': 'nominal',
    'knn-elapsed': 'quantitative',
    'mark-pred': 'ordinal',
    'n': 'quantitative',
    'num-edges': 'quantitative',
    'primitive': 'nominal',
    'pull': 'nominal',
    'undirected': 'ordinal',
}

chart = {}

for primtuple in [('kd-snn', ''),
                  # ('r-snn', ''),
                  ]:
    primitive = primtuple[0]

    my = {
        ('kd-snn', ''): {
            'y': ('dataset', 'Dataset', 'linear'),
            'x': ('elapsed', 'Runtime (ms)', 'log'),
            'color': ('primitive', 'SNN Implementation'),
            'shape': ('primitive', 'SNN Implementation'),
        },
    }

    selection = {}

    # https://github.com/altair-viz/altair/issues/291
    # how to alter Charts after they're created

    chart[primtuple] = alt.Chart(df).mark_point().encode(
        x=alt.X(my[primtuple]['x'][0],
                type=datatypes[my[primtuple]['x'][0]],
                axis=alt.Axis(
                    title=my[primtuple]['x'][1],
        ),
            scale=alt.Scale(type=my[primtuple]['x'][2]),
        ),
        y=alt.Y(my[primtuple]['y'][0],
                type=datatypes[my[primtuple]['y'][0]],
                # sort=alt.EncodingSortField(field='n'),
                axis=alt.Axis(
                    title=my[primtuple]['y'][1],
        ),
            scale=alt.Scale(type=my[primtuple]['y'][2]),
        ),
        tooltip=['primitive', 'dataset', 'gpuinfo_name', 'n',
                 'avg-process-time', 'knn-elapsed', 'elapsed'],
    ).interactive()
    if ('col' in my[primtuple]):
        chart[primtuple] = chart[primtuple].encode(
            column=alt.Column(my[primtuple]['col'][0],
                              type=datatypes[my[primtuple]['col'][0]],
                              header=alt.Header(title=my[primtuple]['col'][1]),
                              ))
    if ('row' in my[primtuple]):
        chart[primtuple] = chart[primtuple].encode(
            row=alt.Row(my[primtuple]['row'][0],
                        type=datatypes[my[primtuple]['row'][0]],
                        header=alt.Header(title=my[primtuple]['row'][1]),
                        ))
    if ('color' in my[primtuple]):
        color = stripShorthand(my[primtuple]['color'][0])
        chart[primtuple] = chart[primtuple].encode(
            color=alt.Color(color,
                            type=datatypes[color],
                            legend=alt.Legend(title=my[primtuple]['color'][1]),
                            scale=alt.Scale(scheme='dark2')
                            ))
        selection['color'] = alt.selection_multi(fields=[color],
                                                 bind='legend')
        chart[primtuple] = chart[primtuple].add_selection(selection['color'])

    if ('shape' in my[primtuple]):
        shape = stripShorthand(my[primtuple]['shape'][0])
        chart[primtuple] = chart[primtuple].encode(
            shape=alt.Shape(shape,
                            type=datatypes[shape],
                            legend=alt.Legend(title=my[primtuple]['shape'][1]),
                            ))
        selection['shape'] = alt.selection_multi(fields=[shape],
                                                 bind='legend')
        chart[primtuple] = chart[primtuple].add_selection(selection['shape'])

    if primtuple[1] == 'sel':
        # input_checkbox = alt.binding_checkbox()
        # checkbox_selection = alt.selection_single(bind=input_checkbox, name="Big Budget Films")
        # size_checkbox_condition = alt.condition(checkbox_selection,
        #                                         alt.SizeValue(25),
        #                                         alt.Size('Hundred_Million_Production')
        # )
        checkbox = {}
        checkbox_selection = {}
        for box in ['undirected']:
            for l in [box + '_on', box + 'off']:
                checkbox_selection[l] = alt.selection_single(
                    bind=alt.binding_checkbox(),
                    name=l)
                chart[primtuple] = chart[primtuple].add_selection(
                    checkbox_selection[l])

    plotname = '_'.join(filter(lambda x: bool(x),
                               [name, primtuple[0], primtuple[1]]))
    save(chart=chart[primtuple],
         df=df,
         plotname=plotname,
         formats=['tablehtml', 'tablemd', 'md', 'html', 'png', 'svg', 'pdf'],
         sortby=['primitive',
                 'dataset',
                 'engine',
                 'gunrock-version',
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

    #     chart[primtuple] = alt.Chart(df).mark_point().encode(
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
    #     tooltip=['primitive', 'dataset', 'gpuinfo_name', 'num-vertices',
    #              'num-edges', 'advance_mode',
    #              'mark-pred', 'undirected', '64bit-SizeT', '64bit-VertexT',
    #              'avg-mteps', 'avg-process-time']
    # )
