from PyQt6 import QtCore, QtGui, QtWidgets
from UI.Control.wareHouse import Ui_Dialog

class FrmWarehouse(QtWidgets.QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)