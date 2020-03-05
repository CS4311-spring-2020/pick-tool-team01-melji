# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout

# from popups.menupopup import OpenMenuPopup
# from popups.ChangeVector import OpenVectorChangePopup
from popups.vector_configuration import OpenVectorConfigPopup
from popups.vc_manager import OpenVCPopup
from popups.timestamp_filter import OpenTSPopup
from popups.remove_link import OpenRLPopup
from popups.relationships import OpenRelatePopup
from popups.node_creator import OpenNodeCreatePopup
from popups.IconConfiguration import IconConfiguration
from popups.FilterVector import OpenFilterVectorPopup
from popups.filterTeam import OpenFilterTeamPopup
from popups.filter_all import OpenFilterAllPopup
from popups.export_configuration import OpenExportConfigPopup
from popups.expand import OpenExpandPopup
from popups.connect_link import OpenconnectlinkPopup
from popups.IconConfiguration import IconConfiguration

import sys


class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.setFixedSize(300, 300)
        Menu.setWindowTitle("Menu")
        self.buttonBox = QtWidgets.QDialogButtonBox(Menu)
        self.buttonBox.setGeometry(QtCore.QRect(0, 240, 260, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)

        self.pushButton = QtWidgets.QPushButton(Menu)
        self.pushButton.setGeometry(QtCore.QRect(90, 80, 170, 20))
        self.pushButton.setText("Export")
        self.pushButton.clicked.connect(lambda: OpenExportConfigPopup())

        self.pushButton_2 = QtWidgets.QPushButton(Menu)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 110, 170, 20))
        self.pushButton_2.setText("View Relationships")
        self.pushButton_2.clicked.connect(lambda: OpenRelatePopup())

        self.pushButton_3 = QtWidgets.QPushButton(Menu)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 140, 170, 20))
        self.pushButton_3.setText("Create Node")
        self.pushButton_3.clicked.connect(lambda: OpenNodeCreatePopup())

        self.pushButton_4 = QtWidgets.QPushButton(Menu)
        self.pushButton_4.setGeometry(QtCore.QRect(90, 170, 170, 20))
        self.pushButton_4.setText("Add Icon")
        variable = IconConfiguration()
        self.pushButton_4.clicked.connect(lambda: variable.showiconconfig())


        self.buttonBox.accepted.connect(Menu.accept)
        self.buttonBox.rejected.connect(Menu.reject)
        QtCore.QMetaObject.connectSlotsByName(Menu)



class OpenMenuPopup(QMainWindow):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Menu()
        self.ui.setupUi(self.Dialog)
        layout.addWidget(self.Dialog)
        self.setLayout(layout)
        self.Dialog.show()
