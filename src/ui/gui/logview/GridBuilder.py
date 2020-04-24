#############################################################################
##  This code shoveswhatever is in an array of "LogInfo" into individual spaces - todo
##  Thanks - Micheal 2/1/20
#############################################################################
import sys
from PyQt5.QtWidgets import (QScrollArea,QWidget,QGridLayout,QLabel)
#from logview.LogDataType import LogInfo
from logview.GridButtonBuilder import GetGridWidgets
from logview.SampleDataMaker import GetSampleWidgets
from random import seed,randint
import random

from logview.splunk_data_maker import SplunkData
from services import intake_service
from services.intake_service import IntakeService


class GridMake(QScrollArea):
    def __init__(self,dir_conf, parent=None):
        super(GridMake, self).__init__(parent)
        self.scrollmake(dir_conf)

    def scrollmake(self,dir_conf):
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

        self.intake_service = IntakeService()
        location = dir_conf.Return_Root()+"/"
        self.entries = self.intake_service.ingest_files(location)
            #"/Users/eddie/Documents/SchoolProjects/pick-tool-team01-melji/example/")
        for y in range(len(self.entries)): #this code will detect what is in the datatype and put it into spaces in grid layout
            sampledata = SplunkData(self.entries[y])
            for x in range(0,10):
                if y < 2:
                    widgettoad = arrayofwidgets[i]
                    self.layoutgrid.addWidget(widgettoad,y,x)
                    i = i+1

                else:
                    
                    arrayofsamplewidgets = sampledata.splunk_data
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
