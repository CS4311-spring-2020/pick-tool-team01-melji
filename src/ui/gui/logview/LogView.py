#############################################################################
##  Please note that this is runnable and currently requires tweaking
##  The toolbar code is located in TemplateforPICK under InitUI 
##  Thanks - Micheal 2/1/20
#############################################################################
import sys

import os
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QVBoxLayout, QWidget,QToolBar,QLineEdit,QPushButton
from PyQt5.QtGui import QIcon
from logview.GridBuilder import GridMake
from popups.menupopup import OpenMenuPopup
from popups.ChangeVector import OpenVectorChangePopup
from popups.vector_configuration import OpenVectorConfigPopup
from popups.vc_manager import OpenVCPopup
from popups.timestamp_filter import OpenTSPopup
from popups.team_configuration import Configure_Team
from popups.remove_link import OpenRLPopup
from popups.relationships import OpenRelatePopup
from popups.node_creator import OpenNodeCreatePopup
from popups.IconConfiguration import IconConfiguration
from popups.FilterVector import OpenFilterVectorPopup
from popups.filterTeam import OpenFilterTeamPopup
from popups.filter_all import OpenFilterAllPopup
from popups.export_configuration import OpenExportConfigPopup
from popups.expand import OpenExpandPopup
from popups.directory_configuration import OpenDirectoryConfigPopup
from popups.connect_link import OpenconnectlinkPopup

global ex3
global window
class LogView(QMainWindow):
    
    def __init__(self,ex2): # this is to start grid builder before .show  ***note grid builder will require a array of data type called loginfo in the future***
        super().__init__()
        global ex3
        global window
        ex3 = ex2
        test = qApp
        test.setStyleSheet("")
        self.initUI()
        #this code runs GridBuilder
        #############################################################################
        self.grid = GridMake(self)
        _widget = QWidget()
        _layout = QVBoxLayout(_widget)
        _layout.addWidget(self.grid)
        self.setCentralWidget(_widget)
        #############################################################################
        self.setGeometry(500, 500, 500, 500)
        currtitle = 'PICK System'
        self.setWindowTitle(currtitle)  
        self.show()
        
        
    def initUI(self):               
        #this is where the toolbar elements are set up

        self.toolbar = self.addToolBar('UI')   #to-do lock toolbar
        
        fileAct = QAction(QIcon('bin/assets/file.png'), 'file', self)
        fileAct.setShortcut('Ctrl+X')
        #use following code for actions 
        fileAct.triggered.connect(OpenMenuPopup) 
        #self.toolbar.addAction(fileAct)

        saveAct = QAction(QIcon('bin/assets/save.png'), 'save', self)
        saveAct.setShortcut('Ctrl+S')
        #saveAct.triggered.connect(saveaction())
        #self.toolbar.addAction(saveAct)
        
        vcAct = QAction(QIcon('bin/assets/VC.jpg'), 'version control', self)
        vcAct.setShortcut('Ctrl+N')
        vcAct.triggered.connect(OpenVCPopup)
        #self.toolbar.addAction(vcAct)

        settingsAct = QAction(QIcon('bin/assets/settings.png'), 'settings', self)
        settingsAct.setShortcut('Ctrl+I')
        #settingsAct.triggered.connect(settingspopup())
        #self.toolbar.addAction(settingsAct)

        logviewAct = QAction(QIcon('bin/assets/logview.png'), 'log view', self)
        logviewAct.setShortcut('Ctrl+T')
        #logviewAct.triggered.connect(logview())
        #self.toolbar.addAction(logviewAct)

        historyAct = QAction(QIcon('bin/assets/history.png'), 'history', self)
        historyAct.setShortcut('Ctrl+H')
        #historyAct.triggered.connect(history popup())
        #self.toolbar.addAction(historyAct)

        redoAct = QAction(QIcon('bin/assets/redo.png'), 'redo change', self)
        redoAct.setShortcut('Ctrl+Y')
        #redoAct.triggered.connect(redo())
        #self.toolbar.addAction(redoAct)

        undoAct = QAction(QIcon('bin/assets/undo.png'), 'undo change', self)
        undoAct.setShortcut('Ctrl+Z')
        #undoAct.triggered.connect(undo())
        #self.toolbar.addAction(undoAct)

        

        #the following code adds the items to the toolbar
        self.toolbar.addAction(fileAct)
        #6self.toolbar.addAction(saveAct)
        self.toolbar.addAction(vcAct)
        #self.toolbar.addAction(settingsAct)
        #self.toolbar.addAction(logviewAct)
        self.toolbar.addAction(historyAct)
        self.toolbar.addAction(redoAct)
        self.toolbar.addAction(undoAct)

        self.toolbarlower = QToolBar()   #to-do lock toolbarlower
        
        filterAct = QAction(QIcon('bin/assets/filter.png'), 'file', self)
        filterAct.setShortcut('Ctrl+F')
        #use following code for actions 
        #fileAct.triggered.connect(filepopup()**note function call may not be correct**) 
        #self.toolbarlower.addAction(fileAct)

        saveAct = QAction(QIcon('bin/assets/save.png'), 'save', self)
        saveAct.setShortcut('Ctrl+S')
        #saveAct.triggered.connect(saveaction())
        #self.toolbarlower.addAction(saveAct)
        
        vcAct = QAction(QIcon('bin/assets/VC.jpg'), 'version control', self)
        vcAct.setShortcut('Ctrl+N')
        #vcAct.triggered.connect(versionpopup())
        #self.toolbarlower.addAction(vcAct)

        settingsAct = QAction(QIcon('bin/assets/settings.png'), 'settings', self)
        settingsAct.setShortcut('Ctrl+I')
        #settingsAct.triggered.connect(settingspopup())
        #self.toolbarlower.addAction(settingsAct)

        logviewAct = QAction(QIcon('bin/assets/logview.png'), 'log view', self)
        logviewAct.setShortcut('Ctrl+T')
        #logviewAct.triggered.connect(logview())
        #self.toolbarlower.addAction(logviewAct)

        historyAct = QAction(QIcon('bin/assets/history.png'), 'history', self)
        historyAct.setShortcut('Ctrl+H')
        #historyAct.triggered.connect(history popup())
        #self.toolbarlower.addAction(historyAct)

        redoAct = QAction(QIcon('bin/assets/redo.png'), 'redo change', self)
        redoAct.setShortcut('Ctrl+Y')
        #redoAct.triggered.connect(redo())
        #self.toolbarlower.addAction(redoAct)

        undoAct = QAction(QIcon('bin/assets/undo.png'), 'undo change', self)
        undoAct.setShortcut('Ctrl+Z')
        #undoAct.triggered.connect(undo())
        #self.toolbarlower.addAction(undoAct)

        

        #the following code adds the items to the toolbarlower
        self.toolbarlower.addAction(filterAct)

        self.lineEntry = QLineEdit(self)
        self.lineEntry.setMaximumWidth(200)
        self.toolbarlower.addWidget(self.lineEntry)
        
        self.searchbutton = QPushButton("Search")
        self.searchbutton.setMaximumWidth(150)
        self.toolbarlower.addWidget(self.searchbutton)

        self.changevectorbutton = QPushButton("Go To Vector")
        self.changevectorbutton.setMaximumWidth(150)
        global ex3
        global window
        self.changevectorbutton.clicked.connect(lambda:OpenVectorChangePopup(ex3,self))
        self.toolbarlower.addWidget(self.changevectorbutton)

        self.editvectorbutton = QPushButton("Edit Vector")
        self.editvectorbutton.setMaximumWidth(150)
        self.editvectorbutton.clicked.connect(OpenVectorConfigPopup)
        self.toolbarlower.addWidget(self.editvectorbutton)

        self.addvectorbutton = QPushButton("Add Vector")
        self.addvectorbutton.setMaximumWidth(150)
        self.toolbarlower.addWidget(self.addvectorbutton)

        self.removevectorbutton = QPushButton("Remove Vector")
        self.removevectorbutton.setMaximumWidth(150)
        self.toolbarlower.addWidget(self.removevectorbutton)

        self.addToolBarBreak()
        self.addToolBar(self.toolbarlower)