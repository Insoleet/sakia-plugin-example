PLUGIN_NAME = "Plugin example"
PLUGIN_DESCRIPTION = "A simple widget"
PLUGIN_VERSION = "0.1"

from .main_dialog import ExampleDialog

def plugin_exec(app, main_window):
    """
    :param sakia.app.Application app:
    :param sakia.gui.main_window.controller.MainWindowController main_window:
    """
    from PyQt5.QtWidgets import QAction
    tool_menu = main_window.toolbar.view.toolbutton_menu.menu()
    action_open_example = QAction("Plugin example", tool_menu)
    tool_menu.addAction(action_open_example)
    action_open_example.triggered.connect(lambda c, a=app, mw=main_window: open_dialog(a, mw))


def open_dialog(app, main_window):
    """
    :param sakia.app.Application app:
    :param sakia.gui.main_window.controller.MainWindowController main_window:
    """
    dialog = ExampleDialog(main_window)
    dialog.exec()


from . import icons_rc