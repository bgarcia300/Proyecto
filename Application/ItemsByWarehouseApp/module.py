from PyQt6 import QtCore, QtGui, QtWidgets
from UI.Inventario.itemsByWarehouse import Ui_Dialog
from Domain.coreModule import *

class FrmItemsByWarehouse(QtWidgets.QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.addComboboxItems()
        self.assingSpinnerValues()
        self.ui.btnSave.clicked.connect(self.btnSave_Clicked)
        
    def addComboboxItems(self):
        for item in inventory_manager.items:
            self.ui.cmbItem.addItem(inventory_manager.items[item].name)        
            
        for warehouse in inventory_manager.warehouses:
            self.ui.cmbWarehouse.addItem(inventory_manager.warehouses[warehouse].name)

    def assingSpinnerValues(self):
        itemName = self.ui.cmbItem.currentText()
        for item in inventory_manager.items:
            if inventory_manager.items[item].name == itemName:
                self.spnItemsNumber.setMaximum(inventory_manager.items[item].amount)
                self.spnItemsNumber.setMinimum(1)
                self.spnItemsNumber.setValue(inventory_manager.items[item].amount)
                
    def btnSave_Clicked(self):

        itemName = self.ui.cmbItem.currentText()
        itemId = 0
        for item in inventory_manager.items:
            if inventory_manager.items[item].name == itemName:
                itemId = item


        warehouseId = 0
        warehouseName = self.ui.cmbWarehouse.currentText()
        for warehouse in inventory_manager.warehouses:
            if inventory_manager.warehouses[warehouse].name == warehouseName:
                warehouseId = warehouse

        quantity = self.ui.spnItemsNumber.value()

        inventory_manager.assign_item(warehouseId, itemId, quantity)

        self.assingSpinnerValues()



