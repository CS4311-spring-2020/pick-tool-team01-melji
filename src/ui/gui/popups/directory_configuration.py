# -*- coding: utf-8 -*-


import sys
import qdarkstyle
from PyQt5.QtWidgets import QScrollArea, QWidget, QGridLayout, QLabel, QPushButton, QMainWindow, QHBoxLayout, QVBoxLayout, QTextEdit, QCheckBox , QTimeEdit, QCalendarWidget
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.Qt import *
max_width = 4000

class Configure_Directory(QMainWindow):
    def __init__(self): 
        super().__init__()
        
      

        _widget = QWidget()
                  
        layout = QGridLayout()    
        
        
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(10)
        
       
        

        title_label = QLabel("Directory Configuration")
        title_label.setMaximumHeight(35)
        
        root_file = QHBoxLayout()
        self.file_text_label = QLabel("C:/")
        self.file_text_label.setMaximumHeight(90)
        self.file_text_label.setWordWrap(True)
        file_button = QPushButton("Root Directory")
        file_button.setMaximumWidth(150)
        file_button.setMinimumWidth(150)
        file_button.clicked.connect(self.get_root)
        file_button.setMaximumHeight(35)
        root_file.addWidget(self.file_text_label)
        root_file.addWidget(file_button)
        root_file.setSpacing(0)
        
        red_team_file = QHBoxLayout()
        self.red_file_text_label = QLabel("C:/")
        self.red_file_text_label.setMaximumHeight(90)
        self.red_file_text_label.setWordWrap(True)
        red_file_button = QPushButton("Red Team Directory")
        red_file_button.setMaximumWidth(150)
        red_file_button.setMinimumWidth(150)
        red_file_button.clicked.connect(self.get_red_file)
        red_file_button.setMaximumHeight(35)
        red_team_file.addWidget(self.red_file_text_label)
        red_team_file.addWidget(red_file_button)
        red_team_file.setSpacing(0)

        
        blue_team_file = QHBoxLayout()
        self.blue_file_text_label = QLabel("C:/")
        self.blue_file_text_label.setMaximumHeight(90)
        self.blue_file_text_label.setWordWrap(True)
        blue_file_button = QPushButton("Blue Team Directory")
        blue_file_button.setMaximumWidth(150)
        blue_file_button.setMinimumWidth(150)
        blue_file_button.clicked.connect(self.get_blue_file)
        blue_file_button.setMaximumHeight(35)
        blue_team_file.addWidget(self.blue_file_text_label)
        blue_team_file.addWidget(blue_file_button)
        blue_team_file.setSpacing(0)

        white_team_file = QHBoxLayout()
        self.white_file_text_label = QLabel("C:/")
        self.white_file_text_label.setMinimumWidth(300)
        self.white_file_text_label.setMaximumHeight(90)
        self.white_file_text_label.setWordWrap(True)
        white_file_button = QPushButton("White Team Directory")
        white_file_button.setMaximumWidth(150)
        white_file_button.setMinimumWidth(150)
        white_file_button.clicked.connect(self.get_white_file)
        white_file_button.setMaximumHeight(35)
        white_team_file.addWidget(self.white_file_text_label)
        white_team_file.addWidget(white_file_button)
        white_team_file.setSpacing(0)

        start_ingestion_button = QPushButton("Start Data Ingestion")
        start_ingestion_button.clicked.connect(self.get_blue_file)

        widget = QWidget()                    
        widget.setLayout(layout)

        layout.addWidget(title_label, 0, 1)
        layout.addLayout(root_file,1,0,1,3)
        layout.addLayout(red_team_file,2,0,1,3)
        layout.addLayout(blue_team_file,3,0,1,3)
        layout.addLayout(white_team_file,4,0,1,3)
        layout.addWidget(start_ingestion_button,5,2)
        
        layout.setAlignment(Qt.AlignVCenter|Qt.AlignHCenter)
        widget.setLayout(layout)

        _layout = QVBoxLayout(_widget)
        _layout.addWidget(widget)
        _layout.setAlignment(Qt.AlignVCenter|Qt.AlignHCenter)
        self.setCentralWidget(_widget)
        #############################################################################

        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle("Event Configuration")  


    def show_config(self):
        self.show()

    def get_root(self):
        self.root_folder = QFileDialog.getExistingDirectory(self, 'Open Root Directory', options=QFileDialog.ShowDirsOnly)
        self.file_text_label.setText(self.root_folder)
        
        #dlg = QFileDialog()
        #dlg.setFileMode(QFileDialog.AnyFile)
        #dlg.setFilter("Text files (*.txt)")
        #filenames = QStringList()

        
    def get_red_file(self):
        self.red_folder = QFileDialog.getExistingDirectory(self, 'Open Red Team Directory', options=QFileDialog.ShowDirsOnly)
        self.red_file_text_label.setText(self.red_folder)
        
        
    def get_blue_file(self):
        self.blue_folder = QFileDialog.getExistingDirectory(self, 'Open Blue Team Directory', options=QFileDialog.ShowDirsOnly)
        self.blue_file_text_label.setText(self.blue_folder)
        
    def get_white_file(self):
        self.white_folder = QFileDialog.getExistingDirectory(self, 'Open White Team Directory', options=QFileDialog.ShowDirsOnly)
        self.white_file_text_label.setText(self.white_folder)

    def call_ingestion(self):
        #yourvalidationservicecalltopassinformation(self.root_folder,self.red_folder,self.blue_folder,self.white_folder,)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Configure_Directory()
    ex.show_config()
    sys.exit(app.exec_())


    
    