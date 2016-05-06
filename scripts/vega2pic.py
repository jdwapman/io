#!/usr/bin/env python
"""Converts JSON outputs from json2vega.py (vega-spec jsons) to actual plots.

Author: Farmehr Farhour f.farhour@gmail.com

This file contains a builder pattern class structure to convert generated vega-spec
    JSON files to an actual plot. The output format can be specified by the user.

Dependencies:
    python
    nodejs:
        vega (sudo npm install vega)
        vega-lite (sudo npm install vega-lite)

"""
import os   # built-in


class Builder(object):
    """Base class for converting vega-specific graph json files to an actual visual plot.

    This class is the base class, and the child classes inherit the methods and variables of this class.
    The purpose of this class is to specify an abstract interface for creating parts of an output Product object.

    Attributes:

    """

    def __init__(self,input_json,output_type,output_name,output_dir=""):
        """Initis base class with provided atrributes."""
        self.input_json = input_json
        self.output_type = output_type
        self.output_dir = output_path
        self.output_name = output_name

    def buildPlot(self,verbose=False):
        """builds the actual visual plot. This method is 'virtual' in the Builder class. """

class PNGBuilder(Builder):
    """class for converting vega-specific graph json files to an actual visual plot as a PNG file.

    This class is a child class of Builder and inherits all the methods and variables.

    Attributes:


    """
    def buildPlot(self,verbose=False):
        """builds the actual visual plot. """
        # pipe JSON through vg2png to turn it into png files
        file = open('%s/%s.json' %(self.output_dir,self.output_name), 'w')
        p = Popen(["vg2png"], stdout=file, stdin=PIPE,shell=True)
        vg = p.communicate(input=input_json)[0]
        if(verbose): print("Created " + file.name)
        file.close()
