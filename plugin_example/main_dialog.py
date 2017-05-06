from .example_uic import Ui_ExampleDialog
from PyQt5.QtWidgets import QDialog


class ExampleDialog(QDialog, Ui_ExampleDialog):
    def __init__(self, main_window):
        super().__init__(main_window.view)

        self.setupUi(self)
        self.button_close.clicked.connect(self.close)

