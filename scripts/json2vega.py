#!/usr/bin/env python
"""Converts JSON outputs from graph algorithms to vega-spec json files to be plotted.

Author: Farmehr Farhour f.farhour@gmail.com
Some code refactored and re-used from testvl.py script written by JDO

This file contains a base class, and a child class for each type of graph to be plotted.
"""

import pandas, numpy
import json, os, sys, argparse          #built-in
from subprocess import Popen, PIPE, STDOUT          #built-in

class bcolors:
	"""Used to implement ANSI colors without the need to remember the numbers.

	Does not contain any methods. Only contains variables.

	Usage: simply concatenate bcolors.<color> at the start of string to be printed,
		and bcolors.ENDC at the end of the string, to color the string with the
		specified color.
	"""

	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

#Base class to produce vega-spec jsons
class VegaGraphBase(object):
    """Base class for converting json outputs of different algorithms to vega-specific graph json files.

    This class is the base class, and the child classes inherit the methods and variables of this class.
    The purpose of this class is to centralise the main functionalities shared by all child classes.

    Attributes:
        output_path: the output directory to write the vega-spec json files to.
        input_path: the input path containing the input json files to be processed.
        config_path: the directory containing the json config files relevant to each plot type.
            Each config file will need to have a specific name of the format: '<plot type>_config.json'
        engine_name: the name of the engine used to run the algorithm (e.g. Gunrock). This is
            used to name the output files.
        algorithm_name: the name of the algorithm (e.g. BFS). This is used to name the
            output files.
    """

    #list containing all jsons
    __input_jsons = []


    def __init__(self,output_path,input_path,config_path,engine_name,algorithm_name):
        """Initis base class with provided atrributes."""
        self.output_path = output_path
        self.input_path = input_path
        self.config_path = config_path
        self.engine_name = engine_name
        self.algorithm_name = algorithm_name


    def read_json(self):
        """Reads json files wiht the right specs into __input_jsons list

        Does not take any arguments.
        Does not return any variables.
        """
        #read in all json files in the input_path, that match the algorithm_name and are not outputs
        for f in os.listdir(self.input_path):
            if(os.path.splitext(f)[1]==".json") and (os.path.basename(f).startswith(self.algorithm_name)) and (not os.path.basename(f).startswith("_")):
                self.__input_jsons += [json.load(open(self.input_path + f))]


    def read_config(self):
        """Returns the json config file as a python object"""
        return json.load(open(self.config_path + "bar_config.json"))

    #function: parse_jsons
    def parse_jsons(self):
        #store all data in a pandas DataFrame
        pandas_df = pandas.DataFrame(self.__input_jsons)
        return pandas_df
    #function: write_json
    #output json to the output_path and with a specific name
    def write_json(self,json_in,suffix=""):
        # pipe it through vl2vg to turn it into vega
        file = open('%s_%s_%s_%s.json' %(self.output_path,self.engine_name,self.algorithm_name,suffix), 'w')
        p = Popen(["vl2vg"], stdout=file, stdin=PIPE)
        vg = p.communicate(input=json.dumps(json_in))[0]
        file.close()

#Class to produce vega bar graphs
class VegaGraphBar(VegaGraphBase):
    'Class to produce bar graphs from specified data'

    #Constructor
    def __init__(self,output_path,input_path,config_path,engine_name,algorithm_name,conditions_dict,axes_vars):
        self.conditions_dict = conditions_dict
        self.axes_vars = axes_vars
        super(VegaGraphBar,self).__init__(output_path,input_path,config_path,engine_name,algorithm_name)


    def parse_jsons(self):
        pandas_df = super(VegaGraphBar,self).parse_jsons()
        #restricted bar graph, based on conditions_dict provided
        df_restricted = pandas_df
        for key,value in self.conditions_dict.iteritems():
            df_restricted = df_restricted.loc[df_restricted[key]==value]

        # delete everything except dataset (index) and the desired variable
        df_restricted = pandas.DataFrame(df_restricted.set_index(self.axes_vars['x'])[self.axes_vars['y']])
        #turn dataset back to vanilla column instead of index
        df_restricted = df_restricted.reset_index()
        #complete vega-lite bar description
        bar = self.read_config()
        # add extracted data to json
        bar["data"] = {"values":df_restricted.to_dict(orient='records')}
        # add relevant attributes to y and x axes based on input data
        bar["encoding"]["y"]["field"]=self.axes_vars['y']
        bar["encoding"]["y"]["axis"] = {"title":self.axes_vars['y']}
        #check whether axis is quantitative or ordinal. add respective attributes to json
        for key in self.axes_vars:
            if(df_restricted[self.axes_vars[key]].dtype=='float64'):
                bar["encoding"][key]["type"]="quantitative"
            else:
                bar["encoding"][key]["type"]="ordinal"
        bar["encoding"]["x"]["field"]=self.axes_vars['x']

        #print(json.dumps(bar))
        #return json
        return bar
