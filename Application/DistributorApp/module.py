from PyQt6 import QtCore, QtGui, QtWidgets
from UI.Control.distribuitor import Ui_Dialog
from Domain.classes import *

class FrmDistributor(QtWidgets.QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.ui.btnSave.clicked.connect(self.btnSave_Clicked)
        
    def btnSave_Clicked(self):
        self.oItem = Distributor()
        self.oItem.id = self.ui.txtDistribuitor.text()
        self.oItem.name = self.ui.txtIdDistribuitor.text() 
        self.oItem.address = self.ui.txtAddress.text() 
        self.ui.txtDistribuitor.setText("")
        self.ui.txtIdDistribuitor.setText("")
        self.ui.txtAddress.setText("")
        