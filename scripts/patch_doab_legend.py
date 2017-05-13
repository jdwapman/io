#!/usr/bin/env python
import glob
import os
import re
from fileops import savefile

# Read in the file
files = glob.glob('output/do_ab_random_?????*.svg')
for f in files:
    stub = os.path.splitext(os.path.split(f)[1])[0]
    print stub
    with open(f, 'rb') as file:
        filedata = file.read()

    # Replace the target string
    p = re.compile(r'^<svg class="marks" width="(\d+)" height="(\d+)"')
    m = p.match(filedata)
    w = m.group(1)
    h = m.group(2)
    # w: subtract 125
    # h: add 48
    whin = 'width="%s" height="%s"' % (w, h)
    neww = int(w) - 125
    newh = int(h) + 48
    print 'w:', w, neww, 'h:', h, newh
    whout = 'width="%s" height="%s"' % (neww, newh)
    filedata = filedata.replace(whin, whout)
    # 'width="590" height="462"', 'width="465" height="510"')
    filedata = filedata.replace('translate(404.5,0.5)', 'translate(260,390)')

    # Write the file out again
    with open(f, 'wb') as file:
        file.write(filedata)

    savefile('', stub, 'pdf', 'output', patchFunctions=[])
