#############################################################################
##  This code shoveswhatever is in an array of "LogInfo" into individual spaces - todo
##  Thanks - Micheal 2/1/20
#############################################################################
import sys
from PyQt5.QtWidgets import (QScrollArea, QWidget, QGridLayout, QLabel, QPushButton,QMainWindow,QVBoxLayout,QVBoxLayout)
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.Qt import *

class ProjectConfiguration(QMainWindow):
    
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
        self.setWindowTitle("project Configuration")  
        #self.show()
    def showprojectconfig(self):
        self.show()




class projectMake(QScrollArea):   
    def __init__(self, parent=None):
        super(projectMake, self).__init__(parent)
        self.scrollmake()

    def scrollmake(self):
        self.widget = QWidget()                 
        self.layoutgrid = QGridLayout()  
        self.layoutgrid.setSpacing(0)
        self.layoutgrid.setHorizontalSpacing(0)

        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)

        label1.setPixmap(QPixmap("bin/assets/white.png"))
        label2.setPixmap(QPixmap("bin/assets/blue.png"))
        label3.setPixmap(QPixmap("bin/assets/red.png"))

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
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = ProjectConfiguration()
    ex.showprojectconfig()
    sys.exit(app.exec_())