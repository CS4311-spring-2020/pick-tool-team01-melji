#############################################################################
##  This code shoveswhatever is in an array of "LogInfo" into individual spaces - todo
##  Thanks - Micheal 2/1/20
#############################################################################
import sys
from PyQt5.QtWidgets import (QScrollArea,QWidget,QGridLayout,QLabel)
from logview.LogDataType import LogInfo
from logview.GridButtonBuilder import GetGridWidgets
from logview.SampleDataMaker import GetSampleWidgets
from random import seed,randint
import random

class GridMake(QScrollArea):   
    def __init__(self, parent=None):
        super(GridMake, self).__init__(parent)
        self.scrollmake()

    def scrollmake(self):
        self.widget = QWidget()                 
        self.layoutgrid = QGridLayout()  
        self.layoutgrid.setSpacing(0)
        self.layoutgrid.setHorizontalSpacing(0)
        i = 0
        n = 0
        data = GetGridWidgets()
        arrayofwidgets = data.arrayofwidgets
        
        numofsample = 0
        numofsample = randint(2, 98)

        for y in range(0,numofsample): #this code will detect what is in the datatype and put it into spaces in grid layout
            sampledata = GetSampleWidgets()
            for x in range(0,9):
                if y < 2:
                    widgettoad = arrayofwidgets[i]
                    self.layoutgrid.addWidget(widgettoad,y,x)
                    i = i+1

                else:
                    
                    arrayofsamplewidgets = sampledata.arrayofsamplewidgets
                    widgettoad = arrayofsamplewidgets[x]
                    self.layoutgrid.addWidget(widgettoad,y,x)
                    n = n+1
        
        self.widget.setLayout(self.layoutgrid)
        self.setWidgetResizable(True)
        self.setWidget(self.widget)
        #this code sets borders to 1px
        #QRegExp regexp(".*border: *(\\d+)px.*");
        #if (regexp.indexIn(btn->styleSheet()) >= 0)
        #qDebug() << regexp.cap(1);

        return
