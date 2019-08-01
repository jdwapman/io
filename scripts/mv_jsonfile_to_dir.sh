#!/bin/bash

# All this script does is moves the json run, named:
# ALGO_dataset_some date and time.json to its respective
# dataset directory.

# TODO: Change ALGO to correct algorithm (for e.g. SSSP)
for f in ALGO_*.json; do
    name=`echo "$f" | sed 's/.*ALGO_\([^]]*\)_.*/\1/g'`
    mv "$f" "$name"
done
