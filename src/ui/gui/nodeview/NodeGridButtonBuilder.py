import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton, QHBoxLayout, QCheckBox ,QAction, QFrame, QSizePolicy
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.Qt import *

from popups.filter_all import OpenFilterAllPopup
from popups.export_configuration import OpenExportConfigPopup

widthofcolumns = 200
heightofrows=50
heightoftextrow = 25

class GetNodeGridWidgets(QFrame):

    def __init__(self, parent=None):
        super(GetNodeGridWidgets,self).__init__(parent)
        #NodeVisibilityTextWidget()NodeIDWidget()NodeNameWidget()NodeTimeStampWidget()NodeDescriptionWidget()NodeSourceWidget()NodeOriginDocumentWidget(), NodeLogEntryRefrenceWidget(),NodeIconWidget(),NodeIDTextWidget(), NodeNameTextWidget(), NodeTimeStampTextWidget(), NodeDescriptionTextWidget(), NodeSourceTextWidget(),  Node1TextWidget(), NodeOriginDocumentTextWidget(), NodeLogEntryRefrenceTextWidget(),NodeIconTextWidget()
        self.arrayofwidgets = [ NodeTextWidget("Visibility"), TopGrid("1_9","no"), TopGrid("a_z","no"), TopGrid("a_z","true"), TopGrid("a_z","no"),  
        TopGrid("a_z","true"), TopGrid("a_z","true"), TopGrid("a_z","true"), TopGrid("a_z","no"), TopGrid("a_z","true"), TopGrid("direction","no"), 
        EmptyWidget(), NodeTextWidget("Node ID"), NodeTextWidget("Node Name"), NodeTextWidget("TimeStamp"), NodeTextWidget("Description"), 
        NodeTextWidget("Source"), NodeTextWidget("Event Team"), NodeTextWidget("Location"), NodeTextWidget("Origin Document"), NodeTextWidget("Log Refrence"), NodeTextWidget("Icon")]
        return 
#TODO select all in empty space

class NodeTextWidget(QFrame):

    def __init__(self,texttodisplay,parent=None):
        super(NodeTextWidget,self).__init__(parent)
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


class TopGrid(QFrame):
    global nodesortbuttonext
    global nodefilterbuttonext
    global nodefilterbuttonext
    global nodecheckbuttonext
    
    def __init__(self, typeofsort,hasfilter,parent=None):
        super(TopGrid,self).__init__(parent)
        #return

    #def maketopwidget(self,typeofsort,hasfilter):
        
        global nodesortbuttonext
        global nodefilterbuttonext
        button_width = 40
        button_min_size = 1
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setAlignment(Qt.AlignVCenter|Qt.AlignHCenter)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        #self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        if typeofsort == "1_9":

            self.nodesortbutton = QPushButton()
            nodesortbuttonext = self.nodesortbutton
            self.nodesortbutton.setIcon(QIcon(QPixmap("bin/assets/1_9sort.png")))
            self.nodesortbutton.setToolTip("This allows you to sort the current column")
            #self.nodesortbutton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.nodesortbutton.setMaximumWidth(button_width)
            self.nodesortbutton.setMinimumSize(button_min_size,button_min_size)
            self.nodesortbutton.setStyleSheet(" border: 0px; ")
            #self.nodesortbutton.clicked.connect(lambda:self.whichbtn(self.b2))
            layout.addWidget(self.nodesortbutton)

        elif typeofsort == "1_9v":

            self.nodesortbutton = QPushButton()
            nodesortbuttonext = self.nodesortbutton
            self.textlable = QLabel("Visibility")
            layout.addWidget(self.textlable)
            self.nodesortbutton.setIcon(QIcon(QPixmap("bin/assets/1_9sort.png")))
            self.nodesortbutton.setToolTip("This allows you to sort the current column")
            #self.nodesortbutton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.nodesortbutton.setMaximumWidth(button_width)
            self.nodesortbutton.setMinimumSize(button_min_size,button_min_size)
            self.nodesortbutton.setStyleSheet(" border: 0px; ")
            #self.nodesortbutton.clicked.connect(lambda:self.whichbtn(self.b2))
            layout.addWidget(self.nodesortbutton)


        elif typeofsort == "a_z":
            
            self.nodesortbutton = QPushButton()
            nodesortbuttonext = self.nodesortbutton
            self.nodesortbutton.setIcon(QIcon(QPixmap("bin/assets/a_zsort.png")))
            self.nodesortbutton.setToolTip("This allows you to sort the current column")
            #self.nodesortbutton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.nodesortbutton.setMaximumWidth(button_width)
            self.nodesortbutton.setMinimumSize(button_min_size,button_min_size)
            self.nodesortbutton.setStyleSheet(" border: 0px; ")
            #self.nodesortbutton.clicked.connect(lambda:self.whichbtn(self.b2))
            layout.addWidget(self.nodesortbutton)

        elif typeofsort == "direction":

            self.nodesortbutton = QPushButton()
            nodesortbuttonext = self.nodesortbutton
            self.nodesortbutton.setIcon(QIcon(QPixmap("bin/assets/upsort.png")))
            self.nodesortbutton.setToolTip("This allows you to sort the current column")
            #self.nodesortbutton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.nodesortbutton.setMaximumWidth(button_width)
            self.nodesortbutton.setMinimumSize(button_min_size,button_min_size)
            self.nodesortbutton.setStyleSheet(" border: 0px; ")
            #self.nodesortbutton.clicked.connect(lambda:self.whichbtn(self.b2))
            layout.addWidget(self.nodesortbutton)
        global nodecheckbuttonext
        self.nodecheckbutton = QCheckBox()
        #self.nodecheckbutton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        nodecheckbuttonext = self.nodecheckbutton
        self.nodecheckbutton.setToolTip("This allows you to change visiblilty in this and the graph")
        self.nodecheckbutton.setChecked(True)
        self.nodecheckbutton.setStyleSheet(" border: 0px; ")
        #self.nodecheckbutton.stateChanged.connect(lambda:self.btnstate(self.b1))
        layout.addWidget(self.nodecheckbutton)
        

        if hasfilter == "true":
            self.nodefilterbutton = QPushButton()
            nodefilterbuttonext = self.nodefilterbutton
            #self.nodefilterbutton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.nodefilterbutton.setIcon(QIcon(QPixmap("bin/assets/filter.png")))
            self.nodefilterbutton.setToolTip("This allows you to filter the current column")
            self.nodefilterbutton.setMaximumWidth(button_width)
            self.nodefilterbutton.setMinimumSize(button_min_size,button_min_size)
            #self.nodefilterbutton.clicked.connect(lambda: OpenFilterAllPopup())
            self.nodefilterbutton.setStyleSheet(" border: 0px; ")
            layout.addWidget(self.nodefilterbutton)

        #super(NodeTimeStampWidget,self).__init__(parent)


        
        self.setLayout(layout)
        #self.setFixedSize(widthofcolumns, heightofrows) 
        self.setMaximumHeight(heightofrows)
        return

    def returnbutton(self,typeofbutton):
        global nodesortbuttonext
        global nodefilterbuttonext
        global nodecheckbuttonext
        if typeofbutton == "sort":
            return nodesortbuttonext


        elif typeofbutton == "filter":
            return nodesortbuttonext


        elif typeofbutton == "check":
            return nodecheckbuttonext


class NodeVisibilityTextWidget(QFrame):

    def __init__(self, parent=None):
        super(NodeVisibilityTextWidget,self).__init__(parent)

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        self.textlable = QLabel("Visibility")
        layout.addWidget(self.textlable)
        self.setLayout(layout)  
        self.setMaximumHeight(heightoftextrow)
        return



class NodeIDWidget(QFrame):
    def __init__(self, parent=None):
        super(NodeIDWidget,self).__init__(parent)

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")

        b ="Visibility"
        self.textlable = QLabel(b)
        layout.addWidget(self.textlable)
        
        self.nodeidsortbutton = QPushButton()
        self.nodeidsortbutton.setIcon(QIcon(QPixmap("bin/assets/1_9sort.png")))
        #self.b2.clicked.connect(lambda:self.whichbtn(self.b2))
        layout.addWidget(self.nodeidsortbutton)

        self.nodeidvisibilitybutton = QCheckBox()
        self.nodeidvisibilitybutton.setToolTip("This allows you to change visiblilty in this and the graph")
        self.nodeidvisibilitybutton.setChecked(True)
        #self.nodeidvisibilitybutton.stateChanged.connect(lambda:self.btnstate(self.b1))
        layout.addWidget(self.nodeidvisibilitybutton)

        
        self.setLayout(layout)
        self.setMaximumHeight(heightofrows)
        #self.setFixedSize(widthofcolumns, heightofrows) 
        return



class NodeIDTextWidget(QFrame):

    def __init__(self, parent=None):
        super(NodeIDTextWidget,self).__init__(parent)
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        self.textlable = QLabel("Node ID")
        layout.addWidget(self.textlable)
        self.setLayout(layout)    
        self.setMaximumHeight(heightoftextrow)
        return



class NodeNameWidget(QFrame):

    def __init__(self, parent=None):
        super(NodeNameWidget,self).__init__(parent)

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        
        self.nodenamesortbutton = QPushButton()
        self.nodenamesortbutton.setIcon(QIcon(QPixmap("bin/assets/a_zsort.png")))
        #self.b2.clicked.connect(lambda:self.whichbtn(self.b2))
        layout.addWidget(self.nodenamesortbutton)

        self.nodenamevisibilitybutton = QCheckBox()
        self.nodenamevisibilitybutton.setToolTip("This allows you to change visiblilty in this and the graph")
        self.nodenamevisibilitybutton.setChecked(True)
        #self.nodenamevisibilitybutton.stateChanged.connect(lambda:self.btnstate(self.b1))
        layout.addWidget(self.nodenamevisibilitybutton)

        
        self.setLayout(layout)
        #self.setFixedSize(widthofcolumns, heightofrows) 
        self.setMaximumHeight(heightofrows)
        return



class NodeNameTextWidget(QFrame):

    def __init__(self, parent=None):
        super(NodeNameTextWidget,self).__init__(parent)

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        self.textlable = QLabel("NodeName")
        layout.addWidget(self.textlable)
        self.setLayout(layout)  
        self.setMaximumHeight(heightoftextrow)
        return



class NodeTimeStampWidget(QFrame):

    def __init__(self, parent=None):
        super(NodeTimeStampWidget,self).__init__(parent)

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        
        self.nodetimestampsortbutton = QPushButton()
        self.nodetimestampsortbutton.setIcon(QIcon(QPixmap("bin/assets/1_9sort.png")))
        #self.nodetimestampsortbutton.clicked.connect(lambda:self.whichbtn(self.b2))
        layout.addWidget(self.nodetimestampsortbutton)
        
        self.nodetimestampvisibilitybutton = QCheckBox()
        self.nodetimestampvisibilitybutton.setToolTip("This allows you to change visiblilty in this and the graph")
        self.nodetimestampvisibilitybutton.setChecked(True)
        #self.nodetimestampvisibilitybutton.stateChanged.connect(lambda:self.btnstate(self.b1))
        layout.addWidget(self.nodetimestampvisibilitybutton)

        self.nodetimestampfilterbutton = QPushButton()
        self.nodetimestampfilterbutton.setIcon(QIcon(QPixmap("bin/assets/filter.png")))
        self.nodetimestampfilterbutton.clicked.connect(lambda: OpenFilterAllPopup())
        
        #self.pushButton.clicked.connect(lambda: OpenExportConfigPopup())
        #self.nodetimestampfilterbutton.clicked.connect(lambda:self.whichbtn(self.b2))
        layout.addWidget(self.nodetimestampfilterbutton)

        
        self.setLayout(layout)
        #self.setFixedSize(widthofcolumns, heightofrows) 
        self.setMaximumHeight(heightofrows)
        return



class NodeTimeStampTextWidget(QFrame):

    def __init__(self, parent=None):
        super(NodeTimeStampTextWidget,self).__init__(parent)

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        self.textlable = QLabel("TimeStamp")
        layout.addWidget(self.textlable)
        self.setLayout(layout)  
        self.setMaximumHeight(heightoftextrow)
        return



class NodeDescriptionWidget(QFrame):

    def __init__(self, parent=None):
        super(NodeDescriptionWidget,self).__init__(parent)

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        
        self.nodedescriptionsortbutton = QPushButton()
        self.nodedescriptionsortbutton.setIcon(QIcon(QPixmap("bin/assets/upsort.png")))
        #self.nodedescriptionsortbutton.clicked.connect(lambda:self.whichbtn(self.b2))
        layout.addWidget(self.nodedescriptionsortbutton)
        


        self.nodedescriptionvisibilitybutton = QCheckBox()
        self.nodedescriptionvisibilitybutton.setToolTip("This allows you to change visiblilty in this and the graph")
        self.nodedescriptionvisibilitybutton.setChecked(True)
        #self.nodedescriptionvisibilitybutton.stateChanged.connect(lambda:self.btnstate(self.b1))
        layout.addWidget(self.nodedescriptionvisibilitybutton)


        
        self.setLayout(layout)
        #self.setFixedSize(widthofcolumns, heightofrows) 
        self.setMaximumHeight(heightofrows)

        return



class NodeDescriptionTextWidget(QFrame):

    def __init__(self, parent=None):
        super(NodeDescriptionTextWidget,self).__init__(parent)

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        self.textlable = QLabel("Description")
        layout.addWidget(self.textlable)
        self.setLayout(layout)  
        self.setMaximumHeight(heightoftextrow)
        return


class EmptyWidget(QFrame):

    def __init__(self, parent=None):
        super(EmptyWidget,self).__init__(parent)

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        self.textlable = QLabel("")
        layout.addWidget(self.textlable)
        self.setLayout(layout)  
        self.setMaximumHeight(heightoftextrow)
        return

class NodeSourceWidget(QFrame):

    def __init__(self, parent=None):
        super(NodeSourceWidget,self).__init__(parent)

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        
        self.nodeeventteamsortbutton = QPushButton()
        self.nodeeventteamsortbutton.setIcon(QIcon(QPixmap("bin/assets/a_zsort.png")))
        #self.nodeeventteamsortbutton.clicked.connect(lambda:self.whichbtn(self.b2))
        layout.addWidget(self.nodeeventteamsortbutton)
        
        self.nodeeventteamvisibilitybutton = QCheckBox()
        self.nodeeventteamvisibilitybutton.setToolTip("This allows you to change visiblilty in this and the graph")
        self.nodeeventteamvisibilitybutton.setChecked(True)
        #self.nodeeventteamvisibilitybutton.stateChanged.connect(lambda:self.btnstate(self.b1))
        layout.addWidget(self.nodeeventteamvisibilitybutton)

        self.nodeeventteamfilterbutton = QPushButton()
        self.nodeeventteamfilterbutton.setIcon(QIcon(QPixmap("bin/assets/filter.png")))
        self.nodeeventteamfilterbutton.clicked.connect(lambda: OpenFilterAllPopup())
        #self.nodeeventteamfilterbutton.clicked.connect(lambda:self.whichbtn(self.b2))
        layout.addWidget(self.nodeeventteamfilterbutton)

        
        self.setLayout(layout)
        #self.setFixedSize(widthofcolumns, heightofrows) 
        self.setMaximumHeight(heightofrows)
        return



class NodeSourceTextWidget(QFrame):

    def __init__(self, parent=None):
        super(NodeSourceTextWidget,self).__init__(parent)

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)

        self.setStyleSheet("border: 1px solid black;")
        self.textlable = QLabel("Source")

        layout.addWidget(self.textlable)
        self.setLayout(layout)  
        self.setMaximumHeight(heightoftextrow)

        return


class NodeIconWidget(QFrame):

    def __init__(self, parent=None):
        super(NodeIconWidget,self).__init__(parent)

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        
        self.nodeiconsortbutton = QPushButton()
        self.nodeiconsortbutton.setIcon(QIcon(QPixmap("bin/assets/upsort.png")))
        #self.nodeiconsortbutton.clicked.connect(lambda:self.whichbtn(self.b2))
        layout.addWidget(self.nodeiconsortbutton)
        
        self.nodeiconvisibilitybutton = QCheckBox()
        self.nodeiconvisibilitybutton.setToolTip("This allows you to change visiblilty in this and the graph")
        self.nodeiconvisibilitybutton.setChecked(True)
        #self.nodeiconvisibilitybutton.stateChanged.connect(lambda:self.btnstate(self.b1))
        layout.addWidget(self.nodeiconvisibilitybutton)

        
        self.setLayout(layout)
        #self.setFixedSize(widthofcolumns, heightofrows) 
        self.setMaximumHeight(heightofrows)
        return



class NodeIconTextWidget(QFrame):

    def __init__(self, parent=None):
        super(NodeIconTextWidget,self).__init__(parent)
        
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        self.textlable = QLabel("Icon")
        layout.addWidget(self.textlable)
        self.setLayout(layout)
        self.setMaximumHeight(heightoftextrow)


class Node1TextWidget(QFrame):

    def __init__(self, parent=None):
        super(Node1TextWidget,self).__init__(parent)
        
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        self.textlable = QLabel("Event Team")
        layout.addWidget(self.textlable)
        self.setLayout(layout)
        self.setMaximumHeight(heightoftextrow)



class NodeOriginDocumentWidget(QFrame):

    def __init__(self, parent=None):
        super(NodeOriginDocumentWidget,self).__init__(parent)

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        
        self.nodeorigindocumentsortbutton = QPushButton()
        self.nodeorigindocumentsortbutton.setIcon(QIcon(QPixmap("bin/assets/a_zsort.png")))
        #self.nodeorigindocumentsortbutton.clicked.connect(lambda:self.whichbtn(self.b2))
        layout.addWidget(self.nodeorigindocumentsortbutton)
        
        self.nodeorigindocumentvisibilitybutton = QCheckBox()
        self.nodeorigindocumentvisibilitybutton.setToolTip("This allows you to change visiblilty in this and the graph")
        self.nodeorigindocumentvisibilitybutton.setChecked(True)
        #self.nodeorigindocumentvisibilitybutton.stateChanged.connect(lambda:self.btnstate(self.b1))
        layout.addWidget(self.nodeorigindocumentvisibilitybutton)

        
        self.setLayout(layout)
        #self.setFixedSize(widthofcolumns, heightofrows) 
        self.setMaximumHeight(heightofrows)
        return
        


class NodeOriginDocumentTextWidget(QFrame):

    def __init__(self, parent=None):
        super(NodeOriginDocumentTextWidget,self).__init__(parent)

        
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        self.textlable = QLabel("Origin Document")
        layout.addWidget(self.textlable)
        self.setLayout(layout)
        self.setMaximumHeight(heightoftextrow)
        return


        
class NodeLogEntryRefrenceWidget(QFrame):

    def __init__(self, parent=None):
        super(NodeLogEntryRefrenceWidget,self).__init__(parent)

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        
        self.nodevectorsattachedtosortbutton = QPushButton()
        self.nodevectorsattachedtosortbutton.setIcon(QIcon(QPixmap("bin/assets/a_zsort.png")))
        #self.nodevectorsattachedtosortbutton.clicked.connect(lambda:self.whichbtn(self.b2))
        layout.addWidget(self.nodevectorsattachedtosortbutton)
        
        self.nodevectorsattachedtovisibilitybutton = QCheckBox()
        self.nodevectorsattachedtovisibilitybutton.setToolTip("This allows you to change visiblilty in this and the graph")
        self.nodevectorsattachedtovisibilitybutton.setChecked(True)
        #self.nodevectorsattachedtovisibilitybutton.stateChanged.connect(lambda:self.btnstate(self.b1))
        layout.addWidget(self.nodevectorsattachedtovisibilitybutton)

        self.nodevectorsattachedtofilterbutton = QPushButton()
        self.nodevectorsattachedtofilterbutton.setIcon(QIcon(QPixmap("bin/assets/filter.png")))
        self.nodevectorsattachedtofilterbutton.clicked.connect(lambda: OpenFilterAllPopup())
        #self.nodevectorsattachedtofilterbutton.clicked.connect(lambda:self.whichbtn(self.b2))
        layout.addWidget(self.nodevectorsattachedtofilterbutton)

        
        self.setLayout(layout)
        #self.setFixedSize(widthofcolumns, heightofrows) 
        self.setMaximumHeight(heightofrows)
        return


        
class NodeLogEntryRefrenceTextWidget(QFrame):

    def __init__(self, parent=None):
        super(NodeLogEntryRefrenceTextWidget,self).__init__(parent)
        
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        self.textlable = QLabel("Log Refrence")
        layout.addWidget(self.textlable)
        self.setLayout(layout)
        self.setMaximumHeight(heightoftextrow)
        return