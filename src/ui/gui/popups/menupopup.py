# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menupopup.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout

#from popups.menupopup import OpenMenuPopup
#from popups.ChangeVector import OpenVectorChangePopup
from popups.vector_configuration import OpenVectorConfigPopup
from popups.vc_manager import OpenVCPopup
from popups.timestamp_filter import OpenTSPopup
from popups.team_configuration import Configure_Team
from popups.remove_link import OpenRLPopup
from popups.relationships import OpenRelatePopup
from popups.node_creator import OpenNodeCreatePopup
from popups.IconConfiguration import IconConfiguration
from popups.FilterVector import OpenFilterVectorPopup
from popups.filterTeam import OpenFilterTeamPopup
from popups.filter_all import OpenFilterAllPopup
from popups.export_configuration import OpenExportConfigPopup
from popups.expand import OpenExpandPopup
from popups.directory_configuration import Configure_Directory
from popups.connect_link import OpenconnectlinkPopup
from popups.IconConfiguration import IconConfiguration

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
        self.pushButton_4 = QtWidgets.QPushButton(Menu)
        self.pushButton_4.setGeometry(QtCore.QRect(90, 180, 171, 20))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Menu)
        self.buttonBox.accepted.connect(Menu.accept)
        self.buttonBox.rejected.connect(Menu.reject)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Menu"))
        self.pushButton.setText(_translate("Menu", "Export"))
        self.pushButton.clicked.connect(lambda: OpenExportConfigPopup())
        self.pushButton_2.setText(_translate("Menu", "View Relationships"))
        self.pushButton_2.clicked.connect(lambda: OpenRelatePopup())
        self.pushButton_3.setText(_translate("Menu", "Create Node"))
        self.pushButton_3.clicked.connect(lambda: OpenNodeCreatePopup())
        self.pushButton_4.setText(_translate("Menu", "Add Icon"))
        varable = IconConfiguration()
        self.pushButton_4.clicked.connect(lambda: varable.showiconconfig())

    #icon = IconConfiguration()



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
        self.Dialog.show()
        #sys.exit(app1.exec_())
    #def Open(self):
        

