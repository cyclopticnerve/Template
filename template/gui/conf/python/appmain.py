# ------------------------------------------------------------------------------
# Project : PyPlate                                                /          \
# Filename: appmain.py                                            |     ()     |
# Date    : 12/08/2022                                            |            |
# Author  : cyclopticnerve                                        |   \____/   |
# License : WTFPLv2                                                \          /
# ------------------------------------------------------------------------------

"""
A class to manage a specific Application.

This class manages the more advanced functions of an application, such as
specific windows and system events.
The purpose of this module is to offload as much GUI-specific code as possible
from the main script, so that the main script remains as close to a CLI as
possible.
"""

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

# system imports
from pathlib import Path
import sys

# find paths to dev or user
DIR_PARENT = Path(__file__).parents[1].resolve()
if DIR_PARENT.name == "src":
    DIR_PRJ = DIR_PARENT.parent
    DIR_CFG = DIR_PRJ / "src/support/conf"
    DIR_LIB = Path.home() / "Documents/Projects/Python/PyPlate" / "lib"
    DIR_SRC = DIR_PRJ / "src" / "support"
else:
    DIR_HOME = Path.home()
    DIR_CFG = DIR_HOME / ".config/pyplate"
    DIR_LIB = DIR_HOME / ".local/share/cyclopticnerve/lib"
    DIR_SRC = DIR_HOME / ".local/share/pyplate"

# add paths to import search
sys.path.append(str(DIR_LIB))
sys.path.append(str(DIR_SRC))

# pylint: disable=wrong-import-position
# pylint: disable=wrong-import-order
# pylint: disable=no-name-in-module
# pylint: disable=import-error

# my imports
from cnapplib.cnapp import CNApp  # type: ignore
from windowmain import WindowMain

# pylint: enable=wrong-import-position
# pylint: enable=wrong-import-order
# pylint: enable=no-name-in-module
# pylint: enable=import-error

# ------------------------------------------------------------------------------
# Classes
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# The main file that runs the gui application
# ------------------------------------------------------------------------------
class AppMain(CNApp):
    """
    The main file that runs the gui application

    This script is called from the main script and should not be called
    directly. The purpose of this script is to offload as much GUI-specific
    code as possible from the main script, so that the main script remains as
    close to a CLI as possible.
    """

    # --------------------------------------------------------------------------
    # Class methods
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # Initialize the new object
    # --------------------------------------------------------------------------
    def __init__(self, dict_args=None):
        """
        Initialize the new object

        Arguments:
            dict_args: The arguments passed to the calling CLI script

        Initializes a new instance of the class, setting the default values of
        its properties, and any other code needed to create a new object.
        """

        # NB: do something with args
        if dict_args is None:
            dict_args = {}
        self._dict_args = dict_args

        # app props
        app_id = "org.cyclopticnerve.pyplate"
        name_win = "default_window"

        # call super with our custom args
        super().__init__(app_id)

        # create an instance of a window
        inst_win = WindowMain(self, name_win)

        # add a window to the app
        super().add_window(name_win, inst_win)


# -)
