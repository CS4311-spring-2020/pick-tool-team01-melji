# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'team_configuration.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import sys
import qdarkstyle
from PyQt5.QtWidgets import QScrollArea, QWidget, QGridLayout, QLabel, QPushButton, QMainWindow, QHBoxLayout, QVBoxLayout, QTextEdit, QCheckBox
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.Qt import *


class Configure_Team(QMainWindow):
    def __init__(self): # this is to start grid builder before .show  ***note grid builder will require a array of data type called loginfo in the future***
        super().__init__()
        
        #self.initUI()

        #this code runs GridBuilder
        #############################################################################

        _widget = QWidget()
                  
        layout = QGridLayout()    
        
        
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(10)
        
       
        

        name_label = QLabel("Team Configuration")
        name_label.setMaximumWidth(150)
        name_label.setMaximumHeight(35)

        lead_check_button = QCheckBox("Lead?")
        lead_check_button.setMaximumWidth(150)
        

        layout_lead_ip = QHBoxLayout()
        ip_label = QLabel("Lead IP Address")
        ip_label.setMaximumWidth(150)
        ip_label.setMaximumHeight(25)
        ip_edit = QTextEdit()
        ip_edit.setMaximumWidth(300)
        ip_edit.setMaximumHeight(25)
        layout_lead_ip.addWidget(ip_label)
        layout_lead_ip.addWidget(ip_edit)
        layout_lead_ip.setSpacing(0)

        layout_connections = QHBoxLayout()
        connections_text_label = QLabel("Number of Established connectons to lead")
        connections_text_label.setMaximumWidth(300)
        connections_text_label.setMaximumHeight(35)
        connections_label = QLabel("Number")
        connections_label.setMaximumWidth(150)
        connections_label.setMaximumHeight(35)
        layout_connections.addWidget(connections_text_label)
        layout_connections.addWidget(connections_label)
        layout_connections.setSpacing(0)

        connect_project_button = QPushButton("Connect")
        connect_project_button.setMaximumWidth(150)

        widget = QWidget()                    
        widget.setLayout(layout)

        layout.addWidget(name_label, 0, 0, 1, 2)
        layout.addWidget(lead_check_button, 1, 0, 1, 2)
        layout.addLayout(layout_lead_ip,2,0,1,2)
        layout.addLayout(layout_connections,3,0,1,2)
        layout.addWidget(connect_project_button,4,1)
        
        layout.setAlignment(Qt.AlignVCenter|Qt.AlignHCenter)
        widget.setLayout(layout)

        _layout = QVBoxLayout(_widget)
        _layout.addWidget(widget)
        _layout.setAlignment(Qt.AlignVCenter|Qt.AlignHCenter)
        self.setCentralWidget(_widget)
        #############################################################################

        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle("Team Configuration")  


    def show_config(self):
        self.show()


    
    