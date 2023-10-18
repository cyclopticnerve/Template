#! /usr/bin/env python
# ------------------------------------------------------------------------------
# Project : __PP_NAME_BIG__                                        /          \
# Filename: __PP_NAME_SMALL___config.py                           |     ()     |
# Date    : __PP_DATE__                                           |            |
# Author  : __PP_AUTHOR__                                         |   \____/   |
# License : __PP_LICENSE_NAME__                                    \          /
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

# system imports
import argparse
import json
from pathlib import Path

# ------------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------------

# some useful constants
_DIR_HOME = Path.home()

# the key in args for the config file (shown in help)
PATH_CONFIG_ARG = "PATH_CONFIG"

# the path to the default config file
_PATH_CONFIG_DEF = _DIR_HOME / ".config" / "__PP_NAME_BIG__" / "config.json"

# ------------------------------------------------------------------------------
# Globals
# ------------------------------------------------------------------------------

# args are global so we can read them from any function
# they are only set once, in __name__()
G_DICT_ARGS = {}

# the global config dict (built-in or loaded from config file)
# they are set twice (once in load_config(), and again in _save_gui()
# order of precedence is:
# 1. this definition
# 2. file at _PATH_CONFIG_DEF
# 3. command line flag -c
G_DICT_CONFIG = {}

# ------------------------------------------------------------------------------
# Public functions
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# The main function of the program
# ------------------------------------------------------------------------------
def main():
    """
    The main function of the program

    This function is the main entry point for the program, initializing the
    program, and performing its steps.
    """

    # call the steps in order
    print(func())


# ------------------------------------------------------------------------------
# Adds command line args to the parser
# ------------------------------------------------------------------------------
def add_args(argparser):
    """
    Adds command line args to the parser

    Arguments:
        argparser: The argparse object to add args to

    This function adds arguments to the parser. IT SHOULD NEVER BE CALLED IN
    CODE! It is teased out to make editing command line parameters easier.
    """

    # NB: https://docs.python.org/3/library/argparse.html
    argparser.add_argument(
        "-c",
        dest=PATH_CONFIG_ARG,
        help="load configuration from file",
        metavar="FILE",
    )


# ------------------------------------------------------------------------------
# Short description
# ------------------------------------------------------------------------------
def func():
    """
    Short description

    Arguments:
        var_name: Description

    Returns:
        Description

    Raises:
        exception_type(vars): Description

    Long description (including HTML).
    """

    return "this is func"


# ------------------------------------------------------------------------------
# Private functions
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Parses command line args and sets the global dict
# ------------------------------------------------------------------------------
def _parse_args():
    """
    Parses command line args and sets the global dict

    This function gets the command line passed to the program, parses it,
    and sets the command line options as a global dict.
    """

    # the global dict of arguments
    global G_DICT_ARGS

    # create the parser
    argparser = argparse.ArgumentParser(description="__PP_SHORT_DESC__")

    # add version argument
    argparser.add_argument(
        "-v",
        "--version",
        action="version",
        version="__PP_VERSION__",
    )

    # add arguments from the function above
    add_args(argparser)

    # parse the arg list into a Namespace object (similar to dict)
    # NB: if there is an error in the command line, this function will:
    # 1. print usage
    # 2. print the error
    # 3. exit
    args = argparser.parse_args()

    # convert args to global dict
    G_DICT_ARGS = vars(args)


# ------------------------------------------------------------------------------
# Load config file from specified path
# ------------------------------------------------------------------------------
def _load_config(path):
    """
    Loads config file from specified path

    Arguments:
        path: The path to the config file to load from

    Raises:
        Exception(str): If the file is not a valid JSON file

    Load the global config from a file at the specified location.
    """

    # the dictionary to load to
    global G_DICT_CONFIG

    # sanity check
    if path is None or not path.is_file():
        return

    # open the file for reading
    try:
        with open(path, "r") as f:
            G_DICT_CONFIG = json.load(f)
    except Exception:
        raise Exception(f'_load_config: "{path}" is not a valid JSON file')


# ------------------------------------------------------------------------------
# Save config file to specified path
# ------------------------------------------------------------------------------
def _save_config(path):
    """
    Saves config file to specified path

    Arguments:
        path: The path to the config file to save to

    Raises:
        Exception(str): If the file does not exist and can't be created

    Save the global config to a file at the specified location.
    """

    # sanity check
    if path is None or path == "":
        return

    # open the file for writing (and create if it doesn't exist)
    try:
        # first make dirs
        dir_config = path.parent
        if dir_config != "":
            path.parent.mkdir(parents=True, exist_ok=True)

        # then write to file
        with open(path, "w") as f:
            json.dump(G_DICT_CONFIG, f, indent=4)
    except Exception:
        raise Exception(f'_save_config: "{path}" cannot be created')


# ------------------------------------------------------------------------------
# Code to run when called from command line
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    # Code to run when called from command line

    # This is the top level code of the program, called when the Python file is
    # invoked from the command line.

    # get command-line args and set them to the global dict
    _parse_args()

    # set default path
    path_config = _PATH_CONFIG_DEF

    # check if there is an arg for config path
    if PATH_CONFIG_ARG in G_DICT_ARGS.keys():
        path_config = G_DICT_ARGS[PATH_CONFIG_ARG]
        if path_config is not None and path_config != "":
            # load from the arg path
            path_config = G_DICT_ARGS[PATH_CONFIG_ARG]

    # load config dict from file (or just keep built-in)
    _load_config(path_config)

    # run main function
    main()

    # save config dict to file
    _save_config(path_config)

# -)
