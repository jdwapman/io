import os      # built-in
import sys     # built-in
import json    # built-in
from json.decoder import JSONDecodeError
import pandas  # http://pandas.pydata.org


def filesToDF(roots, fnFilterInputFiles):
    json_input_files = []
    for root in roots:
        json_input_files = json_input_files + ([os.path.join(subdir, f)
                                                for (subdir, dirs, files)
                                                in os.walk(root) for f in files])
    # filter input files
    for fn in fnFilterInputFiles:
        json_input_files = list(filter(fn, json_input_files))
    # listify this for Series call at end of fn
    json_input_files = list(json_input_files)

    # json.load(open(file)) -> dict
    data_unfiltered = []
    for jf_file in json_input_files:
        try:
            jf = json.load(open(jf_file))
        except JSONDecodeError:
            print("Invalid JSON file: %s" % jf_file, file=sys.stderr)
        if isinstance(jf, list):  # assume list of dicts
            for d in jf:
                d['details'] = jf_file
                data_unfiltered.append(d)
        else:  # not a list, assume dict
            jf['details'] = jf_file
            data_unfiltered.append(jf)

    # dump input files into dataframe
    # data_unfiltered = [json.load(open(jf)) for jf in json_input_files]
    # next call used to be df = pandas.DataFrame(data_unfiltered)
    # instead, json_normalize flattens nested dicts
    df = pandas.json_normalize(data_unfiltered, sep='_')
    # http://stackoverflow.com/questions/26666919/python-pandas-add-column-in-dataframe-from-list
    # df['details'] = pandas.Series(json_input_files).values
    return df
