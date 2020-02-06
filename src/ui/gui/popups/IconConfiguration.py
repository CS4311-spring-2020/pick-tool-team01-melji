#############################################################################
##  This code shoveswhatever is in an array of "LogInfo" into individual spaces - todo
##  Thanks - Micheal 2/1/20
#############################################################################
import sys
from PyQt5.QtWidgets import (QScrollArea, QWidget, QGridLayout, QLabel, QPushButton,QMainWindow,QHBoxLayout,QVBoxLayout)
from PyQt5.QtGui import QIcon, QPixmap

class IconConfiguration(QMainWindow):
    
    def __init__(self): # this is to start grid builder before .show  ***note grid builder will require a array of data type called loginfo in the future***
        super().__init__()
        
        #self.initUI()

        #this code runs GridBuilder
        #############################################################################

        _widget = QWidget()
        
        addiconbutton = QPushButton("Add Icon")
        addiconbutton.setMaximumWidth(150)
        deleteiconbutton = QPushButton("Delete Icon")
        deleteiconbutton.setMaximumWidth(150)
        editiconbutton = QPushButton("Edit Icon")
        editiconbutton.setMaximumWidth(150)

        widget = QWidget()                  
        layouth = QHBoxLayout()                
        widget.setLayout(layouth)
        layouth.addWidget(addiconbutton)
        layouth.addWidget(deleteiconbutton)
        layouth.addWidget(editiconbutton)

        widget.setLayout(layouth)


        grid = IconMake()
        _layout = QVBoxLayout(_widget)
        _layout.addWidget(widget)
        _layout.addWidget(grid)
        

        self.setCentralWidget(_widget)

        #############################################################################

        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle("Icon Configuration")  
        #self.show()
    def showiconconfig(self):
        self.show()




class IconMake(QScrollArea):   
    def __init__(self, parent=None):
        super(IconMake, self).__init__(parent)
        self.scrollmake()

    def scrollmake(self):
        self.widget = QWidget()                 
        self.layoutgrid = QGridLayout()  
        self.layoutgrid.setSpacing(0)
        self.layoutgrid.setHorizontalSpacing(0)

        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)

        label1.setPixmap(QPixmap("bin\\assets\\white.png"))
        label2.setPixmap(QPixmap("bin\\assets\\blue.png"))
        label3.setPixmap(QPixmap("bin\\assets\\red.png"))

        label1.setScaledContents(True)
        label1.setMaximumHeight(100)
        label1.setMaximumWidth(120)
        label2.setScaledContents(True)
        label2.setMaximumHeight(100)
        label2.setMaximumWidth(120)
        label3.setScaledContents(True)
        label3.setMaximumHeight(100)
        label3.setMaximumWidth(120)
        self.layoutgrid.addWidget(label1,0,0)
        self.layoutgrid.addWidget(label2,0,1)
        self.layoutgrid.addWidget(label3,0,2)
        self.widget.setLayout(self.layoutgrid)
        self.setWidgetResizable(True)
        self.setWidget(self.widget)

        return
