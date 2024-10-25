# ------------------------------------------------------------------------------
# Project : CNInstall                                              /          \
# Filename: cninstall.py                                          |     ()     |
# Date    : 09/23/2024                                            |            |
# Author  : cyclopticnerve                                        |   \____/   |
# License : WTFPLv2                                                \          /
# ------------------------------------------------------------------------------

"""
The class to use for installing.
"""

# TODO: strings

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

# global imports
import json
from pathlib import Path
import shutil
import sys

# find paths to lib
# NB: this assumes cnlib is a "sister" folder to cnapplib
DIR_CNLIB = Path(__file__).parents[1].resolve()

# add paths to import search
sys.path.append(str(DIR_CNLIB))

# pylint: disable=wrong-import-position
# pylint: disable=wrong-import-order
# pylint: disable=no-name-in-module
# pylint: disable=import-error

# local imports
from cnlib import cnfunctions as F  # type: ignore

# pylint: enable=wrong-import-position
# pylint: enable=wrong-import-order
# pylint: enable=no-name-in-module
# pylint: enable=import-error

# ------------------------------------------------------------------------------
# Define the classes
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# A class to wrap errors from the install/uninstall methods
# ------------------------------------------------------------------------------
# class CNInstallError(Exception):
#     """
#     A class to wrap errors from the install/uninstall methods

#     Arguments:
#         e: the original exception

#     This class is used to wrap exceptions from the install/uninstall methods,
#     so that a file that uses install/uninstall does not need to import or check
#     for all possible failures. The original exception and its properties will
#     be exposed by the 'exception' property, but printing will defer to the
#     original exception's __repr__ property.
#     """

#     def __init__(self, exception, message):
#         self.exception = exception
#         self.message = message
#         self.__repr__ = self.exception.__repr__

# ------------------------------------------------------------------------------
# Define the main class
# ------------------------------------------------------------------------------
class CNInstall:
    """
    The class to use for installing.
    """

    # --------------------------------------------------------------------------
    # Public methods
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # Initialize the class
    # --------------------------------------------------------------------------
    def __init__(self, debug=False):

        """
        The default initialization of the class

        Public methods:
            run_file:
            run_dict:
        Creates a new instance of the class and set initial properties.
        """

        # default conf dict
        self._dict_conf = {}

        # set conf dict
        # TODO: catch exc
        # with open(path_conf, "r", encoding="utf8") as a_file:
        #     self._dict_conf = json.load(a_file)

        # the dir where the install.py is being run
        # self._dir_assets = dir_assets
        # set debug prop
        self._debug = debug

    # --------------------------------------------------------------------------
    # Run the install process using a file path
    # --------------------------------------------------------------------------
    def run_file(self, a_file):
        """
        Run the install process using a file path

        Arguments:
            a_file: File containing ONLY the install dict

        Raises:
            FileNotFoundError: If the file could not be found
            json.JSONDecodeError: If the file is not a valid JSON file

        Runs the installer using a file path, which must ONLY contain the
        install dict.
        """

        # set conf dict
        try:
            with open(a_file, "r", encoding="utf8") as a_file:
                a_dict = json.load(a_file)
                self.run_dict(a_dict)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Install file could not be found or is not a JSON file")
            sys.exit(-1)

    # --------------------------------------------------------------------------
    # Run the install process using a dict
    # --------------------------------------------------------------------------
    def run_dict(self, a_dict):
        """
        Run the install process using a dict

        Arguments:
            a_dict: Dictionary to use for install information

        This method is the main function of the class. It performs the
        various steps required to install a python program, and should be
        the only method called by your install.py file.
        """

        # set dict property
        self._dict_conf = a_dict

        # check if pip necessary
        sys_reqs = self._dict_conf.get("sys_reqs", [])
        py_reqs = self._dict_conf.get("py_reqs", [])
        if py_reqs and len(py_reqs):
            sys_reqs.append("python3-pip")

        # check if we need sudo password
        if len(sys_reqs) or len(py_reqs):
            cmd = "sudo echo -n"
            # TODO: check for error
            F.sh(cmd)

        # show some text
        prog_name = self._dict_conf["meta"]["name"]
        prog_version = self._dict_conf["meta"]["version"]

        # TODO: check for version number? needs to be stored on user's comp
        # somewhere
        # don't install older version

        print(f"Installing {prog_name} version {prog_version}")

        # do each part of conf dict
        self._run_scripts("preflight")
        self._do_sys_reqs()
        self._do_py_reqs()
        self._do_content()
        self._run_scripts("postflight")

        # done installing
        print(f"{prog_name} installed")

    # --------------------------------------------------------------------------
    # Install system requirements
    # --------------------------------------------------------------------------
    def _do_sys_reqs(self):
        """
        Install system requirements

        This method uses the conf dict to install any system requirements
        (i.e. non-python packages) necessary to run your program.
        """

        # check for empty/no list
        items = self._dict_conf.get("sys_reqs", None)
        if not items or len(items) == 0:
            return

        # show some text
        print("Installing system requirements")

        # get system requirements
        for item in items:

            # show that we are doing something
            print(f"Installing {item}... ", end="")

            # install apt reqs
            if not self._debug:
                cmd = f"sudo apt-get install {item} -qq > /dev/null"
                F.sh(cmd)

            # done
            print("Done")

    # --------------------------------------------------------------------------
    # Install Python requirements
    # --------------------------------------------------------------------------
    def _do_py_reqs(self):
        """
        Install Python requirements

        This method uses the conf dict to install any python requirements
        (i.e. installed with pip) necessary to run your program.
        """

        # check for empty/no list
        items = self._dict_conf.get("py_reqs", None)
        if not items or len(items) == 0:
            return

        # show some text
        print("Installing Python requirements")

        # get python requirements
        for item in items:

            # show that we are doing something
            print(f"Installing {item}... ", end="")

            # install pip reqs
            if not self._debug:
                cmd = f"python -m pip install -q {item} > /dev/null"
                F.sh(cmd)

            # done
            print("Done")

    # --------------------------------------------------------------------------
    # Copy source files/folders
    # --------------------------------------------------------------------------
    def _do_content(self):
        """
        Copy source files/folders

        This method copies files and folders from the assets folder of the
        source to their final locations in the user's folder structure.
        """

        # get source dir and user home
        inst_src = Path(self._dir_assets)
        inst_home = Path.home()

        # content list from dict
        content = self._dict_conf.get("content", None)
        if not content:
            return

        # for each key, value
        for k, v in content.items():

            # get full paths of source / destination
            src = inst_src / k
            dst = inst_home / v

            # if the source is a dir
            if src.is_dir():
                if not self._debug:
                    # copy dir
                    shutil.copytree(src, dst, dirs_exist_ok=True)
                else:
                    print(f"copytree {src} to {dst}")

            # if the source is a file
            else:
                if not self._debug:
                    # copy file
                    # TODO: make sure the dst dir exists
                    shutil.copy2(src, dst)
                else:
                    print(f"copy2 {src} to {dst}")

    # --------------------------------------------------------------------------
    # Run preflight/postflight scripts
    # --------------------------------------------------------------------------
    def _run_scripts(self, step):

        """
        Runs the scripts from preflight or postflight

        Arguments:
            step [str]: The step to run, either preflight or postflight

        This method is the common code for running preflight/postflight
        scripts. It takes the step (specified by the key name) and runs the
        scripts in the order they are specified.
        """

        # check for empty/no list
        # if not self._needs_step(step):
        #     return

        # check for empty/no list
        items = self._dict_conf.get(step, None)
        if not items or len(items) == 0:
            return

        # show some text
        print(f'Running {step} scripts... ', end="")

        for item in self._dict_conf[step]:

            # show that we are doing something
            # print(f'install running {item}... ', end='')

            # TODO: except
            # get item as cmd line array
            if not self._debug:
                F.sh(item)

            # done
            print("Done")

    # --------------------------------------------------------------------------
    # Run the script
    # --------------------------------------------------------------------------
    # def run(self, dict_user):
    #     """
    #     Runs the setup using the supplied user dictionary

    #     Arguments:
    #         dict_user [dict]: the user dict to get options from

    #     This method takes the user dictionary and does some housekeeping,
    #     such as creating the substitution directory. It also uses
    #     configurator to merge the default and user dicts and apply the
    #     substitutions.
    #     """

    # the defs dict
    # dict_defs = {
    #     "general": {"name": ""},
    #     "preflight": [],
    #     "sys_reqs": [],
    #     "py_reqs": [],
    #     "dirs": [],
    #     "files": {},
    #     "postflight": [],
    # }

    # get current user's home dir
    # home_dir = os.path.expanduser("~")

    # # get location
    # src_dir = os.path.dirname(os.path.abspath(__file__))

    # # the default dict of substitutions
    # dict_subs = {"${HOME}": home_dir, "${SRC}": src_dir}

    # do the config merge
    # NB: allow_user_extras is here for the 'files' section, which will have
    # keys (filenames) we don't know about yet
    # self.dict_conf = configurator.load(
    #     dict_defs, dict_user, dict_subs, allow_user_extras=True
    # )
    # self._dict_conf = dict_user

    # --------------------------------------------------------------------------
    # Private methods
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # Run preflight scripts
    # --------------------------------------------------------------------------
    # def _do_preflight(self):

    #     """
    #         Run preflight scripts (before we do the heavy lifting)

    #         This method runs any scripts specified in the preflight section of
    #         the user dict, in the order they are specified.
    #     """

    #     # run preflight scripts
    #     self._run_scripts('preflight')

    # --------------------------------------------------------------------------
    # Run postflight scripts
    # --------------------------------------------------------------------------
    # def _do_postflight(self):

    #     """
    #         Run postflight scripts (after we do the heavy lifting)

    #         This method runs any scripts specified in the postflight section of
    #         the user dict, in the order they are specified.
    #     """

    #     # run postflight scripts
    #     self._run_scripts('postflight')

    # --------------------------------------------------------------------------
    # Check if we are going to need sudo password and get it now
    # --------------------------------------------------------------------------
    # def _check_sudo(self):

    #     """
    #         Checks if we need sudo permission early in the install

    #         Returns:
    #             [bool]: True if we need sudo permission, False if we don't

    #         This method is used to check if we will need sudo (for sys_reqs or
    #         py_reqs) and ask for the sudo password early in the install process.
    #         This gives a better visual appearance to the process.
    #     """

    # if either of theses steps is required, we need sudo
    # if self._needs_step('sys_reqs') or self._needs_step('py_reqs'):

    #     # ask for sudo password now (no try block 'cause f*** it)
    #     cmd = 'sudo echo -n'
    #     cmd_array = shlex.split(cmd)
    #     subprocess.run(cmd_array, check=True)

    # --------------------------------------------------------------------------
    # Check if a step needs to be performed or can be skipped
    # --------------------------------------------------------------------------
    # def _needs_step(self, step):

    #     """
    #     Check if an entry in the defs/user needs to be run

    #     Arguments:
    #         step [str]: the step to check for in the final dict

    #     Returns:
    #         [bool]:True if the dict contains the step, False otherwise

    #     This method checks to see if a step (specified by the key name) is
    #     needed, or if the value is empty. This saves us from printing info
    #     about a step that will not actually be performed (such as not having
    #     any preflight scripts to run, etc.).
    #     """

    #     # if the section is present
    #     if step in self._dict_conf:

    #         # if there are entries in the section
    #         step_conf = self._dict_conf[step]
    #         if len(step_conf):
    #             return True

    #     # otherwise we can skip this step
    #     return False

# -)
