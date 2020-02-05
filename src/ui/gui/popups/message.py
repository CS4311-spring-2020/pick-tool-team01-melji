# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'message.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(469, 328)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 441, 16))
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 40, 471, 191))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 240, 441, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(380, 290, 81, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 290, 81, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Message"))
        self.label.setText(_translate("Dialog", "Warning your version has the following differences from the main program:"))
        self.plainTextEdit.setPlainText(_translate("Dialog", "Gravida in fermentum et sollicitudin ac orci phasellus egestas tellus. Dolor purus non enim praesent elementum facilisis. Diam quam nulla porttitor massa id neque aliquam vestibulum. Pellentesque id nibh tortor id aliquet lectus proin nibh nisl. Suspendisse ultrices gravida dictum fusce ut placerat orci nulla pellentesque. Amet nisl purus in mollis nunc sed. Dui id ornare arcu odio ut sem nulla pharetra diam. Suscipit tellus mauris a diam maecenas. Mattis aliquam faucibus purus in massa tempor nec feugiat. Blandit aliquam etiam erat velit. Nunc vel risus commodo viverra. Ornare suspendisse sed nisi lacus. Mi sit ametGravida in fermentum et sollicitudin ac orci phasellus egestas tellus. Dolor purus non enim praesent elementum facilisis. Diam quam nulla porttitor massa id neque aliquam vestibulum. "))
        self.label_2.setText(_translate("Dialog", "Do you wish to merge the server copy with yours?"))
        self.pushButton.setText(_translate("Dialog", "Proceed"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
