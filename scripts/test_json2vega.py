#!/usr/bin/env python
"""Sample code to test json2vega.py.

Author: Farmehr Farhour f.farhour@gmail.com.

Contains sample code that calls the functions in json2vega.py as intended.

Usage: simply run the script to create a sample bar graph.
"""

import os
import argparse
import sys  # built-in
import json2vega
from utils import bcolors           #bcolors class used to color commandline output

# function: inputArgs
# Processes input arguments
def inputArgs(argv):
    """function to process input args.

    The various input arguments are defined here. parser.add_argument
        creates a new argument. The function parses the various input
        args passed, and stores them in a list (args). The argeparse
        library automatically takes care of the help command. Args:
        argv: the input arguments passed through commandline. Simply
        pass in sys.argv from the main function.

    Returns:
        args: a  populated namespace of all the inputted commandline arguments.

    """
    # parse args
    parser = argparse.ArgumentParser(
        description=bcolors.HEADER + 'IO Options' + bcolors.ENDC)
    # add the arguments available to user
    parser.add_argument('-d', metavar='<directory>', type=str,
                        help='directory containing input JSON files. Default = /', default='../gunrock-output/')
    parser.add_argument('-o', metavar='<directory>', type=str,
                        help='directory for output files. Default = output/', default='output/')
    # TODO add additional arguments: engine_name,
    # algorithm_name,axes_vars,conditions,config_path
    args = parser.parse_args()
    return args


def main(argv):
    """Creates a bar graph by calling methods in json2vega.py"""
    args = inputArgs(argv)            #process input arguments passed
    if not os.path.exists(args.o):            #create output directory
        os.makedirs(args.o)

    # Create required arguments and instantite bar class object for testing.
<<<<<<< 9133c1fb1bc2e22f2d53180fb68c254a72603043
    conditions = {"algorithm": "BFS",
                  "undirected": True, "mark_predecessors": True}
    axes_vars = {'x': 'dataset', 'y': 'm_teps'}
    bar1 = json2vega.VegaGraphBar(
        args.o, args.d, "config_files/", "g", "BFS", conditions, axes_vars)
=======
    conditions = {"algorithm" : "BFS","undirected" : True ,"mark_predecessors" : True}
    axes_vars = {'x':'dataset','y':'m_teps'}
<<<<<<< d2faaa731d3b0c33158616bd668d1ff533f38f7c
    bar1 = json2vega.VegaGraphBar(output_path=args.o,input_path=args.d,config_dir="config_files",engine_name="g",algorithm_name="BFS",conditions_dict=conditions,axes_vars=axes_vars)
    bar1.run(True)
    """
>>>>>>> Created run function to call all the methods required insted of the user doing so one by one. Have not yet implemented suffix argument. Also used named arguments in test file.
    bar1.read_json()
    bar = bar1.parse_jsons()
    bar1.write_json(bar,"0",True)"""
=======
    names = {'engine_name':'g','algorithm_name':'BFS','x_axis':'Datasets','y_axis':'MTEPS','file_suffix':'0'}
    bar1 = json2vega.VegaGraphBar(output_path=args.o,input_path=args.d,config_dir="config_files",labels=names,conditions_dict=conditions,axes_vars=axes_vars)
    bar1.run(verbose=True)
>>>>>>> Changed input attributes to create the object. Now there is a labels dict that contains the algorithm_name, engine_name, file_suffix, as well as x and y axes labels. So now the file name suffix can be specified. So can the x and y axes labels.

if __name__ == "__main__":
    main(sys.argv)
