#!/usr/bin/env python

import vincent # http://vincent.readthedocs.org/en/latest/
               # https://github.com/wrobstory/vincent
import pandas  # http://pandas.pydata.org
import json    # built-in
import os      # built-in

## Load all JSON files into an array of dicts.
## Each array element is one JSON input file (one run).
## Each JSON input file is a dict indexed by attribute.
## If we have more than one JSON object per file:
## http://stackoverflow.com/questions/20400818/python-trying-to-deserialize-multiple-json-objects-in-a-file-with-each-object-s

json_files = [f for f in os.listdir('.')
              if (os.path.isfile(f) and
                  f.endswith(".json"))]
data_unfiltered = [json.load(open(jf)) for jf in json_files]
results = {}
for d in data_unfiltered:
    print d["dataset"], d["alpha"], d["beta"], d["m_teps"]
