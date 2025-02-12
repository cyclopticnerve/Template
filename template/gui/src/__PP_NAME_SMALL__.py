#! /usr/bin/env python
# ------------------------------------------------------------------------------
# Project : __PP_NAME_BIG__                                        /          \
# Filename: __PP_NAME_SMALL__                                     |     ()     |
# Date    : __PP_DATE__                                           |            |
# Author  : __PP_AUTHOR__                                         |   \____/   |
# License : __PP_LICENSE_NAME__                                    \          /
# ------------------------------------------------------------------------------

"""
The main file that runs the program

This file is executable and can be called from the terminal like:

foo@bar:~$ cd [path to directory of this file]
foo@bar:~[path to directory of this file]$ ./__PP_NAME_SMALL__ [cmd line]

or if installed in a global location:

foo@bar:~$ __PP_NAME_SMALL__ [cmd line]

Typical usage is show in the main() method.
"""

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

# system imports
import gettext
import locale
from pathlib import Path
import sys

# find path to prj/lib
P_DIR_PRJ_INST = Path.home() / "__PP_USR_INST__"
P_DIR_PRJ = Path(__file__).parents[1].resolve()

P_DIR_LIB_INST = P_DIR_PRJ_INST / "__PP_DIR_LIB__"
P_DIR_LIB = P_DIR_PRJ / "__PP_DIR_LIB__"

P_DIR_GUI_INST = P_DIR_PRJ_INST / "__PP_DIR_GUI__"
P_DIR_GUI = P_DIR_PRJ / "__PP_DIR_GUI__"

# add paths to import search
sys.path.append(str(P_DIR_LIB_INST))
sys.path.append(str(P_DIR_LIB))
sys.path.append(str(P_DIR_GUI_INST))
sys.path.append(str(P_DIR_GUI))

# pylint: disable=wrong-import-position
# pylint: disable=import-error

# import my stuff
from cnlib import cnfunctions as F  # type: ignore
from cnlib.cncli import CNCli  # type: ignore
from python.__PP_APP_FILE_FMT__ import App  # type: ignore

# pylint: enable=wrong-import-position
# pylint: enable=import-error

# ------------------------------------------------------------------------------
# gettext stuff for CLI
# ------------------------------------------------------------------------------

# to test translations, run as foo@bar:$ LANGUAGE=xx ./__PP_NAME_SMALL__.py
DOMAIN = "__PP_NAME_SMALL__"
if P_DIR_PRJ_INST.exists():
    DIR_LOCALE = P_DIR_PRJ_INST / "__PP_PATH_LOCALE__"
else:
    DIR_LOCALE = P_DIR_PRJ / "__PP_PATH_LOCALE__"
TRANSLATION = gettext.translation(DOMAIN, DIR_LOCALE, fallback=True)
_ = TRANSLATION.gettext

# fix locale (different than gettext stuff, mostly fixes GUI issues, but ok to
# use for CLI in the interest of common code)
locale.bindtextdomain(DOMAIN, DIR_LOCALE)

# ------------------------------------------------------------------------------
# Required for pybaker
# ------------------------------------------------------------------------------

# globals for pb to find
# NB: you may edit these by hand, but they will be overwritten by PyBaker
S_PP_VERSION = "__PP_VERSION__"
# I18N: short description
S_PP_SHORT_DESC = "__PP_SHORT_DESC__"

# ------------------------------------------------------------------------------
# Strings
# ------------------------------------------------------------------------------

# version string
# NB: done in two steps to avoid linter errors
S_VER_FMT = "__PP_VER_FMT__"
S_VER_OUT = S_VER_FMT.format(S_PP_VERSION)

# about string
S_ABOUT = (
    "__PP_NAME_BIG__\n"
    f"{S_PP_SHORT_DESC}\n"
    f"{S_VER_OUT}\n"
    "__PP_URL__/__PP_NAME_BIG__\n"
)

# ------------------------------------------------------------------------------
# Paths
# ------------------------------------------------------------------------------

# path to default config file
P_CFG_DEF = None

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
        app = App(self._dict_args)
        app.run()

        # ----------------------------------------------------------------------
        # teardown

        # call boilerplate code
        self._teardown()

    # --------------------------------------------------------------------------
    # Private methods
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # Boilerplate to use at the start of main
    # --------------------------------------------------------------------------
    def _setup(self):
        """
        Boilerplate to use at the start of main

        Perform some mundane stuff like running the arg parser and loading
        config files.
        """

        # call to super run arg parser
        self._run_parser()

        # print about msg on every run (but only after checking for -h)
        print(S_ABOUT)

        # super load config file (or not, if no param and not using -c)
        # NB: first param is path to us (for rel path)
        # NB: second param is path to def file or none
        parent_dir = Path(__file__).parent.resolve()
        self._load_config(parent_dir, P_CFG_DEF)

        # throw in a debug test
        if self._debug:
            F.pp(self._dict_cfg, label="load cfg")

    # --------------------------------------------------------------------------
    # Add arguments to argparse parser
    # --------------------------------------------------------------------------
    def _add_args(self, parser):
        """
        Add arguments to argparse parser

        Args:
            parser: The ArgumentParser to add the args to

        This method is called by the superclass's _run_parser method, and
        allows subclasses to add their own arguments to the parser.
        """

        # set help string
        parser.description = S_ABOUT

        # add config (user dict) option
        parser.add_argument(
            CNCli.S_ARG_CFG_OPTION,
            dest=CNCli.S_ARG_CFG_DEST,
            help=CNCli.S_ARG_CFG_HELP,
            metavar=CNCli.S_ARG_CFG_METAVAR,
        )

        # add debug option
        parser.add_argument(
            CNCli.S_ARG_DBG_OPTION,
            action=CNCli.S_ARG_DBG_ACTION,
            dest=CNCli.S_ARG_DBG_DEST,
            help=CNCli.S_ARG_DBG_HELP,
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
            F.pp(self._dict_cfg, label="save cfg")

        # call to save config
        self._save_config()


# ------------------------------------------------------------------------------
# Code to run when called from command line
# ------------------------------------------------------------------------------
if __name__ == "__main__":

    # Code to run when called from command line

    # This is the top level code of the program, called when the Python file is
    # invoked from the command line.

    # create a new instance of the main class
    obj = __PP_NAME_CLASS__()

    # run the new object
    obj.main()

# -)
