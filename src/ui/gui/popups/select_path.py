# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'team_configuration.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5.QtWidgets import (QScrollArea, QWidget, QGridLayout, QLabel, QPushButton, QMainWindow, QVBoxLayout, QVBoxLayout)
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.Qt import *
from popups.team_configuration import Configure_Team
from popups.Event_Configuration import Configure_Event

class Paths(QMainWindow):
    def __init__(self): # this is to start grid builder before .show  ***note grid builder will require a array of data type called loginfo in the future***
        super().__init__()
        
        #self.initUI()

        #this code runs GridBuilder
        #############################################################################

        _widget = QWidget()
        
        addprojectbutton = QPushButton("New Project")
        #self.team_config = Configure_Team()
        #self.event_config = Configure_Event()
        addprojectbutton.clicked.connect(lambda: self.closeMyApp_OpenNewApp_Event())
        addprojectbutton.setMaximumWidth(150)
        connectprojectbutton = QPushButton("Connect to Project")
        connectprojectbutton.clicked.connect(lambda: self.closeMyApp_OpenNewApp_Team())
        connectprojectbutton.setMaximumWidth(150)
        resumeprojectbutton = QPushButton("Resume Project")
        resumeprojectbutton.setMaximumWidth(150)

        widget = QWidget()                  
        layouth = QVBoxLayout()                
        widget.setLayout(layouth)
        layouth.addWidget(addprojectbutton)
        layouth.addWidget(connectprojectbutton)
        layouth.addWidget(resumeprojectbutton)
        layouth.setAlignment(Qt.AlignVCenter|Qt.AlignHCenter)
        
        widget.setLayout(layouth)
        


        
        _layout = QVBoxLayout(_widget)
        _layout.addWidget(widget)
        

        self.setCentralWidget(_widget)

        #############################################################################

        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle("PICK")  
        #self.show()
    
    
    def closeMyApp_OpenNewApp_Event(self): 
        #ex2 = NodeView()
        self.close() 
        configevent = Configure_Event() 
        configevent.getlastconf(self)
        self.Open = configevent
        self.Open.show()
    def closeMyApp_OpenNewApp_Team(self): 
        #ex2 = NodeView()
        self.close() 
        configteam = Configure_Team()
        self.Open = configteam 
        self.Open.show()

    def showpaths(self):
        self.show()



    
    