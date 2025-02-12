# Form implementation generated from reading ui file 'itemsByWarehouse.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from Domain.coreModule import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(476, 216)
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 141, 51))
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 141, 20))
        self.label.setObjectName("label")
        self.btnSave = QtWidgets.QPushButton(parent=Dialog)
        self.btnSave.setGeometry(QtCore.QRect(340, 30, 101, 23))
        self.btnSave.setObjectName("btnSave")
        self.btnBack = QtWidgets.QPushButton(parent=Dialog)
        self.btnBack.setGeometry(QtCore.QRect(340, 80, 101, 23))
        self.btnBack.setObjectName("btnBack")
        self.cmbItem = QtWidgets.QComboBox(parent=Dialog)
        self.cmbItem.setGeometry(QtCore.QRect(170, 30, 161, 22))
        self.cmbItem.setObjectName("cmbItem")
        self.cmbItem.currentTextChanged.connect(self.spinner_index_changed)
        self.cmbWarehouse = QtWidgets.QComboBox(parent=Dialog)
        self.cmbWarehouse.setGeometry(QtCore.QRect(170, 140, 161, 22))
        self.cmbWarehouse.setObjectName("cmbWarehouse")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 151, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.spnItemsNumber = QtWidgets.QSpinBox(parent=Dialog)
        self.spnItemsNumber.setGeometry(QtCore.QRect(170, 80, 161, 22))
        self.spnItemsNumber.setObjectName("spnItemsNumber")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Asignacion de articulos por bodegas"))
        self.label_2.setText(_translate("Dialog", "Seleccione la bodega a la cual desea asignar el articulo"))
        self.label.setText(_translate("Dialog", "¿Que articulo desea mover?"))
        self.btnSave.setText(_translate("Dialog", "Guardar"))
        self.btnBack.setText(_translate("Dialog", "Volver"))
        self.label_3.setText(_translate("Dialog", "¿Cuantos de estos articulos desea mover?"))
    
    def spinner_index_changed(self, itemName):
        for item in inventory_manager.items:
            if inventory_manager.items[item].name == itemName:
                self.spnItemsNumber.setMaximum(inventory_manager.items[item].amount)
                self.spnItemsNumber.setMinimum(1)
                self.spnItemsNumber.setValue(inventory_manager.items[item].amount)
