# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filter_all.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout

import sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 195)
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(10, 130, 41, 21))
        self.radioButton.setObjectName("radioButton")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(60, 0, 20, 291))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(80, 130, 41, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(130, 0, 20, 191))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Form)
        self.radioButton_3.setGeometry(QtCore.QRect(150, 130, 41, 16))
        self.radioButton_3.setObjectName("radioButton_3")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(200, 0, 20, 201))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Form)
        self.dateTimeEdit.setGeometry(QtCore.QRect(230, 30, 91, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(330, 0, 20, 191))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(345, 90, 51, 20))
        self.pushButton.setObjectName("pushButton")
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(Form)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(230, 80, 91, 22))
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.radioButton_4 = QtWidgets.QRadioButton(Form)
        self.radioButton_4.setGeometry(QtCore.QRect(250, 130, 41, 16))
        self.radioButton_4.setObjectName("radioButton_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 100, 35, 10))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(90, 100, 35, 10))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(150, 100, 51, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(250, 110, 41, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(220, 20, 35, 10))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(220, 70, 35, 10))
        self.label_6.setObjectName("label_6")
        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Filter All"))
        self.radioButton.setText(_translate("Form", "Enable"))
        self.radioButton_2.setText(_translate("Form", "Enable"))
        self.radioButton_3.setText(_translate("Form", "Enable"))
        self.pushButton.setText(_translate("Form", "Filter"))
        self.radioButton_4.setText(_translate("Form", "Enable"))
        self.label.setText(_translate("Form", "Vector"))
        self.label_2.setText(_translate("Form", "Reporter"))
        self.label_3.setText(_translate("Form", "Event Team"))
        self.label_4.setText(_translate("Form", "Timestamp"))
        self.label_5.setText(_translate("Form", "Start:"))
        self.label_6.setText(_translate("Form", "End:"))
        self.comboBox.setItemText(0, _translate("Form", "None"))
        self.comboBox.setItemText(0, _translate("Form", ""))


 
class OpenFilterAllPopup(QMainWindow):
    
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
        self.Dialog.show()