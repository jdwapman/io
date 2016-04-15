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


#Base class to produce vega-spec jsons
class VegaGraphBase(object):
    'Base class for converting json outputs of different algorithms to vega-specific graph json files.'

    #list containing all jsons
    __input_jsons = []

    #Constructor
    def __init__(self,output_path,input_path,config_path,engine_name,algorithm_name):
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
            if(os.path.splitext(f)[1]==".json") and (os.path.basename(f).startswith(self.algorithm_name)) and (not os.path.basename(f).startswith("_")):
                self.__input_jsons += [json.load(open(self.input_path + f))]

    #function: read_config
    def read_config(self):
        #return the json config file
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
    #TODO add additional arguments: engine_name, algorithm_name,axes_vars,conditions,config_path
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

    #instantite bar class object for testing
    conditions = {"algorithm" : "BFS","undirected" : True ,"mark_predecessors" : True}
    axes_vars = {'x':'dataset','y':'m_teps'}
    bar1 = VegaGraphBar(args.o,args.d,"","g","BFS",conditions,axes_vars)
    bar1.read_json()
    bar = bar1.parse_jsons()
    bar1.write_json(bar,"0")

if __name__ == "__main__":
   main(sys.argv)
