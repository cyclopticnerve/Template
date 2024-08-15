#! /usr/bin/env python
# ------------------------------------------------------------------------------
# Project : __PP_NAME_BIG__                                        /          \
# Filename: __PP_NAME_SMALL__                                     |     ()     |
# Date    : __PP_DATE__                                           |            |
# Author  : __PP_AUTHOR__                                         |   \____/   |
# License : __PP_LICENSE_NAME__                                    \          /
# ------------------------------------------------------------------------------

# pyplate: disable=replace
"""
The main file that runs the program

This file is executable and can be called from the terminal like:

foo@bar:~$ cd [path to directory of this file]
foo@bar:~[path to directory of this file]$ ./__PP_NAME_SMALL__ [cmd line]

or if installed in a global location:

foo@bar:~$ __PP_NAME_SMALL__ [cmd line]

Typical usage is show in the main() method.
"""
# pyplate: enable=replace

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

# system imports
from pathlib import Path
import sys

# pylint: disable=wrong-import-position
# pylint: disable=wrong-import-order
# pylint: disable=no-name-in-module
# pylint: disable=import-error

# my imports
# add custom import paths

# find paths to dev or user
DIR_PARENT = Path(__file__).parent.resolve()
if DIR_PARENT.name == "__PP_DEV_SRC__":
    DIR_PRJ = DIR_PARENT.parent
    DIR_CFG = DIR_PRJ / "__PP_DEV_CONF__"
    DIR_LIB = Path.home() / "__PP_DEV_PP__" / "lib"
    DIR_SRC = DIR_PRJ / "__PP_DEV_SRC__" / "__PP_SUPPORT__"
else:
    DIR_HOME = Path.home()
    DIR_CFG = DIR_HOME / "__PP_USR_CONF__"
    DIR_LIB = DIR_HOME / "__PP_USR_LIB__"
    DIR_SRC = DIR_HOME / "__PP_USR_SRC__"

# add paths to import search
sys.path.append(str(DIR_LIB))
sys.path.append(str(DIR_SRC))

# import my stuff
from cnlib import cnfunctions as F  # type: ignore
from cnlib.cncli import CNCli  # type: ignore

# pylint: enable=wrong-import-position
# pylint: enable=wrong-import-order
# pylint: enable=no-name-in-module
# pylint: enable=import-error

# ------------------------------------------------------------------------------
# Required for pybaker
# ------------------------------------------------------------------------------

# globals for pb to find
PB_VERSION = "__PP_VERSION__"

# ------------------------------------------------------------------------------
# Public classes
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# The main class, responsible for the operation of the program
# ------------------------------------------------------------------------------
class __PP_NAME_CLASS__(CNCli):
    """
    The main class, responsible for the operation of the program

    Public methods:
        main: The main method of the program

    This class does the most of the work of a typical CLI program. It parses
    command line options, loads/saves config files, and performs the operations
    required for the program.
    """

    # --------------------------------------------------------------------------
    # Class methods
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # Initialize the new object
    # --------------------------------------------------------------------------
    def __init__(self):
        """
        Initialize the new object

        Initializes a new instance of the class, setting the default values
        of its properties, and any other code that needs to run to create a
        new object.
        """

        # call super init to initialize the base class
        super().__init__()

        # set default property values
        # NB: commented props are from super
        # self._d_args = {}   # from super
        # self._dict_cfg = {}    # from super
        # self._p_cfg = None  # from super
        self._debug = False

    # --------------------------------------------------------------------------
    # Public methods
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # The main method of the program
    # --------------------------------------------------------------------------
    def main(self):
        """
        The main method of the program

        This method is the main entry point for the program, initializing the
        program, and performing its steps.
        """

        # ----------------------------------------------------------------------
        # setup

        # call boilerplate code
        self._setup()

        # ----------------------------------------------------------------------
        # main stuff

        # do the thing with the thing
        print(self._func())

        # ----------------------------------------------------------------------
        # teardown

        # call boilerplate code
        self._teardown()

    # --------------------------------------------------------------------------
    # Private methods
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # Short description
    # --------------------------------------------------------------------------
    def _func(self):
        """
        Short description

        Arguments:
            var_name: Short description

        Returns:
            Description

        Raises:
            exception_type(vars): Description

        Long description (including HTML).
        """

        # change a value in the config dict
        self._dict_cfg["inside"] = "bar"

        # check for debug flag
        if self._debug:
            return "this is func (DEBUG)"

        # no debug, return normal result
        return "this is func"

    # --------------------------------------------------------------------------
    # Boilerplate to use at the start of main
    # --------------------------------------------------------------------------
    def _setup(self):
        """
        Boilerplate to use at the start of main

        Perform some mundane stuff like running the arg parser and loading
        config files.
        """

        # call to set up and run arg parser
        super()._run_parser()

        # get other options from command line
        self._debug = self._dict_args[CNCli.ARG_DBG_DEST]

        # the default config file
        cfg_def = str(DIR_CFG / "__PP_NAME_SMALL__.json")

        # command line cfg is None or str
        cfg_arg = self._dict_args[CNCli.ARG_CFG_DEST]

        # load the config file
        # not using def path, using arg path
        # super()._load_config(None, cfg_arg, self._dict_cfg)
        # using def path, not using arg path
        # super()._load_config(cfg_def, dict_def=self._dict_cfg)
        # using def path, using arg path, using internal
        super()._load_config(
            cfg_def, path_arg=cfg_arg, dict_def=self._dict_cfg
        )

        # throw in a debug test
        if self._debug:
            F.pp(self._dict_cfg, label="load cfg:")

    # --------------------------------------------------------------------------
    # Add arguments to argparse parser
    # --------------------------------------------------------------------------
    def _add_args(self, parser):
        """
        Add arguments to argparse parser

        Arguments:
            parser: The ArgumentParser to add the args to

        This method is teased out for better code maintenance.
        """

        # formatted version
        # pylint: disable=consider-using-f-string
        # pylint: disable=format-string-without-interpolation
        ver_fmt = "__PP_VER_FMT__".format(PB_VERSION)
        # pylint: enable=consider-using-f-string
        # pylint: enable=format-string-without-interpolation

        # about string
        s_about = (
            "__PP_NAME_SMALL__\n"
            "__PP_SHORT_DESC__\n"
            f"{ver_fmt}\n"
            "__PP_URL__/__PP_NAME_BIG__"
        )

        # set help string
        parser.description = s_about

        # add debug option
        parser.add_argument(
            CNCli.ARG_DBG_OPTION,
            action=CNCli.ARG_DBG_ACTION,
            dest=CNCli.ARG_DBG_DEST,
            help=CNCli.ARG_DBG_HELP,
        )

        # add config (user dict) option
        parser.add_argument(
            CNCli.ARG_CFG_OPTION,
            dest=CNCli.ARG_CFG_DEST,
            help=CNCli.ARG_CFG_HELP,
            metavar=CNCli.ARG_CFG_METAVAR,
        )

    # --------------------------------------------------------------------------
    # Boilerplate to use at the end of main
    # --------------------------------------------------------------------------
    def _teardown(self):
        """
        Boilerplate to use at the end of main

        Perform some mundane stuff like saving config files.
        """

        # throw in a debug test
        if self._debug:
            F.pp(self._dict_cfg, label="save cfg:")

        # call to save config
        super()._save_config()


# ------------------------------------------------------------------------------
# Code to run when called from command line
# ------------------------------------------------------------------------------
if __name__ == "__main__":

    # Code to run when called from command line

    # This is the top level code of the program, called when the Python file is
    # invoked from the command line.

    # create a new instance of the main class
    __PP_NAME_CLASS__().main()

# pyplate: disable=replace
S1 = "__PP_NAME_BIG__"
# pyplate: enable=replace

# -)
