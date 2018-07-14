#!/bin/bash

TAG="ADD_YOUR_TAG_HERE"
RESULTDIR="/path/to/json-results" # example: ../gunrock-output/5Apps.ubuntu16.04_v100x1_dev
FILES="PageRank_*" # which json files need the add? For example all PageRank_* runs.

sed -i -e "59i \ \ \ \ \"tag\" : \"$TAG\"," $RESULTDIR/$FILES
