import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton, QHBoxLayout, QCheckBox ,QAction, QFrame
from PyQt5.QtGui import QIcon, QPixmap
from popups.filter_all import OpenFilterAllPopup

widthofcolumns = 200
heightofrows=50
heightoftextrow = 25

class GetGridWidgets(QFrame):

    def __init__(self, parent=None):
        super(GetGridWidgets,self).__init__(parent)
        
        self.arrayofwidgets = [ LogIDWidget(), LogNameWidget(), TimeStampWidget(), DescriptionWidget(), ReporterWidget(), EventTeamWidget(),EventTeamWidget(), 
        IconWidget(),OriginDocumentWidget(),VectorsAttachedToWidget(), LogIDTextWidget(), LogNameTextWidget(), TimeStampTextWidget(), 
        DescriptionTextWidget(), ReporterTextWidget(), EventTeamTextWidget(), LogTextWidget("Location"), IconTextWidget(), OriginDocumentTextWidget(), VectorsAttachedToTextWidget()]
        return 
    
class LogTextWidget(QFrame):

    def __init__(self,texttodisplay,parent=None):
        super(LogTextWidget,self).__init__(parent)
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        self.textlable = QLabel(texttodisplay)
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
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")

        if typeofsort == "1_9":

            self.nodesortbutton = QPushButton()
            nodesortbuttonext = self.nodesortbutton
            self.nodesortbutton.setIcon(QIcon(QPixmap("bin/assets/1_9sort.png")))
            self.nodesortbutton.setToolTip("This allows you to sort the current column")
            #self.nodesortbutton.clicked.connect(lambda:self.whichbtn(self.b2))
            layout.addWidget(self.nodesortbutton)


        elif typeofsort == "a_z":
            
            self.nodesortbutton = QPushButton()
            nodesortbuttonext = self.nodesortbutton
            self.nodesortbutton.setIcon(QIcon(QPixmap("bin/assets/a_zsort.png")))
            self.nodesortbutton.setToolTip("This allows you to sort the current column")
            #self.nodesortbutton.clicked.connect(lambda:self.whichbtn(self.b2))
            layout.addWidget(self.nodesortbutton)

        elif typeofsort == "upsort":

            self.nodesortbutton = QPushButton()
            nodesortbuttonext = self.nodesortbutton
            self.nodesortbutton.setIcon(QIcon(QPixmap("bin/assets/upsort.png")))
            self.nodesortbutton.setToolTip("This allows you to sort the current column")
            #self.nodesortbutton.clicked.connect(lambda:self.whichbtn(self.b2))
            layout.addWidget(self.nodesortbutton)
        
        global nodecheckbuttonext
        self.nodecheckbutton = QCheckBox()
        nodecheckbuttonext = self.nodecheckbutton
        self.nodecheckbutton.setToolTip("This allows you to change visiblilty in this and the graph")
        self.nodecheckbutton.setChecked(True)
        #self.nodecheckbutton.stateChanged.connect(lambda:self.btnstate(self.b1))
        layout.addWidget(self.nodecheckbutton)
        

        if hasfilter == "true":
            self.nodefilterbutton = QPushButton()
            nodefilterbuttonext = self.nodefilterbutton
            self.nodefilterbutton.setIcon(QIcon(QPixmap("bin/assets/filter.png")))
            self.nodesortbutton.setToolTip("This allows you to filter the current column")
            #self.nodefilterbutton.clicked.connect(lambda: OpenFilterAllPopup())
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

class LogIDWidget(QFrame):
    def __init__(self, parent=None):
        super(LogIDWidget,self).__init__(parent)

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")

        b ="Visibility"
        self.textlable = QLabel(b)
        layout.addWidget(self.textlable)
        
        self.logidsortbutton = QPushButton()
        self.logidsortbutton.setIcon(QIcon(QPixmap("bin/assets/1_9sort.png")))
        #self.b2.clicked.connect(lambda:self.whichbtn(self.b2))
        layout.addWidget(self.logidsortbutton)

        self.logidvisibilitybutton = QCheckBox()
        self.logidvisibilitybutton.setToolTip("This allows you to change visiblilty in this and the graph")
        self.logidvisibilitybutton.setChecked(True)
        #self.logidvisibilitybutton.stateChanged.connect(lambda:self.btnstate(self.b1))
        layout.addWidget(self.logidvisibilitybutton)

        
        self.setLayout(layout)
        self.setMaximumHeight(heightofrows)
        #self.setFixedSize(widthofcolumns, heightofrows) 
        return



class LogIDTextWidget(QFrame):

    def __init__(self, parent=None):
        super(LogIDTextWidget,self).__init__(parent)
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        self.textlable = QLabel("Log ID")
        layout.addWidget(self.textlable)
        self.setLayout(layout)    
        self.setMaximumHeight(heightoftextrow)
        return



class LogNameWidget(QFrame):

    def __init__(self, parent=None):
        super(LogNameWidget,self).__init__(parent)

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        
        self.lognamesortbutton = QPushButton()
        self.lognamesortbutton.setIcon(QIcon(QPixmap("bin/assets/a_zsort.png")))
        #self.b2.clicked.connect(lambda:self.whichbtn(self.b2))
        layout.addWidget(self.lognamesortbutton)

        self.lognamevisibilitybutton = QCheckBox()
        self.lognamevisibilitybutton.setToolTip("This allows you to change visiblilty in this and the graph")
        self.lognamevisibilitybutton.setChecked(True)
        #self.lognamevisibilitybutton.stateChanged.connect(lambda:self.btnstate(self.b1))
        layout.addWidget(self.lognamevisibilitybutton)

        
        self.setLayout(layout)
        #self.setFixedSize(widthofcolumns, heightofrows) 
        self.setMaximumHeight(heightofrows)
        return



class LogNameTextWidget(QFrame):

    def __init__(self, parent=None):
        super(LogNameTextWidget,self).__init__(parent)

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        self.textlable = QLabel("LogID")
        layout.addWidget(self.textlable)
        self.setLayout(layout)  
        self.setMaximumHeight(heightoftextrow)
        return



class TimeStampWidget(QFrame):

    def __init__(self, parent=None):
        super(TimeStampWidget,self).__init__(parent)

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        
        self.logtimestampsortbutton = QPushButton()
        self.logtimestampsortbutton.setIcon(QIcon(QPixmap("bin/assets/1_9sort.png")))
        #self.logtimestampsortbutton.clicked.connect(lambda:self.whichbtn(self.b2))
        layout.addWidget(self.logtimestampsortbutton)
        
        self.logtimestampvisibilitybutton = QCheckBox()
        self.logtimestampvisibilitybutton.setToolTip("This allows you to change visiblilty in this and the graph")
        self.logtimestampvisibilitybutton.setChecked(True)
        #self.logtimestampvisibilitybutton.stateChanged.connect(lambda:self.btnstate(self.b1))
        layout.addWidget(self.logtimestampvisibilitybutton)

        self.logtimestampfilterbutton = QPushButton()
        self.logtimestampfilterbutton.setIcon(QIcon(QPixmap("bin/assets/filter.png")))
        self.logtimestampfilterbutton.clicked.connect(lambda: OpenFilterAllPopup())
        layout.addWidget(self.logtimestampfilterbutton)

        
        self.setLayout(layout)
        #self.setFixedSize(widthofcolumns, heightofrows) 
        self.setMaximumHeight(heightofrows)
        return



class TimeStampTextWidget(QFrame):

    def __init__(self, parent=None):
        super(TimeStampTextWidget,self).__init__(parent)

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        self.textlable = QLabel("TimeStamp")
        layout.addWidget(self.textlable)
        self.setLayout(layout)  
        self.setMaximumHeight(heightoftextrow)
        return
        


class DescriptionWidget(QFrame):

    def __init__(self, parent=None):
        super(DescriptionWidget,self).__init__(parent)

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        
        self.logdescriptionsortbutton = QPushButton()
        self.logdescriptionsortbutton.setIcon(QIcon(QPixmap("bin/assets/upsort.png")))
        #self.logdescriptionsortbutton.clicked.connect(lambda:self.whichbtn(self.b2))
        layout.addWidget(self.logdescriptionsortbutton)
        
        self.logdescriptionvisibilitybutton = QCheckBox()
        self.logdescriptionvisibilitybutton.setToolTip("This allows you to change visiblilty in this and the graph")
        self.logdescriptionvisibilitybutton.setChecked(True)
        #self.logdescriptionvisibilitybutton.stateChanged.connect(lambda:self.btnstate(self.b1))
        layout.addWidget(self.logdescriptionvisibilitybutton)


        
        self.setLayout(layout)
        #self.setFixedSize(widthofcolumns, heightofrows) 
        self.setMaximumHeight(heightofrows)
        return



class DescriptionTextWidget(QFrame):

    def __init__(self, parent=None):
        super(DescriptionTextWidget,self).__init__(parent)

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        self.textlable = QLabel("Description")
        layout.addWidget(self.textlable)
        self.setLayout(layout)
        self.setMaximumHeight(heightoftextrow)
        return



class ReporterWidget(QFrame):

    def __init__(self, parent=None):
        super(ReporterWidget,self).__init__(parent)

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        
        self.logreportersortbutton = QPushButton()
        self.logreportersortbutton.setIcon(QIcon(QPixmap("bin/assets/a_zsort.png")))
        #self.logreportersortbutton.clicked.connect(lambda:self.whichbtn(self.b2))
        layout.addWidget(self.logreportersortbutton)
        
        self.logreportervisibilitybutton = QCheckBox()
        self.logreportervisibilitybutton.setToolTip("This allows you to change visiblilty in this and the graph")
        self.logreportervisibilitybutton.setChecked(True)
        #self.logreportervisibilitybutton.stateChanged.connect(lambda:self.btnstate(self.b1))
        layout.addWidget(self.logreportervisibilitybutton)

        self.logreporterfilterbutton = QPushButton()
        self.logreporterfilterbutton.setIcon(QIcon(QPixmap("bin/assets/filter.png")))
        self.logreporterfilterbutton.clicked.connect(lambda: OpenFilterAllPopup())
        layout.addWidget(self.logreporterfilterbutton)

        
        self.setLayout(layout)
        #self.setFixedSize(widthofcolumns, heightofrows) 
        self.setMaximumHeight(heightofrows)
        return



class ReporterTextWidget(QFrame):

    def __init__(self, parent=None):
        super(ReporterTextWidget,self).__init__(parent)

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        self.textlable = QLabel("Reporter")
        layout.addWidget(self.textlable)
        self.setLayout(layout)  
        self.setMaximumHeight(heightoftextrow)
        return



class EventTeamWidget(QFrame):

    def __init__(self, parent=None):
        super(EventTeamWidget,self).__init__(parent)

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        
        self.logeventteamsortbutton = QPushButton()
        self.logeventteamsortbutton.setIcon(QIcon(QPixmap("bin/assets/a_zsort.png")))
        #self.logeventteamsortbutton.clicked.connect(lambda:self.whichbtn(self.b2))
        layout.addWidget(self.logeventteamsortbutton)
        
        self.logeventteamvisibilitybutton = QCheckBox()
        self.logeventteamvisibilitybutton.setToolTip("This allows you to change visiblilty in this and the graph")
        self.logeventteamvisibilitybutton.setChecked(True)
        #self.logeventteamvisibilitybutton.stateChanged.connect(lambda:self.btnstate(self.b1))
        layout.addWidget(self.logeventteamvisibilitybutton)

        self.logeventteamfilterbutton = QPushButton()
        self.logeventteamfilterbutton.setIcon(QIcon(QPixmap("bin/assets/filter.png")))
        self.logeventteamfilterbutton.clicked.connect(lambda: OpenFilterAllPopup())
        layout.addWidget(self.logeventteamfilterbutton)

        
        self.setLayout(layout)
        #self.setFixedSize(widthofcolumns, heightofrows) 
        self.setMaximumHeight(heightofrows)
        return



class EventTeamTextWidget(QFrame):

    def __init__(self, parent=None):
        super(EventTeamTextWidget,self).__init__(parent)

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        self.textlable = QLabel("Event Team")
        layout.addWidget(self.textlable)
        self.setLayout(layout)  
        self.setMaximumHeight(heightoftextrow)
        return



class IconWidget(QFrame):

    def __init__(self, parent=None):
        super(IconWidget,self).__init__(parent)

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        
        self.logiconsortbutton = QPushButton()
        self.logiconsortbutton.setIcon(QIcon(QPixmap("bin/assets/upsort.png")))
        #self.logiconsortbutton.clicked.connect(lambda:self.whichbtn(self.b2))
        layout.addWidget(self.logiconsortbutton)
        
        self.logiconvisibilitybutton = QCheckBox()
        self.logiconvisibilitybutton.setToolTip("This allows you to change visiblilty in this and the graph")
        self.logiconvisibilitybutton.setChecked(True)
        #self.logiconvisibilitybutton.stateChanged.connect(lambda:self.btnstate(self.b1))
        layout.addWidget(self.logiconvisibilitybutton)

        
        self.setLayout(layout)
        #self.setFixedSize(widthofcolumns, heightofrows) 
        self.setMaximumHeight(heightofrows)
        return



class IconTextWidget(QFrame):

    def __init__(self, parent=None):
        super(IconTextWidget,self).__init__(parent)
        
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        self.textlable = QLabel("Icon")
        layout.addWidget(self.textlable)
        self.setLayout(layout)
        self.setMaximumHeight(heightoftextrow)



class OriginDocumentWidget(QFrame):

    def __init__(self, parent=None):
        super(OriginDocumentWidget,self).__init__(parent)

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        
        self.logorigindocumentsortbutton = QPushButton()
        self.logorigindocumentsortbutton.setIcon(QIcon(QPixmap("bin/assets/a_zsort.png")))
        #self.logorigindocumentsortbutton.clicked.connect(lambda:self.whichbtn(self.b2))
        layout.addWidget(self.logorigindocumentsortbutton)
        
        self.logorigindocumentvisibilitybutton = QCheckBox()
        self.logorigindocumentvisibilitybutton.setToolTip("This allows you to change visiblilty in this and the graph")
        self.logorigindocumentvisibilitybutton.setChecked(True)
        #self.logorigindocumentvisibilitybutton.stateChanged.connect(lambda:self.btnstate(self.b1))
        layout.addWidget(self.logorigindocumentvisibilitybutton)

        
        self.setLayout(layout)
        #self.setFixedSize(widthofcolumns, heightofrows) 
        self.setMaximumHeight(heightofrows)
        return
        


class OriginDocumentTextWidget(QFrame):

    def __init__(self, parent=None):
        super(OriginDocumentTextWidget,self).__init__(parent)

        
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        self.textlable = QLabel("Origin Document")
        layout.addWidget(self.textlable)
        self.setLayout(layout)
        self.setMaximumHeight(heightoftextrow)
        return


        
class VectorsAttachedToWidget(QFrame):

    def __init__(self, parent=None):
        super(VectorsAttachedToWidget,self).__init__(parent)

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        
        self.logvectorsattachedtosortbutton = QPushButton()
        self.logvectorsattachedtosortbutton.setIcon(QIcon(QPixmap("bin/assets/a_zsort.png")))
        #self.logvectorsattachedtosortbutton.clicked.connect(lambda:self.whichbtn(self.b2))
        layout.addWidget(self.logvectorsattachedtosortbutton)
        
        self.logvectorsattachedtovisibilitybutton = QCheckBox()
        self.logvectorsattachedtovisibilitybutton.setToolTip("This allows you to change visiblilty in this and the graph")
        self.logvectorsattachedtovisibilitybutton.setChecked(True)
        #self.logvectorsattachedtovisibilitybutton.stateChanged.connect(lambda:self.btnstate(self.b1))
        layout.addWidget(self.logvectorsattachedtovisibilitybutton)

        self.logvectorsattachedtofilterbutton = QPushButton()
        self.logvectorsattachedtofilterbutton.setIcon(QIcon(QPixmap("bin/assets/filter.png")))
        self.logvectorsattachedtofilterbutton.clicked.connect(lambda: OpenFilterAllPopup())
        layout.addWidget(self.logvectorsattachedtofilterbutton)

        
        self.setLayout(layout)
        #self.setFixedSize(widthofcolumns, heightofrows) 
        self.setMaximumHeight(heightofrows)
        return


        
class VectorsAttachedToTextWidget(QFrame):

    def __init__(self, parent=None):
        super(VectorsAttachedToTextWidget,self).__init__(parent)
        
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        self.textlable = QLabel("Vectors Log is Attached to")
        layout.addWidget(self.textlable)
        self.setLayout(layout)
        self.setMaximumHeight(heightoftextrow)
        return


