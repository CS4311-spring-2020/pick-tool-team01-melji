# -*- coding: utf-8 -*-


import sys
import qdarkstyle
from PyQt5.QtWidgets import QScrollArea, QWidget, QGridLayout, QLabel, QPushButton, QMainWindow, QHBoxLayout, QVBoxLayout, QTextEdit, QCheckBox , QTimeEdit, QCalendarWidget
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.Qt import *
max_width = 4000
from popups.directory_configuration import Configure_Directory

class Configure_Event(QMainWindow):
    def __init__(self): # this is to start grid builder before .show  ***note grid builder will require a array of data type called loginfo in the future***
        super().__init__()
        
        #self.initUI()

        #this code runs GridBuilder
        #############################################################################

        _widget = QWidget()
                  
        layout = QGridLayout()    
        
        
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(10)
        
       
        

        title_label = QLabel("Event Configuration")
        title_label.setMaximumHeight(35)
        
        layout_name = QHBoxLayout()
        name_text_label = QLabel("Event Name")
        #name_text_label.setMaximumWidth(150)
        name_text_label.setMaximumHeight(35)
        name_edit = QTextEdit()
        #name_edit.setMaximumWidth(300)
        name_edit.setMaximumHeight(35)
        layout_name.addWidget(name_text_label)
        layout_name.addWidget(name_edit)
        layout_name.setSpacing(0)

        layout_description = QHBoxLayout()
        description_text_label = QLabel("Event description")
        #description_text_label.setMaximumWidth(150)
        description_edit = QTextEdit()
        #description_edit.setMaximumWidth(300)
        description_edit.setMaximumHeight(150)
        layout_description.addWidget(description_text_label)
        layout_description.addWidget(description_edit)
        layout_description.setSpacing(0)

        layout_start = QHBoxLayout()
        start_text_label = QLabel("Event Start")
        #start_text_label.setMaximumWidth(150)
        start_text_label.setMaximumHeight(35)
        start_calendar = QCalendarWidget()
        #start_calendar.setMaximumWidth(600)
        start_calendar.setMaximumHeight(200)
        start_calendar.setGridVisible(True)
        start_time = QTime()
        start_time.setHMS(12,0,0)
        start_time_edit = QTimeEdit()
        start_time_edit.setTime(start_time)
        start_time_edit.setMaximumHeight(35)
        layout_start.addWidget(start_text_label)
        layout_start.addWidget(start_time_edit)
        layout_start.addWidget(start_calendar)
        layout_start.setSpacing(0)

        layout_end = QHBoxLayout()
        end_text_label = QLabel("Event End")
        #end_text_label.setMaximumWidth(150)
        end_text_label.setMaximumHeight(35)
        end_calendar = QCalendarWidget()
        #end_calendar.setMaximumWidth(600)
        end_calendar.setMaximumHeight(200)
        end_calendar.setGridVisible(True)
        end_time = QTime()
        end_time.setHMS(12,0,0)
        end_time_edit = QTimeEdit()
        end_time_edit.setTime(end_time)
        end_time_edit.setMaximumHeight(35)
        layout_end.addWidget(end_text_label)
        layout_end.addWidget(end_time_edit)
        layout_end.addWidget(end_calendar)
        layout_end.setSpacing(0)

        connect_project_button = QPushButton("Save Event")
        self.directory_config = Configure_Directory()
        connect_project_button.clicked.connect(lambda: self.closeMyApp_OpenNewApp())
        back_button = QPushButton("Go Back")
        back_button.clicked.connect(lambda: self.OpenPrevApp())
        #connect_project_button.clicked.connect(self.directory_config.show_config)
        #connect_project_button.setMaximumWidth(150) def closeMyApp_OpenNewApp(self): self.close() self.Open = NewApp.NewApp() self.Open.show()

        widget = QWidget()                    
        widget.setLayout(layout)

        layout.addWidget(title_label, 0, 0, 1, 3)
        layout.addLayout(layout_name,1,0,1,3)
        layout.addLayout(layout_description,2,0,1,3)
        layout.addLayout(layout_start,3,0,1,3)
        layout.addLayout(layout_end,4,0,1,3)
        layout.addWidget(connect_project_button,5,2)
        layout.addWidget(back_button,5,0)
        
        layout.setAlignment(Qt.AlignVCenter|Qt.AlignHCenter)
        widget.setLayout(layout)

        _layout = QVBoxLayout(_widget)
        _layout.addWidget(widget)
        _layout.setAlignment(Qt.AlignVCenter|Qt.AlignHCenter)
        self.setCentralWidget(_widget)
        #############################################################################

        self.setGeometry(400, 400, 400, 650)
        self.setWindowTitle("Event Configuration")  
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

