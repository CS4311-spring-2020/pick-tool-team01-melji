import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton, QHBoxLayout, QCheckBox ,QAction, QFrame, QSizePolicy
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.Qt import *

from popups.menupopup import OpenMenuPopup
#from popups.ChangeVector import OpenVectorChangePopup
from popups.vector_configuration import OpenVectorConfigPopup
from popups.vc_manager import OpenVCPopup
from popups.timestamp_filter import OpenTSPopup
from popups.remove_link import OpenRLPopup
from popups.relationships import OpenRelatePopup
from popups.IconConfiguration import IconConfiguration
from popups.FilterVector import OpenFilterVectorPopup
from popups.filterTeam import OpenFilterTeamPopup
from popups.filter_all import OpenFilterAllPopup
from popups.export_configuration import OpenExportConfigPopup
from popups.expand import OpenExpandPopup
from popups.connect_link import OpenconnectlinkPopup

widthofcolumns = 200
heightofrows=50
heightoftextrow = 25

class Get_Grid_Widgets(QFrame):

    def __init__(self, parent=None):
        super(Get_Grid_Widgets,self).__init__(parent)

        self.arrayofwidgets = [ Text_Widget("File Name"),Text_Widget("Line Number"),Text_Widget("Error Message"),Text_Widget("Validate"),Text_Widget("Invalidate"),
        Text_Widget(" "), Top_Grid("1_9","no","no"), Top_Grid("a_z","no","no"), Top_Grid("direction","true","true"), Top_Grid("direction","true","true")]
        return 


class Text_Widget(QFrame):

    def __init__(self,texttodisplay,parent=None):
        super(Text_Widget,self).__init__(parent)
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        #self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.setAlignment(Qt.AlignVCenter|Qt.AlignHCenter)
        self.setStyleSheet("border: 1px solid black;")
        self.textlable = QLabel(texttodisplay)
        self.textlable.setStyleSheet(" border: 0px; ")
        layout.addWidget(self.textlable)
        self.setLayout(layout)    
        self.setMaximumHeight(heightoftextrow)
        return


class Top_Grid(QFrame):
    global sortbuttonext
    global filterbuttonext
    global filterbuttonext
    global checkbuttonext
    
    def __init__(self, typeofsort,hascheck,hasfilter,parent=None):
        super(Top_Grid,self).__init__(parent)
        #return

    #def maketopwidget(self,typeofsort,hasfilter):
        
        global sortbuttonext
        global filterbuttonext
        button_width = 40
        button_min_size = 1
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setAlignment(Qt.AlignVCenter|Qt.AlignHCenter)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        #self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        if typeofsort == "1_9":

            self.sortbutton = QPushButton()
            sortbuttonext = self.sortbutton
            self.sortbutton.setIcon(QIcon(QPixmap("bin/assets/1_9sort.png")))
            self.sortbutton.setToolTip("This allows you to sort the current column")
            #self.sortbutton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.sortbutton.setMaximumWidth(button_width)
            self.sortbutton.setMinimumSize(button_min_size,button_min_size)
            self.sortbutton.setStyleSheet(" border: 0px; ")
            #self.sortbutton.clicked.connect(lambda:self.whichbtn(self.b2))
            layout.addWidget(self.sortbutton)

        elif typeofsort == "1_9v":

            self.sortbutton = QPushButton()
            sortbuttonext = self.sortbutton
            self.textlable = QLabel("Visibility")
            layout.addWidget(self.textlable)
            self.sortbutton.setIcon(QIcon(QPixmap("bin/assets/1_9sort.png")))
            self.sortbutton.setToolTip("This allows you to sort the current column")
            #self.sortbutton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.sortbutton.setMaximumWidth(button_width)
            self.sortbutton.setMinimumSize(button_min_size,button_min_size)
            self.sortbutton.setStyleSheet(" border: 0px; ")
            #self.sortbutton.clicked.connect(lambda:self.whichbtn(self.b2))
            layout.addWidget(self.sortbutton)


        elif typeofsort == "a_z":
            
            self.sortbutton = QPushButton()
            sortbuttonext = self.sortbutton
            self.sortbutton.setIcon(QIcon(QPixmap("bin/assets/a_zsort.png")))
            self.sortbutton.setToolTip("This allows you to sort the current column")
            #self.sortbutton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.sortbutton.setMaximumWidth(button_width)
            self.sortbutton.setMinimumSize(button_min_size,button_min_size)
            self.sortbutton.setStyleSheet(" border: 0px; ")
            #self.sortbutton.clicked.connect(lambda:self.whichbtn(self.b2))
            layout.addWidget(self.sortbutton)

        elif typeofsort == "direction":

            self.sortbutton = QPushButton()
            sortbuttonext = self.sortbutton
            self.sortbutton.setIcon(QIcon(QPixmap("bin/assets/upsort.png")))
            self.sortbutton.setToolTip("This allows you to sort the current column")
            #self.sortbutton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.sortbutton.setMaximumWidth(button_width)
            self.sortbutton.setMinimumSize(button_min_size,button_min_size)
            self.sortbutton.setStyleSheet(" border: 0px; ")
            #self.sortbutton.clicked.connect(lambda:self.whichbtn(self.b2))
            layout.addWidget(self.sortbutton)
        if hascheck == "true":
            
            self.checkbutton = QCheckBox()
            #self.checkbutton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

            checkbuttonext = self.checkbutton
            self.checkbutton.setToolTip("This allows you to change visiblilty in this and the graph")
            self.checkbutton.setChecked(True)
            self.checkbutton.setStyleSheet(" border: 0px; ")
            #self.checkbutton.stateChanged.connect(lambda:self.btnstate(self.b1))
            layout.addWidget(self.checkbutton)
        

        if hasfilter == "true":
            self.filterbutton = QPushButton()
            filterbuttonext = self.filterbutton
            #self.filterbutton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.filterbutton.setIcon(QIcon(QPixmap("bin/assets/filter.png")))
            self.filterbutton.setToolTip("This allows you to filter the current column")
            self.filterbutton.setMaximumWidth(button_width)
            self.filterbutton.setMinimumSize(button_min_size,button_min_size)
            #self.filterbutton.clicked.connect(lambda: OpenFilterAllPopup())
            self.filterbutton.setStyleSheet(" border: 0px; ")
            layout.addWidget(self.filterbutton)

        #super(TimeStampWidget,self).__init__(parent)


        
        self.setLayout(layout)
        #self.setFixedSize(widthofcolumns, heightofrows) 
        self.setMaximumHeight(heightofrows)
        return

    def returnbutton(self,typeofbutton):
        global sortbuttonext
        global filterbuttonext
        global checkbuttonext
        if typeofbutton == "sort":
            return sortbuttonext


        elif typeofbutton == "filter":
            return sortbuttonext


        elif typeofbutton == "check":
            return checkbuttonext

