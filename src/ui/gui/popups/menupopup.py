# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menupopup.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


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
        Menu.setWindowTitle(_translate("Menu", "Dialog"))
        self.pushButton.setText(_translate("Menu", "Export"))
        self.pushButton_2.setText(_translate("Menu", "View Relationships"))
        self.pushButton_3.setText(_translate("Menu", "Create Node"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Menu()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())