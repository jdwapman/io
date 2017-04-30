#!/usr/bin/env python

import os

for binary in["test_tc_8.0_x86_64"]:
    for dataset in ['preferentialAttachment',
                    'coAuthorsDBLP',
                    'amazon0601',
                    'web-BerkStan',
                    'ldoor',
                    'as-Skitter',
                    'kron_g500-logn21',
                    'cit-Patents',
                    'soc-LiveJournal1',
                    'cage15',
                    'road_central']:
         os.system("../../gunrock/tests/tc/bin/%s market ../../gunrock/dataset/large/%s/%s.mtx --iteration-num=10 --quiet --jsondir=." % (binary, dataset, dataset))
