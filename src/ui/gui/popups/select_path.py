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


class Paths(QMainWindow):
    def __init__(self): # this is to start grid builder before .show  ***note grid builder will require a array of data type called loginfo in the future***
        super().__init__()
        
        #self.initUI()

        #this code runs GridBuilder
        #############################################################################

        _widget = QWidget()
        
        addprojectbutton = QPushButton("New Project")
        addprojectbutton.setMaximumWidth(150)
        deleteprojectbutton = QPushButton("Connect to Project")
        deleteprojectbutton.setMaximumWidth(150)
        editprojectbutton = QPushButton("Resume Project")
        editprojectbutton.setMaximumWidth(150)

        widget = QWidget()                  
        layouth = QVBoxLayout()                
        widget.setLayout(layouth)
        layouth.addWidget(addprojectbutton)
        layouth.addWidget(deleteprojectbutton)
        layouth.addWidget(editprojectbutton)
        layouth.setAlignment(Qt.AlignVCenter|Qt.AlignHCenter)
        
        widget.setLayout(layouth)
        


        
        _layout = QVBoxLayout(_widget)
        _layout.addWidget(widget)
        

        self.setCentralWidget(_widget)

        #############################################################################

        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle("PICK")  
        #self.show()


    def showpaths(self):
        self.show()




    
    