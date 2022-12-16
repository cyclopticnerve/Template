#!/usr/bin/env python
# ------------------------------------------------------------------------------
# Project : __CN_BIG_NAME__                                        /          \
# Filename: install.py                                            |     ()     |
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

# define the install settings
dict_install = {
    'general': {
        'name': '__CN_BIG_NAME__'
    },
    'preflight': [
    ],
    'sys_reqs': [
    ],
    'py_reqs': [
    ],
    'dirs': [
        '${HOME}/.cyclopticnerve/__CN_SMALL_NAME__'
    ],
    'files': {
        'LICENSE': '${HOME}/.cyclopticnerve/__CN_SMALL_NAME__',
        'uninstall.py': '${HOME}/cyclopticnerve/.__CN_SMALL_NAME__',
        '__CN_SMALL_NAME__.py': '${HOME}/.cyclopticnerve/__CN_SMALL_NAME__'
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
        Run the Installer module

        Paramaters: none

        Returns: none

        Raises: none

        This is the main installer function, which creates an instance of the
        Installer class and runs it's main function, with the global
        dictionary created above.
    """

    # instantiate installerator class
    installer = installerator.installerator.Installerator()

    # # run the instance
    installer.run(dict_install)


# ------------------------------------------------------------------------------
# Code to run when called from command line
# ------------------------------------------------------------------------------
if __name__ == '__main__':
    main()

# -)
