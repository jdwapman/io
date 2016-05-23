    #!/usr/bin/env python
"""Sample code to test json2vega.py.

Author: Farmehr Farhour f.farhour@gmail.com.

Contains sample code that calls the functions in json2vega.py as intended.

Usage: simply run the script to create a sample bar graph.
"""

import os   # built-in
import sys  # built-in
import json2vega
from utils import bcolors, parseCmdLineArgs  # bcolors class used to color commandline output. parseCmdLineArgs used to parse commandline arguments

def main(argv):
    """Creates a bar graph by calling methods in json2vega.py"""

    args = parseCmdLineArgs(argv)  # process input arguments passed
    if not os.path.exists(args.o):  # create output directory
        os.makedirs(args.o)

    # Create required arguments and instantite bar class object for testing.
    conditions = {"algorithm": "BFS",
                  "undirected": True, "mark_predecessors": True}
    axes_vars = {'x': 'dataset', 'y': 'm_teps'}
    names = {'engine_name': 'g', 'algorithm_name': 'BFS',
             'x_axis': 'Datasets', 'y_axis': 'MTEPS', 'file_suffix': '0'}
    bar1 = json2vega.VegaGraphBar(output_path=args.o,
                                  input_path=args.d,
                                  config_dir="config_files",
                                  labels=names,
                                  conditions_dict=conditions,
                                  axes_vars=axes_vars)
    bar1.run(verbose=True)


if __name__ == "__main__":
    main(sys.argv)
