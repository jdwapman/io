#!/usr/bin/env python
"""Contains useful functions that are not necessary for proper functionality of scripts.

Author: Farmehr Farhour f.farhour@gmail.com

Contains:
bcolors class: that can be imported and used to color commandline outputs using ANSI colors.
parseCmdLineArgs function: parses inut commandline arguments
"""

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


import argparse # built-in
def parseCmdLineArgs(argv):
    """Function to process input args.

    The various input arguments are defined here. parser.add_argument
        creates a new argument. The function parses the various input
        args passed, and stores them in a list (args). The argparse
        library automatically takes care of the help command.

    Args:
        argv: the input arguments passed through commandline. Simply
            pass in sys.argv from the main function.

    Returns:
        args: a  populated namespace of all the inputted command-line arguments.

    """

    # parse args
    parser = argparse.ArgumentParser(
        description=bcolors.HEADER + 'IO Options' + bcolors.ENDC)
    # add the arguments available to user
    parser.add_argument('-d', metavar='<directory>', type=str,
                        help='directory containing input JSON files. Default= / ',
                        default='../gunrock-output/')
    parser.add_argument('-o', metavar='<directory>', type=str,
                        help='directory for output files. Default= output/',
                        default='output/')
    # TODO add additional arguments: engine_name,
    # algorithm_name,axes_vars,conditions,config_path
    args = parser.parse_args()
    return args
