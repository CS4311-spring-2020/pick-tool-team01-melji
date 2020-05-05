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
from src.objects.Node import Node
from src.objects.Vector import Vector

import random
import os
#sys.path.insert(0, os.path.abspath('...'))

import string
#import pick-tool-team01-melji.src.ui.gui.nodeview.NodeView




class AddVectorPopup(QMainWindow):
    
    def __init__(self,vectors,this_log,vectors_list,where_to_add,widget_to_update): # this is to start grid builder before .show  ***note grid builder will require a array of data type called loginfo in the future***
        super().__init__()
        
        #self.initUI()
        #print('cwd is %s' %(os.getcwd()))
        #this code runs GridBuilder
        #############################################################################

        _widget = QWidget()
        print('h1')
        add_button = QPushButton("change vector")
        add_button.setMaximumWidth(150)
        delete_button = QPushButton("Delete")
        delete_button.setMaximumWidth(150)
        edit_button = QPushButton("Edit")
        edit_button.setMaximumWidth(150)
        
        widget = QWidget()                  
        layoutv = QVBoxLayout()       
        layouth = QHBoxLayout()                       
        widget.setLayout(layoutv)
        
        self.mainv = vectconfigtempname(vectors,vectors_list)
        add_button.clicked.connect( lambda: self.add_clicked(self.mainv,where_to_add,this_log,widget_to_update))
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
        self.show()
        
    def add_clicked(self,get_list,layout,this_log,widget_to_update): 
        array = get_list.button_list
        for x in range(0,len(array)):
            val = array[x].return_if_checked()
            if val: 
                str_val = str(val.return_item("vector_name"))
                print(" val = %s"%(val.return_item("vector_name")))
                print(" val = %s"%(array[x].name))
                lable = QLabel(str_val)
                layout.addWidget(lable)
                widget_to_update.update()
                log_v_list = this_log.return_item("vector_list")
                log_v_list.append(val.return_item("vector_name"))
                temp = this_log.edit_item("vector_list",log_v_list)
                n_list = val.return_item("node_list")
                id_last = 0
                link_list = []
                if n_list:
                    last = n_list[-1]
                    id_last = last.return_item("node_id")
                    id_last += 1
                node = Node(id_last,this_log.return_item("log_name"),this_log.return_item("timestamp"),this_log.return_item("discription"),this_log.return_item("reporter"),this_log.return_item("event_team"),this_log.return_item("location"),this_log.return_item("icon_location"),this_log.return_item("origin_document"),link_list)
                n_list.append(node)
                value_trash = val.edit_item("node_list",n_list)
                


        self.close() 
        #return choices
        #self.Open = NodeView() 
        #self.Open.show()



class vectconfigtempname(QScrollArea):## experimenting with vector add
    def __init__(self,vectors,vectors_list, parent=None):
        super(vectconfigtempname, self).__init__(parent)
        self.button_list = []
        self.widget = QWidget()                 
        self.layoutgrid = QGridLayout()  
        self.layoutgrid.setSpacing(0)
        self.layoutgrid.setHorizontalSpacing(0)
        i = 0
        n = 0
        
        numofsample = 0
        numofsample = randint(5, 28)

        
            

        #for y in range(0,numofsample):
        for y in range(0,len(vectors)):
            if not vectors[y]:
                break
            else:
                self.button1 = Vector_Push_Button(vectors[y],vectors_list)
                if self.button1:
                    self.button_list.append(self.button1)
                    self.text1 = LogRandNameTextWidget(self.button1.name)
                    self.text2 = LogRandNameTextWidget(self.button1.description)
                    self.layoutgrid.addWidget(self.button1,y,0)
                    self.layoutgrid.addWidget(self.text1,y,1)
                    self.layoutgrid.addWidget(self.text2,y,2)
                    
                else:
                    return None
        
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

    def __init__(self,text, parent=None):
        super(LogRandNameTextWidget,self).__init__(parent)

        letters = string.ascii_lowercase
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        
        
        
       
        self.textlable = QLabel(text)
        self.textlable.setWordWrap(True)
        layout.addWidget(self.textlable)
        self.setLayout(layout)  
        self.setMaximumWidth(widthofcolumns)

        return

class Vector_Push_Button(QFrame):

    def __init__(self,vector,vector_list,parent=None):
        super(Vector_Push_Button,self).__init__(parent)
        print("here1")
        layout = QHBoxLayout()
        print("here2")
        self.vector = vector
        print("here3")
        layout.setContentsMargins(0,0,0,0)
        print("here4")
        layout.setAlignment(Qt.AlignVCenter|Qt.AlignHCenter)
        print("here5")
        layout.setSpacing(0)
        print("here6")
        self.check_button = QCheckBox("add")
        print("here7")
        self.name = vector.return_item("vector_name")
        print("here8")
        self.description = vector.return_item("discription")
        print("here9")
        self.check_button.setChecked(False)
        print("here10")
        self.setStyleSheet("border: 1px solid black;")
        print("here11")
        layout.addWidget(self.check_button)
        print("here12")
        if self.vector.return_item("vector_name") in vector_list:
            return None
        print("here13")
        self.setLayout(layout)    
        self.setMaximumWidth(heightofrows)
        
        
    def return_if_checked(self):
        if self.check_button.isChecked():
            return self.vector
        else:
            return None

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
    #from src.ui.gui.nodeview.NodeView import NodeView
    from src.objects.Vector import Vector
    sys.path.append(os.getcwd()+"/src/ui/gui/")
    app = QApplication(sys.argv)
    #print('cwd is %s' %(os.getcwd()))
    
    ex = AddVectorPopup()
    ex.show()
    sys.exit(app.exec_())
#else:
    #from nodeview.NodeView import NodeView