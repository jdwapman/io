#!/usr/bin/env python

import tarfile
import json
import glob
from datetime import datetime

# run me from directory where the .tar.gz files are. Uncompresses into ./new .

cmdlines = {}

for file in glob.glob('./*.tar.gz'):
    tar = tarfile.open(file, "r:gz")
    for member in [x for x in tar.getmembers() if
                   (x.name.endswith(".json") and x.size > 0)]:
        print file, member.name
        jsonobj = json.load(tar.extractfile(member))

        # 1 GPU only
        if (jsonobj['num_gpus'] != 1):
            # print "Multiple GPUs, skipping"
            continue
        cmdline = jsonobj['command_line']
        gpu = jsonobj['gpuinfo']['name']
        dt = datetime.strptime(jsonobj['time'], "%a %b %d %H:%M:%S %Y\n")

        if (cmdline not in cmdlines):
            cmdlines[cmdline] = {}
        if ((gpu not in cmdlines[cmdline]) or
                (cmdlines[cmdline][gpu] < dt)):
            print "Inserting ", dt, " into ", cmdline
            cmdlines[cmdline][gpu] = dt
    tar.close()

# hash now full
for file in glob.glob('./*.tar.gz'):
    tar = tarfile.open(file, "r:gz")
    for member in [x for x in tar.getmembers() if
                   (x.name.endswith(".json") and x.size > 0)]:
        jsonobj = json.load(tar.extractfile(member))

        # 1 GPU only
        if (jsonobj['num_gpus'] != 1):
            # print "Multiple GPUs, skipping"
            continue
        cmdline = jsonobj['command_line']
        gpu = jsonobj['gpuinfo']['name']
        dt = datetime.strptime(jsonobj['time'], "%a %b %d %H:%M:%S %Y\n")

        if cmdlines[cmdline][gpu] == dt:
            tar.extract(member, path="new/")
            print "Writing: ", file, member.name
    tar.close()
