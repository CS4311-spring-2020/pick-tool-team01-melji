# -*- coding: utf-8 -*-


import sys
import qdarkstyle
from PyQt5.QtWidgets import QScrollArea, QWidget, QGridLayout, QLabel, QPushButton, QMainWindow, QHBoxLayout, QVBoxLayout, QTextEdit, QCheckBox , QTimeEdit, QCalendarWidget
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.Qt import *
from src.objects.Vector import Vector
max_width = 4000
#from popups.directory_configuration import Configure_Directory

class Make_Vector(QMainWindow):
    def __init__(self,vector_list): # this is to start grid builder before .show  ***note grid builder will require a array of data type called loginfo in the future***
        super().__init__()
        
        #self.initUI()

        #this code runs GridBuilder
        #############################################################################

        _widget = QWidget()
                  
        layout = QGridLayout()    
        
        
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(10)
        
       
        

        #title_label = QLabel("Make Vector")
        #title_label.setMaximumHeight(35)
        
        layout_name = QHBoxLayout()
        name_text_label = QLabel("Vector Name")
        #name_text_label.setMaximumWidth(150)
        name_text_label.setMaximumHeight(35)
        name_edit = QTextEdit()
        #name_edit.setMaximumWidth(300)
        name_edit.setMaximumHeight(35)
        layout_name.addWidget(name_text_label)
        layout_name.addWidget(name_edit)
        layout_name.setSpacing(0)

        layout_description = QHBoxLayout()
        description_text_label = QLabel("Vector Description")
        #description_text_label.setMaximumWidth(150)
        description_edit = QTextEdit()
        #description_edit.setMaximumWidth(300)
        description_edit.setMaximumHeight(150)
        layout_description.addWidget(description_text_label)
        layout_description.addWidget(description_edit)
        layout_description.setSpacing(0)

        connect_project_button = QPushButton("Make Vector")
        #self.directory_config = Configure_Directory()
        connect_project_button.clicked.connect(lambda: self.create_vector(name_edit,description_edit,vector_list))
        back_button = QPushButton("Cancel")
        back_button.clicked.connect(lambda: self.closeApp())
        #connect_project_button.clicked.connect(self.directory_config.show_config)
        #connect_project_button.setMaximumWidth(150) def closeMyApp_OpenNewApp(self): self.close() self.Open = NewApp.NewApp() self.Open.show()

        widget = QWidget()                    
        widget.setLayout(layout)

        #layout.addWidget(title_label, 0, 0, 1, 3)
        layout.addLayout(layout_name,1,0,1,3)
        layout.addLayout(layout_description,2,0,1,3)
        
        layout.addWidget(connect_project_button,5,2)
        layout.addWidget(back_button,5,0)
        
        layout.setAlignment(Qt.AlignVCenter|Qt.AlignHCenter)
        widget.setLayout(layout)

        _layout = QVBoxLayout(_widget)
        _layout.addWidget(widget)
        _layout.setAlignment(Qt.AlignVCenter|Qt.AlignHCenter)
        self.setCentralWidget(_widget)
        #############################################################################

        self.setGeometry(400, 400, 400, 450)
        self.setWindowTitle("Make Vector")  
        self.show()
    def closeApp(self):
        self.close()
        return
    def create_vector(self, name, description,vector_list):
        nametext = name.toPlainText()
        descriptiontext = description.toPlainText()
        num = 0
        nodelist = []
        if vector_list:
            num = vector_list[-1].return_item("vector_id") # expects a number
            num+=1
        vector_list.append(Vector(num,nametext,None,None,descriptiontext,nodelist))
        self.close()
        return



    def closeMyApp_OpenNewApp(self): 
        self.close() 
        nxt = Configure_Directory()
        #nxt.getselfsnxt) 
        #mys = self.myself
        nxt.getlast(self)
        self.Open = nxt 
        self.Open.show()
    def getlastconf(self,lastc):
        self.lasta = lastc
        
    def OpenPrevApp(self): 
        #ex2 = NodeView()
        self.close() 
        self.Open = self.lasta
        self.Open.show()
    def show_config(self):
        self.show()

