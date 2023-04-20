from PyQt6 import QtCore, QtGui, QtWidgets
from UI.Control.wareHouse import Ui_Dialog
from Domain.coreModule import *

class FrmWarehouse(QtWidgets.QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.ui.btnSave.clicked.connect(self.btnSave_Clicked)
        
    def btnSave_Clicked(self):
        id = self.ui.txtIdWarehouse.text()
        name = self.ui.txtWarehouse.text() 
        self.ui.txtIdWarehouse.setText("")
        self.ui.txtWarehouse.setText("")
        inventory_manager.add_warehouse(id, name)
        print(inventory_manager.warehouses)