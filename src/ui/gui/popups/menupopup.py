# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menupopup.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout

import sys

class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Menu)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.pushButton = QtWidgets.QPushButton(Menu)
        self.pushButton.setGeometry(QtCore.QRect(90, 80, 171, 20))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Menu)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 110, 171, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Menu)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 140, 171, 20))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Menu)
        self.buttonBox.accepted.connect(Menu.accept)
        self.buttonBox.rejected.connect(Menu.reject)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Menu"))
        self.pushButton.setText(_translate("Menu", "Export"))
        self.pushButton_2.setText(_translate("Menu", "View Relationships"))
        self.pushButton_3.setText(_translate("Menu", "Create Node"))


class OpenMenuPopup(QMainWindow):
    
    def __init__(self): 
        super().__init__()
        
        self.initUI()
    
    def initUI(self):    
        layout = QVBoxLayout()
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Menu()
        self.ui.setupUi(self.Dialog)
        layout.addWidget(self.Dialog)
        self.setLayout(layout)
        #sys.exit(app1.exec_())
    def Open(self):
        self.Dialog.show()
        

