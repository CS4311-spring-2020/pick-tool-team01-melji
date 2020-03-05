# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setFixedSize(400, 164)
        Form.setWindowTitle("Version Control")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(80, 46, 81, 31))
        self.pushButton.setText("Push")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 116, 81, 31))
        self.pushButton_2.setText("Disconnect")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 46, 81, 31))
        self.pushButton_3.setText("Pull")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(220, 116, 81, 31))
        self.pushButton_4.setText("Connect")

class OpenVCPopup(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Dialog)
        layout.addWidget(self.Dialog)
        self.setLayout(layout)
        self.Dialog.show()
        #sys.exit(app1.exec_())
