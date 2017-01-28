import json    # built-in


def patchTwoLegends(j):
    if 'marks' not in j.keys():
        return j
    if type(j['marks']) != list:
        return j
    if len(j['marks']) < 1:
        return j
    if 'legends' not in j['marks'][0].keys():
        return j
    if type(j['marks'][0]['legends']) != list:
        return j
    if len(j['marks'][0]['legends']) != 2:
        return j
    if not('stroke' in j['marks'][0]['legends'][0].keys() and j['marks'][0]['legends'][0]['stroke'] == 'color'):
        return j
    if not('shape' in j['marks'][0]['legends'][1].keys() and j['marks'][0]['legends'][1]['shape'] == 'shape'):
        return j
    if not('title' in j['marks'][0]['legends'][0].keys() and
           'title' in j['marks'][0]['legends'][1].keys() and
           j['marks'][0]['legends'][0]['title'] ==
           j['marks'][0]['legends'][1]['title']):
        return j
    for n in [0, 1]:
        if not('properties' in j['marks'][0]['legends'][n].keys() and 'symbols' in j['marks'][0]['legends'][n]['properties'].keys()):
            return j
        for s in ['strokeWidth', 'opacity']:
            if not (s in j['marks'][0]['legends'][n]['properties']['symbols'].keys()):
                return j
            if not ('value' in j['marks'][0]['legends'][n]['properties']['symbols'][s].keys()):
                return j
    d0 = j['marks'][0]['legends'][0]
    d1 = j['marks'][0]['legends'][1]
    for s in ['strokeWidth', 'opacity']:
        if d0['properties']['symbols'][s]['value'] != d1['properties']['symbols'][s]['value']:
            return j
    if not ('shape' in d0['properties']['symbols'].keys() and 'value' in d0['properties']['symbols']['shape']):
        return j
    if not ('stroke' in d1['properties']['symbols'].keys() and 'value' in d1['properties']['symbols']['stroke']):
        return j

    # ok, we're gonna call that good. Construct the new dict now.
    d = {'shape': d1['shape'],
         'title': d0['title'],
         'properties':
         {'symbols':
          {'strokeWidth': {'value':
                           d0['properties']['symbols']['strokeWidth']['value']
                           },
           'opacity': {'value':
                       d0['properties']['symbols']['opacity']['value']
                       },
           'stroke': {'scale': 'color'}
           }
          }
         }

    j['marks'][0]['legends'] = [d]
    return j

# INPUT
#     "marks": [
#         {
#     "legends":
#         [
#             {
#                 "stroke": "color",
#                 "title": "dataset",
#                 "properties": {
#                     "symbols": {
#                         "strokeWidth": {
#                             "value": 2
#                         },
#                         "opacity": {
#                             "value": 0.7
#                         },
#                         "shape": {
#                             "value": "circle"
#                         }
#                     }
#                 }
#             },
#             {
#                 "shape": "shape",
#                 "title": "dataset",
#                 "properties": {
#                     "symbols": {
#                         "strokeWidth": {
#                             "value": 2
#                         },
#                         "opacity": {
#                             "value": 0.7
#                         },
#                         "stroke": {
#                             "value": "#4682b4"
#                         }
#                     }
#                 }
#             }
#         ]
#
#
# OUTPUT
# "legends":
#     [
#         {
#             "shape": "shape",
#             "title": "dataset",
#             "properties": {
#                 "symbols": {
#                     "strokeWidth": {
#                         "value": 2
#                     },
#                     "opacity": {
#                         "value": 0.7
#                     },
#                     "stroke": {
#                         "scale": "color"
#                     }
#                 }
#             }
#         }
#     ]
