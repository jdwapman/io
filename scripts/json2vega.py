#!/usr/bin/env python

#Author: Farmehr Farhour f.farhour@gmail.com

import pandas, numpy, json, os
import sys, argparse

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


#function: inputArgs
def inputArgs(argv):
    #define global variablesbeing used as input args
    global g_iDir
    global g_oDir
    #parse args
    parser = argparse.ArgumentParser(description=bcolors.HEADER + 'IO Options' + bcolors.ENDC)
    parser.add_argument('-d', metavar='<directory>', type=str, help='directory containing input JSON files', default='/')
    parser.add_argument('-o', metavar='<directory>', type=str, help='directory for output files', default='/output/')
    args = parser.parse_args()

#---<<MAIN function starts here>>---
def main(argv):
    #---<<PRINT HEADER>> ---
    print bcolors.HEADER + "Script to convert generated JSON files to vega-format JSONs" + bcolors.ENDC
    print bcolors.HEADER + "Author: Farmehr Farhour f.farhour@gmail.com" + bcolors.ENDC

    #process input arguments passed
    inputArgs(argv)

    #function: User_Input
    #In:    disp_name: display name of the variable required to ask the user.
    #In:    default_val: default value of the variable
    #Out:   variable value as given by user
    def User_Input(disp_name, default_val):
        print "hello"

if __name__ == "__main__":
   main(sys.argv[1:])
