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
from random import seed,randint
import random

class Grid_Make(QScrollArea):   
    def __init__(self, parent=None):
        super(Grid_Make, self).__init__(parent)
        self.scroll_make()

    def scroll_make(self):
        self.widget = QWidget()               
        self.layoutgrid = QGridLayout()  
        self.layoutgrid.setSpacing(0)
        self.layoutgrid.setHorizontalSpacing(0)
        self.layoutgrid.setContentsMargins(0,0,0,0)
        i = 0
        n = 0
        data = Get_Grid_Widgets()
        arrayofwidgets = data.arrayofwidgets
        
        numofsample = 0
        numofsample = randint(2, 98)
        
        for y in range(0,numofsample): #this code will detect what is in the datatype and put it into spaces in grid layout
            sampledata = Get_Sample_Widgets()
            for x in range(0,5):
                if y < 2:
                    widgettoad = arrayofwidgets[i]
                    self.layoutgrid.addWidget(widgettoad,y,x)
                    i = i+1
               
                    arrayofsamplewidgets = sampledata.arrayofsamplewidgets

                else: 
                    if x < 3:
                        arrayofsamplewidgets = sampledata.arrayofsamplewidgets
                        widgettoad = arrayofsamplewidgets[x]
                        self.layoutgrid.addWidget(widgettoad,y,x)
                    elif x == 3:
                        arrayofsamplewidgets = sampledata.arrayofsamplewidgets
                        widgettoad = arrayofsamplewidgets[x]
                        self.layoutgrid.addWidget(widgettoad,y,x,1,2)

                    n = n+1
        
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
