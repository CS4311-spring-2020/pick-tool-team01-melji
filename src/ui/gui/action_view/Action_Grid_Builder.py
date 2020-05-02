#############################################################################
##  This code shoveswhatever is in an array of "LogInfo" into individual spaces - todo
##  Thanks - Micheal 2/1/20
#############################################################################
import sys
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QScrollArea, QWidget, QGridLayout, QLabel, QSizePolicy
#from LogDataType import LogInfo
from action_view.Action_Grid_Button_Builder import Get_Grid_Widgets
from action_view.Action_Sample_Data_Maker import Get_Sample_Widgets
from action_view.Action_Data_Maker import Get_Widgets
from random import seed,randint
import random

class Grid_Make(QScrollArea):   
    def __init__(self,text_array):
        super().__init__()
        self.widget = QWidget()               
        self.layoutgrid = QGridLayout()  
        self.layoutgrid.setSpacing(0)
        self.layoutgrid.setHorizontalSpacing(0)
        self.layoutgrid.setContentsMargins(0,0,0,0)
        i = 0
        n = 0
        data = Get_Grid_Widgets()
        o_data = Get_Widgets(text_array)
        arrayofwidgets = data.arrayofwidgets + o_data.arrayofwidgets

        numofsample = 0
        numofsample = randint(2, 98)
        #length
        x  = 0
        y=0

        for i in range(0,(len(arrayofwidgets))): #this code will detect what is in the datatype and put it into spaces in grid layout
            
            if x == 5:
                x=0 
                y+=1
            widgettoad = arrayofwidgets[i]
            self.layoutgrid.addWidget(widgettoad,y,x)
            
            x +=1
                
               
                    
        
        self.widget.setLayout(self.layoutgrid)
        self.widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setWidgetResizable(True)
        self.setWidget(self.widget)
        self.updateGeometry
        #this code sets borders to 1px
        #QRegExp regexp(".*border: *(\\d+)px.*");
        #if (regexp.indexIn(btn->styleSheet()) >= 0)
        #qDebug() << regexp.cap(1);

        return
