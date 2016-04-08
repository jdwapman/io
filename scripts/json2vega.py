#!/usr/bin/env python

#Author: Farmehr Farhour f.farhour@gmail.com
#Some code refactored and re-used from testvl.py script written by JDO

import pandas, numpy
import json, os, sys, argparse  #built-in
from subprocess import Popen, PIPE, STDOUT # built-in

#class: bcolors
#Class for coloring terminal outputs using ANSI color codes
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#function: write_json
#write json to a specified file.
def write_json(json_in, json_name):
    # pipe it through vl2vg to turn it into vega
    file = open('%s_g_%s.json' %(args.o,json_name), 'w')
    p = Popen(["vl2vg"], stdout=file, stdin=PIPE)
    vg = p.communicate(input=json.dumps(json_in))[0]
    file.close()

#function: inputArgs
#Processes input arguments
def inputArgs(argv):
    #define global variablesbeing used as input args
    global g_iDir
    global g_oDir
    #parse args
    parser = argparse.ArgumentParser(description=bcolors.HEADER + 'IO Options' + bcolors.ENDC)
    parser.add_argument('-d', metavar='<directory>', type=str, help='directory containing input JSON files', default='/')
    parser.add_argument('-o', metavar='<directory>', type=str, help='directory for output files', default='output/')
    global args
    args = parser.parse_args()

#---<<MAIN function starts here>>---
def main(argv):
    #---<<PRINT HEADER>> ---
    print bcolors.HEADER + "Script to convert generated JSON files to vega-format JSONs" + bcolors.ENDC
    print bcolors.HEADER + "Author: Farmehr Farhour f.farhour@gmail.com" + bcolors.ENDC

    #process input arguments passed
    inputArgs(argv)
    #create output directory
    if not os.path.exists(args.o):
        os.makedirs(args.o)


#TESTS
    ## Sample bar graph json for testing
    bar = {
        "mark": "point",
        "encoding": {
            "y": {"scale": {"type": "log"},
                  "type": "quantitative",
                  "field": "m_teps",
                  "axis": {
                      "title": "MTEPS"
                  }
            },
            "x": {"type": "ordinal",
                  "field": "dataset"
            }
        }
    }
    write_json(bar, "json_name")


if __name__ == "__main__":
   main(sys.argv[1:])
