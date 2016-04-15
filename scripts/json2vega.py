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


#class: VegaGraphBase
class VegaGraphBase(object):
    'Base class for converting json outputs of different algorithms to vega-specific graph json files.'

    input_json_files = []

    #Constructor
    def __init__(self,output_path,input_path,config_path,engine_name,alrogithm_name):
        self.output_path = output_path
        self.input_path = input_path
        self.config_path = config_path
        self.engine_name = engine_name
        self.algorithm_name = algorithm_name

    #function: read_json
    #reads json files with the right specs to input_json_files list
    def read_json(self):
        #read in all json files in the input_path, that match the algorithm_name and are not outputs
        for f in os.listdir(self.input_path):
            if(os.path.splittext(f)[1]==".json") and (os.path.basename(f).startswith(self.algorithm_name)) and (not os.path.basename(f).startswith("_")):
                self.input_json_files.append(f)


    #function: read_config
    def read_config(self):

    #function: write_json
    #output json to the output_path and with a specific name
    def write_json(self,json_in,json_name):
        # pipe it through vl2vg to turn it into vega
        file = open('%s_%s_%s.json' %(self.output_path,self.algorithm_name,json_name), 'w')
        p = Popen(["vl2vg"], stdout=file, stdin=PIPE)
        vg = p.communicate(input=json.dumps(json_in))[0]
        file.close()


"""
#function: write_json
#write json to a specified file.
def write_json(json_in, json_name, algorithm_name):
    # pipe it through vl2vg to turn it into vega
    file = open('%s_%s_%s.json' %(args.o,algorithm_name,json_name), 'w')
    p = Popen(["vl2vg"], stdout=file, stdin=PIPE)
    vg = p.communicate(input=json.dumps(json_in))[0]
    file.close()
"""

#function: inputArgs
#Processes input arguments
def inputArgs(argv):
    #define global variablesbeing used as input args
    global g_iDir
    global g_oDir
    #parse args
    parser = argparse.ArgumentParser(description=bcolors.HEADER + 'IO Options' + bcolors.ENDC)
    parser.add_argument('-d', metavar='<directory>', type=str, help='directory containing input JSON files. Default = /', default='/')
    parser.add_argument('-o', metavar='<directory>', type=str, help='directory for output files. Default = output/', default='output/')
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
    write_json(bar, "json_name","g")


if __name__ == "__main__":
   main(sys.argv)
