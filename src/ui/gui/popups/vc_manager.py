# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vc_manager.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout

import sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Version Control")
        Form.resize(400, 164)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(80, 46, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 116, 81, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 46, 81, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(220, 116, 81, 31))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Version Controll"))
        self.pushButton.setText(_translate("Form", "Push"))
        self.pushButton_2.setText(_translate("Form", "Disconnect"))
        self.pushButton_3.setText(_translate("Form", "Pull"))
        self.pushButton_4.setText(_translate("Form", "Connect"))



class OpenVCPopup(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
    
    def initUI(self):    
        layout = QVBoxLayout()
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Dialog)
        layout.addWidget(self.Dialog)
        self.setLayout(layout)
        self.Dialog.show()
        #sys.exit(app1.exec_())