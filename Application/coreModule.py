from PyQt6 import QtCore, QtGui, QtWidgets
from UI.Core.mainWindow import Ui_mainWindow
from Application.ItemsApp.module import *
from Application.WarehouseApp.module import *
from Application.DistributorApp.module import * 
from Application.ItemsByWarehouseApp.module import *
from Application.ItemsByDistributorApp.module import * 

class FrmMain(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.mnuItems.triggered.connect(self.onClickMnuItems)
        self.ui.mnuWarehouse.triggered.connect(self.onClickMnuWarehouse)
        self.ui.mnuDistribuitors.triggered.connect(self.onClickMnuDistributor)
        self.ui.mnuItemsByWarehouse.triggered.connect(self.onClickMnuItemsByWarehouse)
        self.ui.mnuItemsByDistributor.triggered.connect(self.onClickMnuItemsByDistributor)
        self.itemsWindow = None
        self.warehouseWindow = None
        self.distribuitorWindow = None
        self.itemsByWarehouseWindow = None
        self.itemsByDistributorWindow = None
    
        
    def onClickMnuItems(self):
        self.itemsWindow = FrmItems()
        self.itemsWindow.show()
        
    def onClickMnuWarehouse(self):
        self.warehouseWindow = FrmWarehouse()
        self.warehouseWindow.show()
        
    def onClickMnuDistributor(self):
        self.distribuitorWindow = FrmDistributor()
        self.distribuitorWindow.show()
        
    def onClickMnuItemsByWarehouse(self):
        self.itemsByDistributorWindow = FrmItemsByWarehouse()
        self.itemsByDistributorWindow.show()
        
    def onClickMnuItemsByDistributor(self):
        self.itemsByDistributorWindow = FrmItemsByDistributor()
        self.itemsByDistributorWindow.show()