#############################################################################
##  This code changes your view to vectors of your choosing
##  Thanks - Micheal 2/1/20
#############################################################################
import sys
#sys.path.insert(0, '../nodeview/NodeView.py')
from PyQt5.QtWidgets import (QScrollArea, QWidget, QGridLayout, QLabel, QPushButton,QMainWindow,QVBoxLayout,QHBoxLayout,QFrame)
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.Qt import *
from random import seed,randint
import random
import os
#sys.path.insert(0, os.path.abspath('...'))

import string
#import pick-tool-team01-melji.src.ui.gui.nodeview.NodeView




class OpenVectorChangePopup(QMainWindow):
    
    def __init__(self): # this is to start grid builder before .show  ***note grid builder will require a array of data type called loginfo in the future***
        super().__init__()
        
        #self.initUI()
        print('cwd is %s' %(os.getcwd()))
        #this code runs GridBuilder
        #############################################################################

        _widget = QWidget()
        
        add_button = QPushButton("change vector")
        add_button.setMaximumWidth(150)
        delete_button = QPushButton("Delete")
        delete_button.setMaximumWidth(150)
        edit_button = QPushButton("Edit")
        edit_button.setMaximumWidth(150)
        add_button.clicked.connect( lambda: self.closeMyApp_OpenNewApp())
        
        widget = QWidget()                  
        layoutv = QVBoxLayout()       
        layouth = QHBoxLayout()                       
        widget.setLayout(layoutv)
        
        self.mainv = vectconfigtempname()
        layoutv.addWidget(self.mainv)
        layouth.addWidget(add_button)
        #layouth.addWidget(delete_button)
        #layouth.addWidget(edit_button)
        layoutv.addLayout(layouth)
        layoutv.setAlignment(Qt.AlignVCenter|Qt.AlignHCenter)
        widget.setLayout(layoutv)


        
        _layout = QVBoxLayout(_widget)
        _layout.addWidget(widget)
        

        self.setCentralWidget(_widget)

        #############################################################################

        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle("Vector Configuration")  
        #self.show()
    def showprojectconfig(self):
        self.show()
        
    def closeMyApp_OpenNewApp(self): 
        self.close() 
        self.Open = NodeView() 
        self.Open.show()



class vectconfigtempname(QScrollArea):## experimenting with vector add
    def __init__(self, parent=None):
        super(vectconfigtempname, self).__init__(parent)
        self.scrollmake()
    def add_vecotor(vector_to_add):
        return
    def scrollmake(self):
        self.widget = QWidget()                 
        self.layoutgrid = QGridLayout()  
        self.layoutgrid.setSpacing(0)
        self.layoutgrid.setHorizontalSpacing(0)
        i = 0
        n = 0
        
        numofsample = 0
        numofsample = randint(5, 28)

        
            

        for y in range(0,numofsample):
             
            self.button1 = Vector_Push_Button()
            self.text1 = LogRandNameTextWidget()
            self.text2 = LogRandNameTextWidget()
            self.layoutgrid.addWidget(self.button1,y,0)
            self.layoutgrid.addWidget(self.text1,y,1)
            self.layoutgrid.addWidget(self.text2,y,2)
            y= y+1
            n = n+1
        
        self.widget.setLayout(self.layoutgrid)
        self.setWidgetResizable(True)
        self.setWidget(self.widget)
        
        #this code sets borders to 1px
        #QRegExp regexp(".*border: *(\\d+)px.*");
        #if (regexp.indexIn(btn->styleSheet()) >= 0)
        #qDebug() << regexp.cap(1);

        return


widthofcolumns = 200
heightofrows=50
heightoftextrow = 25
class LogRandNameTextWidget(QFrame):

    def __init__(self, parent=None):
        super(LogRandNameTextWidget,self).__init__(parent)

        letters = string.ascii_lowercase
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        
        a =  randint(1, 8)
        randomtext = ''
        for x in range(0,a):
            randomtextvar =''.join( random.choice(letters) for i in range(randint(0, 20)))
            randomtext = randomtext + ' ' + randomtextvar
        
       
        self.textlable = QLabel(randomtext)
        self.textlable.setWordWrap(True)
        layout.addWidget(self.textlable)
        self.setLayout(layout)  
        self.setMaximumWidth(widthofcolumns)

        return

class Vector_Push_Button(QFrame):

    def __init__(self,parent=None):
        super(Vector_Push_Button,self).__init__(parent)
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setAlignment(Qt.AlignVCenter|Qt.AlignHCenter)
        layout.setSpacing(0)
        self.push_button = QPushButton()
        self.setStyleSheet("border: 1px solid black;")
        layout.addWidget(self.push_button)
        self.setLayout(layout)    
        self.setMaximumWidth(heightofrows)
        return

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
        
if __name__ == "__main__": #remove a's to test without running program
    sys.path.append(os.getcwd())
    from src.ui.gui.nodeview.NodeView import NodeView
    sys.path.append(os.getcwd()+"/src/ui/gui/")
    app = QApplication(sys.argv)
    print('cwd is %s' %(os.getcwd()))
    ex = OpenVectorChangePopup()
    ex.showprojectconfig()
    sys.exit(app.exec_())
else:
    from nodeview.NodeView import NodeView