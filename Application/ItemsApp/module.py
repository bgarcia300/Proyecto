from PyQt6 import QtCore, QtGui, QtWidgets
from UI.Control.items import Ui_Dialog
from Domain.coreModule import *

class FrmItems(QtWidgets.QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.oItem = None
        
        self.ui.btnSave.clicked.connect(self.btnSave_Clicked)
        
    def btnSave_Clicked(self):
        id = self.ui.txtId.text()
        name = self.ui.txtItem.text() 
        amount = int(self.ui.txtDescription.text())
        self.ui.txtId.setText("")
        self.ui.txtItem.setText("")
        self.ui.txtDescription.setText("")
        inventory_manager.add_item(id, name, amount)