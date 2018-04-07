import os      # built-in
import json    # built-in
import pandas  # http://pandas.pydata.org
from pandas.io.json import json_normalize


def filesToDF(roots, fnFilterInputFiles):
    json_input_files = []
    for root in roots:
        json_input_files = json_input_files + ([os.path.join(subdir, f)
                                                for (subdir, dirs, files)
                                                in os.walk(root) for f in files])
    # filter input files
    for fn in fnFilterInputFiles:
        json_input_files = filter(fn, json_input_files)
    # listify this for Series call at end of fn
    json_input_files = list(json_input_files)

    # dump input files into dataframe
    data_unfiltered = [json.load(open(jf)) for jf in json_input_files]
    # next call used to be df = pandas.DataFrame(data_unfiltered)
    # instead, json_normalize flattens nested dicts
    df = json_normalize(data_unfiltered)
    # http://stackoverflow.com/questions/26666919/python-pandas-add-column-in-dataframe-from-list
    df['details'] = pandas.Series(json_input_files).values
    return df
