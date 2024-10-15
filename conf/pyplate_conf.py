# ------------------------------------------------------------------------------
# Project : PyPlate                                                /          \
# Filename: pymaker_conf.py                                       |     ()     |
# Date    : 12/08/2022                                            |            |
# Author  : cyclopticnerve                                        |   \____/   |
# License : WTFPLv2                                                \          /
# ------------------------------------------------------------------------------

# pylint: disable=too-many-lines

"""
This module separates out the constants from pymaker.py.
This file, and the template folder, are the main ways to customize PyPlate.
"""

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

# system imports
from pathlib import Path
import re

# ------------------------------------------------------------------------------
# Bools
# ------------------------------------------------------------------------------

# create a tree and save it to S_TREE_FILE
B_CMD_TREE = True
# create a git using S_CMD_GIT
B_CMD_GIT = True
# create a venv using S_VENV_CMD_CREATE
B_CMD_VENV = True
# create docs
B_CMD_DOCS = True

# ------------------------------------------------------------------------------
# Integers
# ------------------------------------------------------------------------------

# values for line switches
I_SW_NONE = -1
I_SW_TRUE = 1
I_SW_FALSE = 0

# ------------------------------------------------------------------------------
# Strings
# ------------------------------------------------------------------------------

# base dir for project type folders, relative to dev home
S_DIR_PRJ_BASE = "Documents/Projects/Python"

# date format
S_DATE_FMT = "%m/%d/%Y"

# NB: format params are keys in L_TYPES[0] and L_TYPES[1]
S_TYPE_FMT = "{} ({})"
# join each project type with this
S_TYPE_JOIN = " | "

# NB: format param is joined list of project types
S_ASK_TYPE = "Project type [{}]: "
S_ASK_NAME = "Project name: "
S_ASK_DESC = "Short description: "
# NB: format params are D_TYPE_SEC[prj_type], __PP_NAME_SMALL__
S_ASK_SEC = "{} name (default: {}): "

# error strings
S_ERR_TYPE = "Type must be one of {}"
S_ERR_LEN = "Project names must be more than 1 character"
S_ERR_START = "Project names must start with a letter"
S_ERR_END = "Project names must end with a letter or number"
S_ERR_MID = (
    "Project names must contain only letters, numbers,"
    "dashes (-), or underscores (_)"
)
# NB: format param arise dir_type/(proj type dir)
S_ERR_EXIST = 'Project "{}" already exists'

# debug-specific strings
S_ERR_DEBUG = (
    "\n"
    "WARNING! YOU ARE IN DEBUG MODE!\n"
    "IT IS POSSIBLE TO OVERWRITE EXISTING PROJECTS!\n"
)

# TODO: which keys need to be global/which are only used once?
# keys for pybaker private dict
S_KEY_PRV_ALL = "PRV_ALL"
# S_KEY_PRV_EXTRA = "PRV_EXTRA"
S_KEY_PRV_PRJ = "PRV_PRJ"

# keys for metadata, blacklist, i18n in pybaker dev dict
S_KEY_PUB_META = "PUB_META"
S_KEY_PUB_BL = "PUB_BL"
S_KEY_PUB_I18N = "PUB_I18N"
S_KEY_PUB_INSTALL = "PUB_INSTALL"

# keys for blacklist
S_KEY_SKIP_ALL = "SKIP_ALL"
S_KEY_SKIP_CONTENTS = "SKIP_CONTENTS"
S_KEY_SKIP_HEADER = "SKIP_HEADER"
S_KEY_SKIP_CODE = "SKIP_CODE"
S_KEY_SKIP_PATH = "SKIP_PATH"
S_KEY_SKIP_TREE = "SKIP_TREE"

# keys for i18n
S_KEY_CHARSET = "CHARSET"
S_KEY_TYPES = "TYPES"
S_KEY_CLANGS = "CLANGS"
S_KEY_NO_EXT = "NO_EXT"
S_KEY_LOCALE = "LOCALE"
S_KEY_PO = "PO"

# python header/split dict keys
S_KEY_HDR = "S_KEY_HDR"
S_KEY_LEAD = "S_KEY_GRP_LEAD"
S_KEY_VAL = "S_KEY_GRP_VAL"
S_KEY_PAD = "S_KEY_GRP_PAD"
S_KEY_SWITCH = "S_KEY_SWITCH"
S_KEY_COMM = "S_KEY_COMM"
S_KEY_SPLIT = "S_KEY_SPLIT"
S_KEY_SPLIT_INDEX = "S_KEY_SPLIT_INDEX"

S_KEY_NAME_START = "S_KEY_NAME_START"
S_KEY_NAME_END = "S_KEY_NAME_END"
S_KEY_NAME_MID = "S_KEY_NAME_MID"

# dir names, relative to PP template, or project dir
# NB: if you change anything in the template structure, you should revisit this
# and make any appropriate changes
# also make sure that these names don't appear in the blacklist, or else
# pymaker won't touch them
S_DIR_TEMPLATE = "template"
S_DIR_ALL = "all"
S_DIR_GIT = ".git"
S_DIR_CONF = "conf"
S_DIR_DIST = "dist"
S_DIR_ASSETS = "assets"
S_DIR_DOCS = "docs"
S_DIR_MISC = "misc"
S_DIR_README = "readme"
S_DIR_SRC = "src"
S_DIR_SUPPORT = "support"
S_DIR_DESKTOP = "desktop"
S_DIR_UI = "ui"
S_DIR_I18N = "i18n"
S_DIR_IMAGES = "images"
S_DIR_LOCALE = "locale"
S_DIR_PO = "po"
S_DIR_TESTS = "tests"

# common file names, rel to prj dir or pyplate dir
S_FILE_LICENSE = "LICENSE.txt"
S_FILE_README = "README.md"
S_FILE_TOML = "pyproject.toml"
S_FILE_REQS = "requirements.txt"
S_FILE_INSTALL = f"{S_DIR_CONF}/install.json"

# initial location of project (to check for dups)
# /home/<dev>/<S_DIR_PRJ_BASE>/<prj_type>/<prj_name>
# NB: format params are project type and project name
S_DIR_BASE = str(Path.home() / S_DIR_PRJ_BASE)
S_DIR_PRJ = S_DIR_BASE + "/{}/{}"

# paths relative to end user home only
S_USR_CONF = ".config"  # __PP_NAME_SMALL__ will be appended
S_USR_SRC = ".local/share"  # __PP_NAME_SMALL__ will be appended
S_USR_APPS = ".local/share/applications"  # for .desktop file
S_USR_BIN = ".local/bin"  # where to put the binary

# this is where the user libs will go
S_USR_LIB_NAME = "lib"
S_USR_LIB = ".local/share"  # __PP_AUTHOR__/S_USR_LIB_NAME will be appended

# cmds for docs
S_CMD_DOCS = "python -m pdoc --html -f -o {} ."

# formats for tree
S_TREE_NAME = "tree.txt"
S_TREE_FILE = f"{S_DIR_MISC}/{S_TREE_NAME}"
S_TREE_DIR_FORMAT = " [] $NAME/"
S_TREE_FILE_FORMAT = " [] $NAME"

# switch constants
S_SW_ENABLE = "enable"
S_SW_DISABLE = "disable"
S_SW_REPLACE = "replace"

# path to prj pyplate files, relative to prj dir
# NB: leave as string, no start dir yet
S_PRJ_PP_DIR = "pyplate"
S_PRJ_PUB_CFG = f"{S_PRJ_PP_DIR}/project.json"
S_PRJ_PRV_DIR = f"{S_PRJ_PP_DIR}/private"
S_PRJ_PRV_CFG = f"{S_PRJ_PRV_DIR}/private.json"

# ------------------------------------------------------------------------------
# commands for _do_extras

# cmds for git
# NB: format param is proj dir
S_CMD_GIT = "git init {} -q"

# cmds for venv
# NB: format param is __PP_NAME_SMALL__
S_VENV_FMT_NAME = ".venv-{}"
# NB: path to venv create/install/freeze scripts for venv, relative to prj dir
# NB: format param is __PP_NAME_VENV__
S_VENV_CREATE = f"{S_PRJ_PRV_DIR}/venv/venv_create.sh" " {}"
S_VENV_INSTALL = f"{S_PRJ_PRV_DIR}/venv/venv_install.sh"
S_VENV_FREEZE = f"{S_PRJ_PRV_DIR}/venv/venv_freeze.sh"

# path to docs script
S_DOCS_SCRIPT = f"{S_PRJ_PRV_DIR}/docs.sh"

# ------------------------------------------------------------------------------
# pybaker stuff

S_ERR_PRJ_DIR_NO_EXIST = "Project dir {} does not exist"
S_ERR_PRJ_DIR_NONE = "Project dir not provided"

S_CHANGELOG = "CHANGELOG.md"
S_CHANGELOG_CMD = f"git log --pretty='%ad - %s' > {S_CHANGELOG}"

S_TOML_VERSION_SEARCH = (
    r"(^\s*\[project\]\s*$)(.*?)(^\s*version[\t ]*=[\t ]*)(.*?$)"
)
S_TOML_VERSION_REPL = r'\g<1>\g<2>\g<3>"{}"'
S_TOML_SHORT_DESC_SEARCH = (
    r"(^\s*\[project\]\s*$)(.*?)(^\s*description[\t ]*=[\t ]*)(.*?$)"
)
S_TOML_SHORT_DESC_REPL = r'\g<1>\g<2>\g<3>"{}"'
S_TOML_KW_SEARCH = (
    r"(^\s*\[project\]\s*$)(.*?)(^\s*keywords[\t ]*=[\t ]*)(.*?\])"
)
S_TOML_KW_REPL = r"\g<1>\g<2>\g<3>[{}]"

S_META_VER_SEARCH = r"(\s*S_PP_VERSION\s*=\s*)(.*)"
S_META_VER_REPL = r'\g<1>"{}"'
S_META_SD_SEARCH = r"(\s*S_PP_SHORT_DESC\s*=\s*)(.*)"
S_META_SD_REPL = r'\g<1>"{}"'

# S_ERR_COUNT = "Errors: {}"
# S_ERR_UFNF = "ERROR: File {} could not be found, trying default"
# S_ERR_UJSON = "ERROR: FIle {} is not a valid JSON file, trying default"
# S_ERR_DFNF = "ERROR: Default file {} could not be found"
# S_ERR_DJSON = "ERROR: Default file {} is not a valid JSON file"

# ------------------------------------------------------------------------------
# Lists
# ------------------------------------------------------------------------------

# the types of projects this script can create
# val[0] is the char to enter (short, display only)
# val[1] is the display name in the cli (long, display only)
# val[2] is the template folder to use (template/subdir)
# val[3] is the name of the folder under S_DIR_PRJ_BASE in which to place the
# project (prj_dir)
L_TYPES = [
    ["c", "CLI", "cli", "CLIs"],
    ["g", "GUI", "gui", "GUIs"],
    ["p", "PKG", "pkg", "PKGs"],
]

# list of file types to use md/html/xml fixer
L_MARKUP = [
    ".md",
    ".html",
    ".xml",
    ".ui",
    ".glade",
]

# file exts for pybaker
L_DESKTOP = [".desktop"]
L_GTK = [".ui", ".glade"]

# files to remove after the project is done
# paths are relative to project dir
L_PURGE = [
    Path(S_DIR_SRC) / "ABOUT",
]

# folders to put in dist
# TODO: should this be per-project?
L_DIST = [
    "conf",
    "readme",
    S_DIR_SRC,
    "lib",
    "CHANGELOG.md",
    "LICENSE.txt",
    "README.md",
]

# get list of approved categories
# https://specifications.freedesktop.org/menu-spec/latest/apa.html
L_CATS = [
    "AudioVideo",
    "Audio",
    "Video",
    "Development",
    "Education",
    "Game",
    "Graphics",
    "Network",
    "Office",
    "Science",
    "Settings",
    "System",
    "Utility",
    "Building",
    "Debugger",
    "IDE",
    "GUIDesigner",
    "Profiling",
    "RevisionControl",
    "Translation",
    "Calendar",
    "ContactManagement",
    "Database",
    "Dictionary",
    "Chart",
    "Email",
    "Finance",
    "FlowChart",
    "PDA",
    "ProjectManagement",
    "Presentation",
    "Spreadsheet",
    "WordProcessor",
    "2DGraphics",
    "VectorGraphics",
    "RasterGraphics",
    "3DGraphics",
    "Scanning",
    "OCR",
    "Photography",
    "Publishing",
    "Viewer",
    "TextTools",
    "DesktopSettings",
    "HardwareSettings",
    "Printing",
    "PackageManager",
    "Dialup",
    "InstantMessaging",
    "Chat",
    "IRCClient",
    "Feed",
    "FileTransfer",
    "HamRadio",
    "News",
    "P2P",
    "RemoteAccess",
    "Telephony",
    "TelephonyTools",
    "VideoConference",
    "WebBrowser",
    "WebDevelopment",
    "Midi",
    "Mixer",
    "Sequencer",
    "Tuner",
    "TV",
    "AudioVideoEditing",
    "Player",
    "Recorder",
    "DiscBurning",
    "ActionGame",
    "AdventureGame",
    "ArcadeGame",
    "BoardGame",
    "BlocksGame",
    "CardGame",
    "KidsGame",
    "LogicGame",
    "RolePlaying",
    "Shooter",
    "Simulation",
    "SportsGame",
    "StrategyGame",
    "Art",
    "Construction",
    "Music",
    "Languages",
    "ArtificialIntelligence",
    "Astronomy",
    "Biology",
    "Chemistry",
    "ComputerScience",
    "DataVisualization",
    "Economy",
    "Electricity",
    "Geography",
    "Geology",
    "Geoscience",
    "History",
    "Humanities",
    "ImageProcessing",
    "Literature",
    "Maps",
    "Math",
    "NumericalAnalysis",
    "MedicalSoftware",
    "Physics",
    "Robotics",
    "Spirituality",
    "Sports",
    "ParallelComputing",
    "Amusement",
    "Archiving",
    "Compression",
    "Electronics",
    "Emulator",
    "Engineering",
    "FileTools",
    "FileManager",
    "TerminalEmulator",
    "Filesystem",
    "Monitor",
    "Security",
    "Accessibility",
    "Calculator",
    "Clock",
    "TextEditor",
    "Documentation",
    "Adult",
    "Core",
    "KDE",
    "GNOME",
    "XFCE",
    "DDE",
    "GTK",
    "Qt",
    "Motif",
    "Java",
    "ConsoleOnly",
    "Screensaver",
    "TrayIcon",
    "Applet",
    "Shell",
]

# ------------------------------------------------------------------------------
# Dictionaries
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Private dictionaries
# ------------------------------------------------------------------------------

# these are the settings that should be set before you run pymaker.py
# consider them the "all projects" settings
# they are used for all projects, and should not be changed after a project is
# created, as pybaker.py will not update them

# if you need to adjust any of these values in a function, use do_before_fix()
# in this file

D_PRV_ALL = {
    # the author name, used in headers and pyproject.toml
    "__PP_AUTHOR__": "cyclopticnerve",
    # the base url for all projects, used in pyproject.toml and GUI about dlg
    "__PP_URL__": "https://github.com/cyclopticnerve",
    # the author's email, used in headers and pyproject.toml
    "__PP_EMAIL__": "cyclopticnerve@gmail.com",
    # the license name, used in headers and pyproject.toml
    "__PP_LICENSE_NAME__": "WTFPLv2",
    # the license image/link to use in __PP_README_FILE__
    "__PP_RM_LICENSE__": (
        "[!"
        "[License: WTFPLv2]"
        "(https://img.shields.io/badge/License-WTFPL-brightgreen.svg "
        '"http://www.wtfpl.net")'
        "]"
        "(http://www.wtfpl.net)"
    ),
    # dummy value to use in headers
    "__PP_DUMMY__": "",
    # docs folder
    "__PP_NAME_DOCS__": S_DIR_DOCS,
    # version format string for command line
    # NB: format param is __PP_VERSION__ from metadata
    "__PP_VER_FMT__": "Version {}",
    # NB: the struggle here is that using the fixed format results in a
    # four-digit year, but using the locale format ('%x') results in a
    # two-digit year (at least for my locale, which in 'en_US'). so what to do?
    # what i really want is a locale format that uses four-digit years
    # everywhere. so i am faced with a 'cake and eat it too' situation. not
    # sure how to proceed but i think for now i will leave this as a
    # user-editable string and place it in the realm of 'edit it before you
    # run' along with author/email/license/etc
    "__PP_DATE_FMT__": S_DATE_FMT,
    # file names replaced in various places, rel to prj dir
    "__PP_LICENSE_FILE__": S_FILE_LICENSE,
    "__PP_README_FILE__": S_FILE_README,
    "__PP_TOML_FILE__": S_FILE_TOML,
    "__PP_REQS_FILE__": S_FILE_REQS,
    "__PP_INST_FILE__": S_FILE_INSTALL,
    # --------------------------------------------------------------------------
    # these paths are relative to the dev's home/S_BASE_DIR/prj type/prj name
    # i.e. ~_/Documents/Projects/Python/CLIs/MyProject
    # location of src files
    "__PP_DEV_SRC__": S_DIR_SRC,
    # location of config files
    "__PP_DEV_CONF__": f"{S_DIR_SUPPORT}/{S_DIR_CONF}",
    # --------------------------------------------------------------------------
    # these paths are relative to the user's home dir
    "__PP_USR_APPS__": S_USR_APPS,  # for .desktop file
    "__PP_USR_BIN__": S_USR_BIN,  # where to put the binary
    "__PP_SUPPORT__": S_DIR_SUPPORT,  # where is rest of code
    "__PP_IMAGES__": S_DIR_IMAGES,  # where gui images are stored
}

# these are settings that will be calculated for you while running pymaker.py
# consider them the "each project" settings
# they are used for an individual project, and should not be changed after a
# project is created, as pybaker.py will not update them
D_PRV_PRJ = {
    "__PP_TYPE_PRJ__": "",  # 'c'
    "__PP_NAME_BIG__": "",  # PyPlate
    "__PP_NAME_SMALL__": "",  # pyplate
    "__PP_NAME_SEC__": "",  # module1.py
    "__PP_NAME_CLASS__": "",  # Pascal case name for classes
    "__PP_DATE__": "",  # the date each file was created, updated every time
    "__PP_NAME_VENV__": "",  # venv folder name
    # --------------------------------------------------------------------------
    # these paths are calculated at runtime relative to the dev's home dir
    "__PP_DEV_PP__": "",  # location of PyPlate src dir, rel to dev home
    # --------------------------------------------------------------------------
    # these paths are calculated in do_before_fix, relative to the user's home
    # dir
    "__PP_USR_CONF__": "",  # config dir
    "__PP_USR_LIB__": "",  # location of cnlibs dir
    "__PP_USR_SRC__": "",  # where the program will keep it's source
    # --------------------------------------------------------------------------
    # these strings are calculated in do_before_fix
    # NB: technically this should be metadata but we don't want dev editing,
    # only use metadata to recalculate these on every build
    "__PP_KW_STR__": "",  # fix up keywords list for pyproject.toml
    "__PP_RM_DEPS__": "",  # fix up deps for README.md
}

# ------------------------------------------------------------------------------
# Public dictionaries
# ------------------------------------------------------------------------------

# these are settings that will be changed before running pybaker.py
# consider them the "each build" settings
D_PUB_META = {
    # the version number to use in __PP_README_FILE__ and pyproject.toml
    "__PP_VERSION__": "0.0.0",
    # the short description to use in __PP_README_FILE__ and pyproject.toml
    "__PP_SHORT_DESC__": "Short description",
    # the keywords to use in pyproject.toml and github
    "__PP_KEYWORDS__": [],
    # the python dependencies to use in __PP_README_FILE__, pyproject.toml,
    # github, and install.py
    # key is dep name, val is link to dep (optional)
    "__PP_PY_DEPS__": {},
    # the system dependencies to use in __PP_README_FILE__, github.com, and
    # install.py
    # key is dep name, val is link to dep (optional)
    "__PP_SYS_DEPS__": {},
    # the categories to use in .desktop for gui apps (found in pybaker_conf.py)
    "__PP_GUI_CATS__": [],
}

# the lists of dirs/files we don't mess with while running pymaker
# each item can be a full path, a path relative to the project directory, or a
# glob
# see https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob
# NB: you can use dunders here since the path is the last thing to get fixed
# these dir/file names should match what's in the template dir (before any
# modifications, hence using dunder keys)
D_PUB_BL = {
    # skip header, skip text, skip path (0 0 0)
    # NB: this is mostly to speed up processing by not even looking at them
    S_KEY_SKIP_ALL: [
        ".git",
        "**/.venv*",
        # NB: tasks.json needs dunders
        # ".vscode",
        ".VSCodeCounter",
        # NB: dist will have install.py in it, needs dunders
        # S_DIR_DIST,
        S_DIR_DOCS,
        f"**/{S_DIR_LOCALE}",
        f"**/{S_DIR_PO}",
        S_DIR_MISC,
        S_DIR_README,
        S_FILE_LICENSE,
        S_FILE_REQS,
        "**/__pycache__",
        "**/*.mo",
    ],
    # skip header, skip text, fix path (0 0 1)
    # NB: this is used mostly for non-text files
    S_KEY_SKIP_CONTENTS: [
        "**/*.png",
        "**/*.jpg",
        "**/*.jpeg",
    ],
    # skip header, fix text, fix path (0 1 1)
    # NB: not sure what this is useful for, but here it is
    S_KEY_SKIP_HEADER: [],
    # fix header, skip text, fix path (1 0 1)
    # NB: mostly used for files that contain dunders that will be replaced
    # later or files we only want to replace headers in
    S_KEY_SKIP_CODE: [
        "MANIFEST.in",
        ".gitignore",
        "CHANGELOG.md",
    ],
    # fix header, fix text, skip path (1 1 0)
    # NB: not really useful, since we always want to fix paths with dunders,
    # but included for completeness
    S_KEY_SKIP_PATH: [],
    # list of dirs/files to ignore in output dir when creating the initial tree
    # NB: each item can be a partial path relative to the project directory, or
    # a glob
    S_KEY_SKIP_TREE: [
        ".git",
        "**/.venv*",
        # ".vscode",
        ".VSCodeCounter",
        "**/__pycache__",
    ],
}

# I18N stuff to be used in pybaker
D_PUB_I18N = {
    # default charset for .pot/.po files
    S_KEY_CHARSET: "UTF-8",
    # the types of projects that will have i18n applied
    S_KEY_TYPES: ["g"],
    # computer languages
    S_KEY_CLANGS: {
        "Python": [
            "py",
        ],
        "Glade": [
            ".ui",
            ".glade",
        ],
        "Desktop": [".desktop"],
    },
    # dict of clangs and no exts (ie file names)
    S_KEY_NO_EXT: {
        "Python": [
            "__PP_NAME_SMALL__",
        ],
    },
    S_KEY_LOCALE: S_DIR_LOCALE,
    S_KEY_PO: S_DIR_PO,
}

# dict for install script
D_PUB_INST = {
    "meta": {"name": "__PP_NAME_BIG__", "version": "__PP_VERSION__"},
    "preflight": [],
    "sys_reqs": [],
    "py_reqs": [],
    "content": {},
    "postflight": [],
}

# ------------------------------------------------------------------------------
# Other dictionaries
# ------------------------------------------------------------------------------

# dict of files that should be copied from the PyPlate project to the resulting
# project (outside of the template dir)
# this is so that when you update a file in the PyPlate project, it gets copied
# to the project, and cuts down on duplicate files
# key is the relative path to the source file in PyPlate
# val is the relative path to the dest file in the project dir
D_COPY = {
    "lib": "lib",
    f"{S_DIR_MISC}/cnlibs.py": f"{S_DIR_MISC}/cnlibs.py",
    f"{S_DIR_MISC}/default_class.py": f"{S_DIR_MISC}/default_class.py",
    f"{S_DIR_MISC}/default_mod.py": f"{S_DIR_MISC}/default_mod.py",
    f"{S_DIR_MISC}/snippets.txt": f"{S_DIR_MISC}/snippets.txt",
    f"{S_DIR_MISC}/style.txt": f"{S_DIR_MISC}/style.txt",
}

# the info for matching/fixing lines in markup files
D_MU_REPL = {
    S_KEY_HDR: r"^(\s*<!--\s*\S*\s*:\s*)(\S+)(.*-->.*)$",
    S_KEY_LEAD: 1,
    S_KEY_VAL: 2,
    S_KEY_PAD: 3,
    S_KEY_SWITCH: (
        r"^[^\S\r\n]*<!--[^\S\r\n]*pyplate[^\S\r\n]*:"
        r"[^\S\r\n]*(\S*)[^\S\r\n]*=[^\S\r\n]*(\S*)[^\S\r\n]*-->$"
    ),
    S_KEY_COMM: r"^\s*<!--(.*)-->\s*$",
    S_KEY_SPLIT: r"(\'|\")([^\'\"\n]+)(\'|\")|(<!--.*-->)$",
    S_KEY_SPLIT_INDEX: 4,
}

# the info for matching/fixing lines in non-markup files
D_PY_REPL = {
    S_KEY_HDR: r"^(\s*#\s*\S*\s*:\s*)(\S+)(.*)$",
    S_KEY_LEAD: 1,
    S_KEY_VAL: 2,
    S_KEY_PAD: 3,
    S_KEY_SWITCH: (
        r"^[^\S\r\n]*#[^\S\r\n]*pyplate[^\S\r\n]*:"
        r"[^\S\r\n]*(\S*)[^\S\r\n]*=[^\S\r\n]*(\S*)[^\S\r\n]*$"
    ),
    S_KEY_COMM: r"^\s*#",
    S_KEY_SPLIT: r"(\'|\")([^\'\"\n]+)(\'|\")|(#.*)$",
    S_KEY_SPLIT_INDEX: 4,
}

# the type of projects that will ask for a second name
D_NAME_SEC = {
    "p": "Module",
    "g": "Window class",
}

# default dict of block-level switches (should be I_SW_TRUE or I_SW_FALSE)
D_SW_BLOCK_DEF = {
    S_SW_REPLACE: I_SW_TRUE,
}

# default dict of line-level switches (should be I_SW_TRUE if present and
# enabled, I_SW_FALSE if present and disabled, or I_SW_NONE if not present)
D_SW_LINE_DEF = {
    S_SW_REPLACE: I_SW_NONE,
}

# regex's to match project name
D_NAME = {
    S_KEY_NAME_START: r"(^[a-zA-Z])",
    S_KEY_NAME_END: r"([a-zA-Z\d]$)",
    S_KEY_NAME_MID: r"(^[a-zA-Z\d\-_]*$)",
}

# ------------------------------------------------------------------------------
# Public functions
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Do any work before fix
# ------------------------------------------------------------------------------
def do_before_fix(dict_prv_prj=None, dict_pub_meta=None):
    """
    Do any work before fix

    Arguments:
        dict_prv_prj: The dict of project settings (default: D_PRV_PRJ)
        dict_pub_meta: The dictionary containing metadata for the project
        (default: D_PUB_META)

    Do any work before fix. This method is called at the beginning of _do_fix,
    after all dunders have been configured, but before any files have been
    modified.\n
    It is mostly used to make final adjustments to the 'D_PRV_PRJ' dunder dict
    before any replacement occurs.
    """

    # sanity check
    if not dict_prv_prj:
        dict_prv_prj = D_PRV_PRJ
    if not dict_pub_meta:
        dict_pub_meta = D_PUB_META

    # ------------------------------------------------------------------------------
    # these paths are formatted here because they are complex and may be
    # changed by dev

    # get values after pymaker has set them
    author = D_PRV_ALL["__PP_AUTHOR__"]
    name_small = dict_prv_prj["__PP_NAME_SMALL__"]

    # paths relative to the end user's (or dev's) useful folders
    dict_prv_prj["__PP_USR_CONF__"] = f"{S_USR_CONF}/{name_small}"
    dict_prv_prj["__PP_USR_LIB__"] = f"{S_USR_LIB}/{author}/{S_USR_LIB_NAME}"
    dict_prv_prj["__PP_USR_SRC__"] = f"{S_USR_SRC}/{name_small}"

    # add venv to dist list
    # NB: we do this here to avoid having to handle globs in L_DIST
    venv_name = dict_prv_prj["__PP_VENV_NAME__"]
    L_DIST.append(venv_name)


# --------------------------------------------------------------------------
# Do any work after fix
# --------------------------------------------------------------------------
def do_after_fix():
    """
    Do any work after fix

    Arguments:
        dir_prj: The root of the new project

    Do any work after fix. This method is called at the end of the internal
    _do_after_fix, after all files have been modified.
    """


# ------------------------------------------------------------------------------
# File-specific fixes after everything else
# ------------------------------------------------------------------------------
def do_extras(dir_prj, dict_pub_meta=None, dict_prv_prj=None):
    """
    File-specific fixes after everything else

    Arguments:
        dir_prj: the path to the project's directory


    """

    # sanity check
    if not dict_pub_meta:
        dict_pub_meta = D_PUB_META
    if not dict_prv_prj:
        dict_prv_prj = D_PRV_PRJ

    # outsource the big stuff

    print("Do extras/other... ", end="")

    # scan project dir
    for root, _root_dirs, root_files in dir_prj.walk():

        # convert files into Paths
        files = [root / f for f in root_files]

        # check if readme
        if root == dir_prj:
            # for each file item
            for item in files:
                if item.name == D_PRV_ALL["__PP_README_FILE__"]:
                    _fix_readme(item, dict_prv_prj, dict_pub_meta)
                if item.name == D_PRV_ALL["__PP_TOML_FILE__"]:
                    _fix_pyproject(item, dict_pub_meta)

        if root.name == S_DIR_DESKTOP:
            # for each file item
            for item in files:
                # suffix = item.suffix.lstrip(".")
                suffix = (
                    item.suffix if item.suffix[0] == "." else "." + item.suffix
                )
                if suffix in L_DESKTOP:
                    _fix_desktop(item, dict_pub_meta)

        if root.name == S_DIR_UI:
            # for each file item
            for item in files:
                suffix = (
                    item.suffix if item.suffix[0] == "." else "." + item.suffix
                )
                if suffix in L_GTK:
                    _fix_gtk(item, dict_pub_meta)

    print("Done")

    # do i18n stuff
    # print("Do extras/i18n... ", end="")
    # dict_i18n =
    # do_i18n(dict_prj, dict_i18n)
    # print("Done")


# ------------------------------------------------------------------------------
# Private functions
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Remove/replace parts of the main README file
# ------------------------------------------------------------------------------
def _fix_readme(path, dict_pub_meta, dict_prv_prj):
    """
    Remove/replace parts of the main README file

    Arguments:
        path: Path for the README to modify text
        dict_pub_meta: the dict of metadata to replace in the file
        dict_prv_prj: the private calculated proj dict

    Removes parts of the file not applicable to the current project type. Also
    fixes metadata in the file when dict_meta is present.
    """

    # the whole text of the file
    text = ""

    # open and read whole file
    with open(path, "r", encoding="UTF-8") as a_file:
        text = a_file.read()

    # --------------------------------------------------------------------------
    # this part is used by pymaker to remove readme sections

    # find the remove blocks
    prj_type = dict_prv_prj["__PP_TYPE_PRJ__"]
    if prj_type == "c" or prj_type == "g":
        str_pattern = r"<!-- __RM_PKG_START__ -->(.*?)<!-- __RM_PKG_END__ -->"
    else:
        str_pattern = r"<!-- __RM_APP_START__ -->(.*?)<!-- __RM_APP_END__ -->"

    # replace block with empty string (equiv to deleting it)
    # NB: need S flag to make dot match newline
    text = re.sub(str_pattern, "", text, flags=re.S)

    # --------------------------------------------------------------------------
    # this part is used by pybaker to replace metadata

    # replace short description
    str_pattern = (
        r"(<!--[\t ]*__PP_SHORT_DESC__[\t ]*-->)"
        r"(.*?)"
        r"(<!--[\t ]*__PP_SHORT_DESC__[\t ]*-->)"
    )
    pp_short_desc = dict_pub_meta["__PP_SHORT_DESC__"]
    str_rep = rf"\g<1>\n{pp_short_desc}\n\g<3>"
    text = re.sub(str_pattern, str_rep, text, flags=re.S)

    # get deps as links for readme
    d_py_deps = dict_pub_meta["__PP_PY_DEPS__"]
    l_rm_deps = [
        f"[{key}]({val})" if val != "" else key for key, val in d_py_deps
    ]

    #        | 1 | |  2  | | 3| | 4 | |    5    |
    # lst = [res_a if cond else res_b for x in xx]

    # lst = []
    # for x in xx:              5
    #   if cond:                2
    #       lst.append(res_a)   1
    #   else:                   3
    #       lst.append(res_b)   4

    s_rm_deps = "<br>\n".join(l_rm_deps)
    if len(s_rm_deps) == 0:
        s_rm_deps = "None"

    # replace dependencies array
    str_pattern = (
        r"(<!--[\t ]*__PP_RM_DEPS__[\t ]*-->)"
        r"(.*?)"
        r"(<!--[\t ]*__PP_RM_DEPS__[\t ]*-->)"
    )
    str_rep = rf"\g<1>\n{s_rm_deps}\g<3>"
    text = re.sub(str_pattern, str_rep, text, flags=re.S)

    # save file
    with open(path, "w", encoding="UTF-8") as a_file:
        a_file.write(text)


# --------------------------------------------------------------------------
# Replace text in the pyproject file
# --------------------------------------------------------------------------
def _fix_pyproject(path, dict_pub_meta):
    """
    Replace text in the pyproject file

    Arguments:
        path: Path for the file to modify text
        dict_pub_meta: the dict of metadata to replace in the file

    Replaces things like the keywords, requirements, etc. in the toml file.
    """

    # default text if we can't open file
    text = ""

    # open file and get contents
    with open(path, "r", encoding="UTF-8") as a_file:
        text = a_file.read()

    # replace version
    str_pattern = S_TOML_VERSION_SEARCH
    pp_version = dict_pub_meta["__PP_VERSION__"]
    str_rep = S_TOML_VERSION_REPL.format(pp_version)
    text = re.sub(str_pattern, str_rep, text)

    # replace short description
    str_pattern = S_TOML_SHORT_DESC_SEARCH
    pp_short_desc = dict_pub_meta["__PP_SHORT_DESC__"]
    str_rep = S_TOML_SHORT_DESC_REPL.format(pp_short_desc)
    text = re.sub(str_pattern, str_rep, text)

    # fix keywords for pyproject.toml
    l_keywords = dict_pub_meta["__PP_KEYWORDS__"]
    q_keywords = [f'"{item}"' for item in l_keywords]
    s_keywords = ", ".join(q_keywords)

    # replace keywords array
    str_pattern = S_TOML_KW_SEARCH
    str_rep = S_TOML_KW_REPL.format(s_keywords)
    text = re.sub(str_pattern, str_rep, text)

    # save file
    with open(path, "w", encoding="UTF-8") as a_file:
        a_file.write(text)


# ------------------------------------------------------------------------------
# Replace text in the desktop file
# ------------------------------------------------------------------------------
def _fix_desktop(path, dict_pub_meta):
    """
    Replace text in the desktop file

    Arguments:
        path: Path for the file to modify text
        dict_pub_meta: the dict of metadata to replace in the file

    Replaces the desc, exec, icon, path, and category text in a .desktop
    file for programs that use this.
    """

    # validate wanted categories into approved categories
    pp_gui_categories = []
    wanted_cats = dict_pub_meta["__PP_GUI_CATS__"]
    for cat in wanted_cats:
        # category is valid
        if cat in L_CATS:
            # add to final list
            pp_gui_categories.append(cat)
        else:
            # category is not valid, print error and increase error count
            print(
                f'In metadata categories, "{cat}" is not valid, see \n'
                "https://specifications.freedesktop.org/menu-spec/latest/apa.html"
            )

    # convert list to string
    str_cat = ";".join(pp_gui_categories)
    # NB: must have trailing semicolon
    str_cat += ";"

    # default text if we can't open file
    text = ""

    # open file and get contents
    with open(path, "r", encoding="UTF-8") as a_file:
        text = a_file.read()

    # replace categories
    str_pattern = (
        r"(^\s*\[Desktop Entry\]\s*$)"
        r"(.*?)"
        r"(^\s*Categories[\t ]*=)"
        r"(.*?$)"
    )
    str_rep = rf"\g<1>\g<2>\g<3>{str_cat}"
    text = re.sub(str_pattern, str_rep, text, flags=re.M | re.S)

    # replace short description
    str_pattern = (
        r"(^\s*\[Desktop Entry\]\s*$)"
        r"(.*?)"
        r"(^\s*Comment[\t ]*=)"
        r"(.*?$)"
    )
    pp_short_desc = dict_pub_meta["__PP_SHORT_DESC__"]
    str_rep = rf"\g<1>\g<2>\g<3>{pp_short_desc}"
    text = re.sub(str_pattern, str_rep, text, flags=re.M | re.S)

    # save file
    with open(path, "w", encoding="UTF-8") as a_file:
        a_file.write(text)


# ------------------------------------------------------------------------------
# Replace text in the UI files
# ------------------------------------------------------------------------------
def _fix_gtk(path, dict_pub_meta):
    """
    Replace text in the UI files

    Arguments:
        path: Path for the file to modify text
        dict_pub_meta: the dict of metadata to replace in the file

    Replace description and version number in the UI file.
    """

    # default text if we can't open file
    text = ""

    # open file and get contents
    with open(path, "r", encoding="UTF-8") as a_file:
        text = a_file.read()

    # replace short description
    str_pattern = (
        r"(<object class=\"GtkAboutDialog\".*?)"
        r"(<property name=\"comments\".*?\>)"
        r"(.*?)"
        r"(</property>)"
    )
    pp_short_desc = dict_pub_meta["__PP_SHORT_DESC__"]
    str_rep = rf"\g<1>\g<2>{pp_short_desc}\g<4>"
    text = re.sub(str_pattern, str_rep, text, flags=re.M | re.S)

    # replace version
    str_pattern = (
        r"(<object class=\"GtkAboutDialog\".*?)"
        r"(<property name=\"version\">)"
        r"(.*?)"
        r"(</property>.*)"
    )
    pp_version = dict_pub_meta["__PP_VERSION__"]
    str_rep = rf"\g<1>\g<2>{pp_version}\g<4>"
    text = re.sub(str_pattern, str_rep, text, flags=re.M | re.S)

    # save file
    with open(path, "w", encoding="UTF-8") as a_file:
        a_file.write(text)

# # --------------------------------------------------------------------------
# # Run CNPotPy over files to produce I18N files
# # --------------------------------------------------------------------------
# def _do_i18n(dict_prj, dict_pub_i18n):
#     """
#     Run CNPotPy over files to produce I18N files
#     """

#     # # dict of clangs and exts
#     dict_in = {
#         "Python": [
#             ".py",
#         ],
#         "Glade": [
#             ".ui",
#             ".glade",
#         ],
#         "Desktop": [".desktop"],
#     }

#     # dict of clangs and no exts (ie file names)
#     no_ext = "Python"

#     # the list of languages your program has been translated into (can grow
#     # over time, adding languages as they become available)
#     list_wlangs = [
#         "es",
#         "xo",
#         "pq",
#     ]

#     name_big = self._dict_prv_prj["__PP_NAME_BIG__"]
#     name_small = self._dict_prv_prj["__PP_NAME_SMALL__"]
#     version = self._dict_pub_meta["__PP_VERSION__"]
#     author = self._dict_prv_all["__PP_AUTHOR__"]
#     email = self._dict_prv_all["__PP_EMAIL__"]

#     # path to src dir
#     dir_src = self._dir_prj / M.S_DIR_SRC
#     dir_locale = self._dir_prj / "src" / "support" / "i18n" / "locale"
#     dir_po = self._dir_prj / "src" / "support" / "i18n" / "po"

#     # create CNPotPy object
#     pp = CNPotPy(
#         dir_src,
#         str_appname=name_big,
#         str_version=version,
#         str_author=author,
#         str_email=email,
#         dir_locale=dir_locale,
#         dir_po=dir_po,
#         str_domain=name_small,
#         dict_clangs=dict_in,
#         no_ext=no_ext,
#         list_wlangs=list_wlangs,
#     )

#     # this .pot, .po, and .mo files
#     pp.main()

#     # pp.make_desktop(
#     #     self._dir_prj / "src" / "support" / "desktop" / "template.desktop",
#     #     self._dir_prj
#     #     / "src"
#     #     / "support"
#     #     / "desktop"
#     #     / f"{name_small}.desktop",
#     # )


# -)
