import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton, QHBoxLayout, QCheckBox ,QAction, QFrame, QSizePolicy
from PyQt5.QtGui import QIcon, QPixmap
from popups.filter_all import OpenFilterAllPopup
from PyQt5.Qt import *

widthofcolumns = 200
heightofrows=50
heightoftextrow = 25

class GetGridWidgets(QFrame):

    def __init__(self, parent=None):
        super(GetGridWidgets,self).__init__(parent)
        #, LogIDWidget()LogNameWidget()TimeStampWidget()ReporterWidget()DescriptionWidget()IconWidget(),OriginDocumentWidget(),VectorsAttachedToWidget(), LogIDTextWidget(), LogNameTextWidget(), TimeStampTextWidget(),DescriptionTextWidget(), ReporterTextWidget(), EventTeamTextWidget(), LogTextWidget("Location"), IconTextWidget(), OriginDocumentTextWidget(), VectorsAttachedToTextWidget()
        self.arrayofwidgets = [ TopGrid("1_9v","no"), TopGrid("a_z","no"), TopGrid("1_9","true"), TopGrid("a_z","no"), TopGrid("a_z","true"), TopGrid("a_z","true"),TopGrid("a_z","true"), TopGrid("a_z","true"),
        TopGrid("direction","no"),TopGrid("a_z","true"), LogTextWidget("Log ID"), LogTextWidget("Log Name"), LogTextWidget("Time Stamp"), LogTextWidget("Description"), LogTextWidget("Reporter"), LogTextWidget("Event Team"), LogTextWidget("Location"), LogTextWidget("Icon"), LogTextWidget("Origin Document"), LogTextWidget("Vectors Log is Attached to")]
        return 
    
class LogTextWidget(QFrame):

    def __init__(self,texttodisplay,parent=None):
        super(LogTextWidget,self).__init__(parent)
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setAlignment(Qt.AlignVCenter|Qt.AlignHCenter)
        layout.setSpacing(0)
        #self.setSizePolicy( QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setStyleSheet("border: 1px solid black;")
        self.textlable = QLabel(texttodisplay)
        self.textlable.setStyleSheet(" border: 0px; ")
        layout.addWidget(self.textlable)
        self.setLayout(layout)    
        self.setMaximumHeight(heightoftextrow)
        self.logsortbutton = QPushButton()
        return


class TopGrid(QFrame):
    global logsortbuttonext
    global logfilterbuttonext
    global logfilterbuttonext
    global logcheckbuttonext
    def __init__(self, typeofsort,hasfilter,parent=None):
        super(TopGrid,self).__init__(parent)
        self.logsortbutton = QPushButton()
        
        global logsortbuttonext
        global logfilterbuttonext
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setAlignment(Qt.AlignVCenter|Qt.AlignHCenter)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        #self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        if typeofsort == "1_9":

            logsortbuttonext = self.logsortbutton
            self.logsortbutton.setIcon(QIcon(QPixmap("bin/assets/1_9sort.png")))
            self.logsortbutton.setToolTip("This allows you to sort the current column")
            #self.logsortbutton.clicked.connect(lambda:self.whichbtn(self.b2))
            self.logsortbutton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.logsortbutton.setMaximumWidth(7)
            self.logsortbutton.setStyleSheet(" border: 0px; ")
            layout.addWidget(self.logsortbutton) 
        
        elif typeofsort == "1_9v":

            self.logsortbutton = QPushButton()
            logsortbuttonext = self.logsortbutton
            self.textlable = QLabel("Visibility")
            layout.addWidget(self.textlable)
            self.logsortbutton.setIcon(QIcon(QPixmap("bin/assets/1_9sort.png")))
            self.logsortbutton.setToolTip("This allows you to sort the current column")
            #self.logsortbutton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            #self.logsortbutton.clicked.connect(lambda:self.whichbtn(self.b2))
            self.logsortbutton.setStyleSheet(" border: 0px; ")
            layout.addWidget(self.logsortbutton)

        elif typeofsort == "a_z":
            
            self.logsortbutton = QPushButton()
            logsortbuttonext = self.logsortbutton
            self.logsortbutton.setIcon(QIcon(QPixmap("bin/assets/a_zsort.png")))
            self.logsortbutton.setToolTip("This allows you to sort the current column")
            #self.logsortbutton.clicked.connect(lambda:self.whichbtn(self.b2))
            #self.logsortbutton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.logsortbutton.setMaximumWidth(7)
            self.logsortbutton.setStyleSheet(" border: 0px; ")
            layout.addWidget(self.logsortbutton)

        elif typeofsort == "direction":

            self.logsortbutton = QPushButton()
            logsortbuttonext = self.logsortbutton
            self.logsortbutton.setIcon(QIcon(QPixmap("bin/assets/upsort.png")))
            self.logsortbutton.setToolTip("This allows you to sort the current column")
            #self.logsortbutton.clicked.connect(lambda:self.whichbtn(self.b2))
            #self.logsortbutton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.logsortbutton.setMaximumWidth(7)
            self.logsortbutton.setStyleSheet(" border: 0px; ")
            layout.addWidget(self.logsortbutton)
        
        global logcheckbuttonext
        self.logcheckbutton = QCheckBox()
        logcheckbuttonext = self.logcheckbutton
        self.logcheckbutton.setToolTip("This allows you to change visiblilty in this and the graph")
        self.logcheckbutton.setChecked(True)
        self.logcheckbutton.setStyleSheet(" border: 0px; ")
        #self.logcheckbutton.stateChanged.connect(lambda:self.btnstate(self.b1))
        layout.addWidget(self.logcheckbutton)
        

        if hasfilter == "true":
            self.logfilterbutton = QPushButton()
            #self.logfilterbutton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            logfilterbuttonext = self.logfilterbutton
            self.logfilterbutton.setIcon(QIcon(QPixmap("bin/assets/filter.png")))
            self.logfilterbutton.setToolTip("This allows you to filter the current column")
            self.logfilterbutton.setMaximumWidth(7)
            #self.logfilterbutton.clicked.connect(lambda: OpenFilterAllPopup())
            self.logfilterbutton.setStyleSheet(" border: 0px; ")
            layout.addWidget(self.logfilterbutton)

        #super(logTimeStampWidget,self).__init__(parent)


        
        self.setLayout(layout)
        #self.setFixedSize(widthofcolumns, heightofrows) 
        self.setMaximumHeight(heightofrows)
        return

    def returnbutton(self,typeofbutton):
        global logsortbuttonext
        global logfilterbuttonext
        global logcheckbuttonext
        if typeofbutton == "sort":
            return logsortbuttonext


        elif typeofbutton == "filter":
            return logsortbuttonext


        elif typeofbutton == "check":
            return logcheckbuttonext

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
        self.textlable = QLabel("Log Name")
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


