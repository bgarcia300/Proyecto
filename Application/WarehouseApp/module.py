from PyQt6 import QtCore, QtGui, QtWidgets
from UI.Control.wareHouse import Ui_Dialog
from Domain.classes import *

class FrmWarehouse(QtWidgets.QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.ui.btnSave.clicked.connect(self.btnSave_Clicked)
        
    def btnSave_Clicked(self):
        self.oItem = Warehouse()
        self.oItem.id = self.ui.txtIdWarehouse.text()
        self.oItem.name = self.ui.txtWarehouse.text() 
        self.ui.txtIdWarehouse.setText("")
        self.ui.txtWarehouse.setText("")