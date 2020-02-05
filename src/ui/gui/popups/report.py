# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'report.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(527, 441)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 531, 111))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(0, 110, 531, 111))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_3.setReadOnly(True)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(0, 220, 531, 111))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_4.setReadOnly(True)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(0, 330, 531, 111))
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Report"))
        self.plainTextEdit.setPlainText(_translate("Dialog", "Validation issue 1\n""Location: bin/file\n""Violation: Timestamp not found"))
        self.plainTextEdit_2.setPlainText(_translate("Dialog", "Validation issue 2\n""Location: bin/file\n""Violation: Cannot read file"))
        self.plainTextEdit_3.setPlainText(_translate("Dialog", "Validation issue 3\n""Location: bin/file\n""Violation: Timestamp not found"))
        self.plainTextEdit_4.setPlainText(_translate("Dialog", "Validation issue 4\n""Location: bin/file\n""Violation: Timestamp not found"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
