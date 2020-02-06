# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timestamp_filter.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout

import sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Timestamp Filter")
        Form.resize(400, 124)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Form)
        self.dateTimeEdit.setGeometry(QtCore.QRect(40, 40, 101, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(Form)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(250, 40, 111, 22))
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 30, 35, 10))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(250, 30, 35, 10))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 90, 56, 17))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Timestamp Filter"))
        self.label.setText(_translate("Form", "Start:"))
        self.label_2.setText(_translate("Form", "End:"))
        self.pushButton.setText(_translate("Form", "Filter"))




class OpenTFPopup(QMainWindow):
    
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
        #sys.exit(app1.exec_())
    def Open(self):
        self.Dialog.show()