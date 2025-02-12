# ------------------------------------------------------------------------------
# Project : __PP_NAME_BIG__                                        /          \
# Filename: __PP_NAME_SEC___win.py                                |     ()     |
# Date    : __PP_DATE__                                           |            |
# Author  : __PP_AUTHOR__                                         |   \____/   |
# License : __PP_LICENSE_NAME__                                    \          /
# ------------------------------------------------------------------------------

"""
A class to manage a specific Window (or type of window).

This class manages the more advanced functions of a window, such as specific
control handlers.
Remember to connect all the appropriate window events in your ui file to the
private functions declared here.
"""

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

# system imports
from pathlib import Path
import sys

# find path to lib
P_DIR_PRJ_INST = Path.home() / "__PP_USR_INST__"
P_DIR_PRJ = Path(__file__).parents[3].resolve()

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
# pylint: disable=wrong-import-order
# pylint: disable=no-name-in-module
# pylint: disable=import-error

# my imports
from cnguilib.cnwindow import CNWindow  # type: ignore

# pylint: enable=wrong-import-position
# pylint: enable=wrong-import-order
# pylint: enable=import-error
# pylint: enable=no-name-in-module

# ------------------------------------------------------------------------------
# Strings
# ------------------------------------------------------------------------------

# the name of the window in the ui file
UI_WIN_NAME = "__PP_NAME_SEC__"

# ------------------------------------------------------------------------------
# Public classes
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# A class to wrap a specific window object in the ui file
# ------------------------------------------------------------------------------
class __PP_NAME_CLASS__(CNWindow):
    """
    A class to wrap a specific window object in the ui file

    This class contains all the handler code for a specific window and it's
    controls.
    """

    # --------------------------------------------------------------------------
    # Class methods
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # Initialize the new object
    # --------------------------------------------------------------------------
    def __init__(self, app, name_win):
        """
        Initialize the new object

        Args:
            app: The calling Application object
            name_win: The name of the window in the app's instance list

        Initializes a new instance of the class, setting the default values of
        its properties, and any other code needed to create a new object.
        """

        # props necessary tro create a basic window
        # NB: no ext (will find .ui, .glade, .xml...)
        ui_file = P_DIR_PRJ / "__PP_DIR_UI__" / f"{UI_WIN_NAME}"
        ui_path = Path(ui_file).resolve()

        # create a basic window
        super().__init__(app, name_win, ui_path, UI_WIN_NAME)

    # --------------------------------------------------------------------------
    # Private methods
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # Called when the About button is clicked
    # --------------------------------------------------------------------------
    def _btn_about_clicked(self, _obj):
        """
        Called when the About button is clicked

        Args:
            _obj: Not used

        The About button was clicked, show the About dialog.
        """

        # get dialog, run, hide (standard for reusable modal dialogs)
        # NB: no ext (will find .ui, .glade, .xml...)
        dlg_file = P_DIR_PRJ / "__PP_DIR_UI__" / "__PP_DLG_FILE__"
        dlg_path = Path(dlg_file).resolve()
        self._app.show_dialog(dlg_path, "__PP_DLG_ABOUT__")

    # --------------------------------------------------------------------------
    # Called when the New button is clicked
    # --------------------------------------------------------------------------
    def _btn_new_clicked(self, _obj):
        """
        Called when the New button is clicked

        Args:
            _obj: Not used

        The New button was clicked, add the new window.
        """

        print("btn_new: not implemented")

    # --------------------------------------------------------------------------
    # Called when the Title button is clicked
    # --------------------------------------------------------------------------
    def _btn_title_clicked(self, _obj):
        """
        Called when the Title button is clicked

        Args:
            _obj: Not used

        The Title button was clicked, change the window title.
        """

        print("btn_title: not implemented")

    # --------------------------------------------------------------------------
    # Called when the Save button is clicked
    # --------------------------------------------------------------------------
    def _btn_save_clicked(self, _obj):
        """
        Called when the Save button is clicked

        Args:
            _obj: Not used

        The Save button was clicked.
        """

        print("btn_save: not implemented")

    # --------------------------------------------------------------------------
    # Called when the Cancel button is clicked
    # --------------------------------------------------------------------------
    def _btn_cancel_clicked(self, _obj):
        """
        Called when the Cancel button is clicked

        Args:
            _obj: Not used

        The Cancel button was clicked.
        """

        print("btn_cancel: not implemented")

    # --------------------------------------------------------------------------
    # Called when the OK button is clicked
    # --------------------------------------------------------------------------
    def _btn_ok_clicked(self, _obj):
        """
        Called when the OK button is clicked

        Args:
            _obj: Not used

        The OK button was clicked.
        """

        print("btn_ok: not implemented")

    # --------------------------------------------------------------------------
    # Called when the Close button is clicked
    # --------------------------------------------------------------------------
    def _btn_close_clicked(self, _obj):
        """
        Called when the Close button is clicked

        Args:
            _obj: Not used

        The Close button was clicked.
        """

        # close the window as if by the 'X' button
        self.window.close()


# -)
