from PyQt6 import QtCore, QtGui, QtWidgets
from UI.Inventario.itemsByWarehouse import Ui_Dialog
from Domain.classes import Item
from Domain.coreModule import persistence

class FrmItemsByWarehouse(QtWidgets.QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.addComboboxItems()
        self.addComboboxWarehouses()
        
    def addComboboxItems(self):
        for item in persistence.getItem():
            self.ui.cmbItem.addItem(str(item.name))
            
    def addComboboxWarehouses(self):
        for warehouse in persistence.getWarehouse():
            self.ui.cmbWarehouse.addItem(str(warehouse.name))