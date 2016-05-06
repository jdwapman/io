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
from subprocess import call, PIPE, STDOUT

"""
class Director:

    __builder = None
    def setBuilder(self, builder):
        self.__builder = builder

    def build():
        plot = Plot()
        visual = self.__builder.buildPLot()
"""
class Builder:
    """Base class for converting vega-specific graph json files to an actual visual plot.

    This class is the base class, and the child classes inherit the methods and variables of this class.
    The purpose of this class is to specify an abstract interface for creating parts of an output Product object.

    Attributes:

    """

    def __init__(self,input_json):
        """Initis base class with provided atrributes."""
        self.input_json = input_json
        self.output = os.path.splitext(self.input_json)[0]

    def buildPlot(self,verbose=False):
        """builds the actual visual plot. This method is 'virtual' in the Builder class. """
        pass

class PNGBuilder(Builder):
    """class for converting vega-specific graph json files to an actual visual plot as a PNG file.

    This class is a child class of Builder and inherits all the methods and variables.

    Attributes:


    """
    def buildPlot(self,verbose=False):
        """builds the actual visual plot. """
        # call vg2png to turn JSON it into png
        output_png_file = self.output+'.png'
        p = call(['vg2png', self.input_json, output_png_file])
        if(verbose): print("Created " + output_png_file)

class SVGBuilder(Builder):
    """class for converting vega-specific graph json files to an actual visual plot as a PNG file.

    This class is a child class of Builder and inherits all the methods and variables.

    Attributes:


    """
    def buildPlot(self,verbose=False):
        """builds the actual visual plot. """
        # call vg2png to turn JSON it into png
        output_svg_file = self.output+'.svg'
        p = call(['vg2svg', self.input_json, output_svg_file])
        if(verbose): print("Created " + output_svg_file)
