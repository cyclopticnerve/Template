#!/usr/bin/env python
# ------------------------------------------------------------------------------
# Project : __CN_BIG_NAME__                                        /          \
# Filename: uninstall.py                                          |     ()     |
# Date    : __CN_DATE__                                           |            |
# Author  : cyclopticnerve                                        |   \____/   |
# License : WTFPLv2                                                \          /
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

import installerator

# ------------------------------------------------------------------------------
# Globals
# ------------------------------------------------------------------------------

# define the uninstall settings
dict_uninstall = {
    'general': {
        'name': '__CN_BIG_NAME__'
    },
    'preflight': [
    ],
    'dirs': [
        '${HOME}/.cyclopticnerve/__CN_SMALL_NAME__'
    ],
    'files': {
    },
    'postflight': [
    ]
}


# ------------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Main function
# ------------------------------------------------------------------------------
def main():

    """
        Run the Uninstaller module

        Paramaters: none

        Returns: none

        Raises: none

        This is the main uninstaller function, which creates an instance of the
        Uninstaller class and runs it's main function, with the global
        dictionary created above.
    """

    # instantiate uninstallerator class
    uninstaller = installerator.uninstallerator.Uninstallerator()

    # # run the instance
    uninstaller.run(dict_uninstall)


# ------------------------------------------------------------------------------
# Code to run when called from command line
# ------------------------------------------------------------------------------
if __name__ == '__main__':
    main()

# -)
