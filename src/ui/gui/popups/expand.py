# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'expand.ui'
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
        Form.resize(640, 151)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 641, 31))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 7, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 5, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 6, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 4, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 8, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 29, 641, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_17 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_2.addWidget(self.label_17)
        self.label_13 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_2.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_2.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_2.addWidget(self.label_15)
        self.label_18 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_2.addWidget(self.label_18)
        self.label_16 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_2.addWidget(self.label_16)
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Expand"))
        self.label_2.setText(_translate("Form", "      Log ID"))
        self.label_3.setText(_translate("Form", " Original Document"))
        self.label_5.setText(_translate("Form", "   Event Team"))
        self.label_8.setText(_translate("Form", "    Timestamp"))
        self.label_4.setText(_translate("Form", "       Icon"))
        self.label_7.setText(_translate("Form", "   Description "))
        self.label_6.setText(_translate("Form", "     Reporter"))
        self.label_9.setText(_translate("Form", "       Name"))
        self.label.setText(_translate("Form", " List of Vectors Attached      "))
        self.label_17.setText(_translate("Form", "###"))
        self.label_13.setText(_translate("Form", "red_team"))
        self.label_14.setText(_translate("Form", "white team"))
        self.label_15.setText(_translate("Form", "ed attack"))
        self.label_18.setText(_translate("Form", "Name"))
        self.label_16.setText(_translate("Form", "12/21/2019"))
        self.label_12.setText(_translate("Form", "red_team_icon.png"))
        self.label_11.setText(_translate("Form", "whiteTeamReport.txt"))
        self.label_10.setText(_translate("Form", "1.vector 4"))


        

class OpenExpandPopup(QMainWindow):
    
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