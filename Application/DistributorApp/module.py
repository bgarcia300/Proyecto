from PyQt6 import QtCore, QtGui, QtWidgets
from UI.Control.distribuitor import Ui_Dialog
from Domain.coreModule import *

class FrmDistributor(QtWidgets.QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.ui.btnSave.clicked.connect(self.btnSave_Clicked)
        
    def btnSave_Clicked(self):
        name = self.ui.txtDistribuitor.text()
        id = self.ui.txtIdDistribuitor.text()
        address = self.ui.txtAddress.text() 
        self.ui.txtDistribuitor.setText("")
        self.ui.txtIdDistribuitor.setText("")
        self.ui.txtAddress.setText("")
        inventory_manager.add_distributor(id, name, address)
        