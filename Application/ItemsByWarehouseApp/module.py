from PyQt6 import QtCore, QtGui, QtWidgets
from UI.Inventario.itemsByWarehouse import Ui_Dialog
from Domain.classes import Item
from Domain.classes import Warehouse
from Domain.coreModule import persistence

class FrmItemsByWarehouse(QtWidgets.QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.addComboboxItems()
        #self.ui.btnSave.clicked.connect(self.btnSave_Clicked)
        
    def addComboboxItems(self):
        for item in persistence.getItem():
            self.ui.cmbItem.addItem(str(item.name))        
            
        for warehouse in persistence.getWarehouse():
            self.ui.cmbWarehouse.addItem(str(warehouse.name))
    """
    def assingMaxAmount(self):
        for item in persistence.getItem():
            if item.name == self.ui.cmbItem.currentText():
                self.ui.spnItemsNumber.setMaximum(persistence.getItem.amount)
                self.ui.spnItemsNumber.setValue(str(persistence.getItem.amount))
                print(persistence.getItem.amount)
                
    def btnSave_Clicked(self):
        self.oWarehouse = Warehouse()
        for item in persistence.getItem():
            if item.name == self.ui.cmbItem.currentText():
                index = item.index
        for item in persistence.getWarehouse():
            if item.index == index:
                item.amount = self.ui.spnItemsNumber.value()
                print(self.ui.spnItemsNumber.value())
                print(item.amount)"""