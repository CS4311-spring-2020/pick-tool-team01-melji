# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vector_configuration.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout,QScrollArea,QWidget,QGridLayout,QLabel,QFrame,QHBoxLayout
from random import seed,randint
import random
from PyQt5.Qt import *
import string

import sys
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Vector Configuration")
        Form.resize(393, 300)
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(-5, 1, 501, 211))
        self.tableView.setObjectName("tableView")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 0, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(220, 0, 81, 16))
        self.label_2.setObjectName("label_2")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(20, 20, 53, 14))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 60, 53, 14))
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(Form)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 100, 53, 14))
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(Form)
        self.checkBox_4.setGeometry(QtCore.QRect(20, 140, 53, 14))
        self.checkBox_4.setText("")
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(Form)
        self.checkBox_5.setGeometry(QtCore.QRect(20, 180, 53, 14))
        self.checkBox_5.setText("")
        self.checkBox_5.setObjectName("checkBox_5")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(210, 20, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(0, 40, 491, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 60, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(210, 100, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(210, 140, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(210, 180, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(0, 80, 491, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(0, 120, 501, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(0, 160, 501, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Form)
        self.line_5.setGeometry(QtCore.QRect(0, 200, 491, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 230, 56, 17))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 230, 56, 17))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 230, 56, 17))
        self.pushButton_3.setObjectName("pushButton_3")
        self.line_6 = QtWidgets.QFrame(Form)
        self.line_6.setGeometry(QtCore.QRect(50, 0, 20, 211))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalScrollBar = QtWidgets.QScrollBar(Form)
        self.verticalScrollBar.setGeometry(QtCore.QRect(380, 0, 16, 211))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 20, 35, 10))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(80, 60, 35, 10))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(80, 100, 35, 10))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(80, 140, 35, 10))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(80, 180, 35, 10))
        self.label_7.setObjectName("label_7")
        self.line_7 = QtWidgets.QFrame(Form)
        self.line_7.setGeometry(QtCore.QRect(160, 0, 16, 211))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Vector Configuration"))
        self.label.setText(_translate("Form", "Vector Name:"))
        self.label_2.setText(_translate("Form", "Vector Description:"))
        self.lineEdit.setText(_translate("Form", "Description of vector"))
        self.lineEdit_2.setText(_translate("Form", "Description of vector"))
        self.lineEdit_3.setText(_translate("Form", "Description of Vector"))
        self.lineEdit_4.setText(_translate("Form", "Description of vector"))
        self.lineEdit_5.setText(_translate("Form", "Description of vector"))
        self.pushButton.setText(_translate("Form", "Add "))
        self.pushButton_2.setText(_translate("Form", "Delete "))
        self.pushButton_3.setText(_translate("Form", "Edit"))
        self.label_3.setText(_translate("Form", "Vector1"))
        self.label_4.setText(_translate("Form", "Vector2"))
        self.label_5.setText(_translate("Form", "Vector3"))
        self.label_6.setText(_translate("Form", "Vector4"))
        self.label_7.setText(_translate("Form", "Vector5"))




class OpenVectorConfigPopup(QMainWindow):
    
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
        #sys.exit(app1.exec_())\




class vectconfigtempname(QScrollArea):
    def __init__(self, parent=None):
        super(vectconfigtempname, self).__init__(parent)
        self.scrollmake()
    def add_vecotor(vector_to_add):
        return
    def scrollmake(self):
        self.widget = QWidget()                 
        self.layoutgrid = QGridLayout()  
        self.layoutgrid.setSpacing(0)
        self.layoutgrid.setHorizontalSpacing(0)
        i = 0
        n = 0
        
        numofsample = 0
        numofsample = randint(5, 28)

        
            

        for y in range(0,numofsample):
             
            self.button1 = Vector_Push_Button()
            self.text1 = LogRandNameTextWidget()
            self.text2 = LogRandNameTextWidget()
            self.layoutgrid.addWidget(self.button1,y,0)
            self.layoutgrid.addWidget(self.text1,y,1)
            self.layoutgrid.addWidget(self.text2,y,2)
            n = n+1
        
        self.widget.setLayout(self.layoutgrid)
        self.setWidgetResizable(True)
        self.setWidget(self.widget)
        
        #this code sets borders to 1px
        #QRegExp regexp(".*border: *(\\d+)px.*");
        #if (regexp.indexIn(btn->styleSheet()) >= 0)
        #qDebug() << regexp.cap(1);

        return


widthofcolumns = 200
heightofrows=50
heightoftextrow = 25
class LogRandNameTextWidget(QFrame):

    def __init__(self, parent=None):
        super(LogRandNameTextWidget,self).__init__(parent)

        letters = string.ascii_lowercase
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        
        a =  randint(1, 8)
        randomtext = ''
        for x in range(0,a):
            randomtextvar =''.join( random.choice(letters) for i in range(randint(0, 20)))
            randomtext = randomtext + ' ' + randomtextvar
        
       
        self.textlable = QLabel(randomtext)
        self.textlable.setWordWrap(True)
        layout.addWidget(self.textlable)
        self.setLayout(layout)  
        self.setMaximumHeight(heightoftextrow)
        self.setMaximumWidth(heightoftextrow)

        return

class Vector_Push_Button(QFrame):

    def __init__(self,parent=None):
        super(Vector_Push_Button,self).__init__(parent)
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setAlignment(Qt.AlignVCenter|Qt.AlignHCenter)
        layout.setSpacing(0)
        self.push_button = QPushButton()
        self.setStyleSheet("border: 1px solid black;")
        layout.addWidget(self.push_button)
        self.setLayout(layout)    
        self.setMaximumHeight(heightoftextrow)
        return
        
class VectorConfigPopup(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):    
        layout = QVBoxLayout()
        self.mainv = vectconfigtempname()
        layout.addWidget(self.mainv)
        self.setlayout(layout)
        self.show
        #sys.exit(app1.exec_())\

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OpenVectorConfigPopup()
    sys.exit(app.exec_())