#############################################################################
##  This code shoveswhatever is in an array of "LogInfo" into individual spaces - todo
##  Thanks - Micheal 2/1/20
#############################################################################
import sys
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QScrollArea, QWidget, QGridLayout, QLabel, QSizePolicy
from nodeview.NodeGridButtonBuilder import GetNodeGridWidgets
from nodeview.SampleNodeDataMaker import GetNodeSampleWidgets
from nodeview.SampleNodeDataMakerSplunk import GetNodeWidgets
from services.intake_service import IntakeService
from random import seed,randint
import random
 
class NodeGridMake(QScrollArea):   
    def __init__(self, parent=None):
        super(NodeGridMake, self).__init__(parent)
        self.scrollmake()

    def scrollmake(self):
        self.widget = QWidget()               
        self.layoutgrid = QGridLayout()  
        self.layoutgrid.setSpacing(0)
        self.layoutgrid.setHorizontalSpacing(0)
        self.layoutgrid.setContentsMargins(0,0,0,0)
        i = 0
        n = 0
        data = GetNodeGridWidgets()
        arrayofwidgets = data.arrayofwidgets
        
        numofsample = 0
        numofsample = randint(2, 98)
        
        #for y in range(0,numofsample): #this code will detect what is in the datatype and put it into spaces in grid layout
         #   sampledata = GetNodeSampleWidgets()
          #  for x in range(0,11):
           #     if y < 2:
            #        widgettoad = arrayofwidgets[i]
             #       self.layoutgrid.addWidget(widgettoad,y,x)
              #      i = i+1
        
        self.intake_service = IntakeService()
        self.entries = self.intake_service.ingest_files(
            "/Users/eddie/Documents/SchoolProjects/pick-tool-team01-melji/example/")
        for y in range(len(self.entries)): #this code will detect what is in the datatype and put it into spaces in grid layout
            sampledata = GetNodeWidgets(self.entries[y])
            for x in range(0,10):
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
        self.widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setWidgetResizable(True)
        self.setWidget(self.widget)
        self.updateGeometry
        #this code sets borders to 1px
        #QRegExp regexp(".*border: *(\\d+)px.*");
        #if (regexp.indexIn(btn->styleSheet()) >= 0)
        #qDebug() << regexp.cap(1);

        return
