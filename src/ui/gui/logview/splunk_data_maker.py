from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, \
    QCheckBox, QAction, QFrame
from PyQt5.QtGui import QIcon, QPixmap
from random import seed
from random import randint
#from popups.addv import AddVectorPopup
from popups.AddVector import OpenVectorAddPopup
from popups.RemoveVector import OpenVectorRemovePopup
import random
import string
from src.objects.Log import Log
from model import log_entry
from services.intake_service import IntakeService

widthofcolumns = 200
heightofrows = 180
heightoftextrow = 180
rvalueg = 1


# TODO: refactor this in graphical representation of a LogEntry
class SplunkData(QFrame):
    def __init__(self, log_entry,id_of_log,log_list,vectors):
        super(SplunkData, self).__init__(parent=None)
        self.ingestion_service = IntakeService()
        self.log_entry = log_entry
        #self.vectors = None
        self.log = Log(id_of_log,self.log_entry.identifier,self.log_entry.timestamp,self.log_entry.content,"white","white",self.log_entry.host,"bin/assets/white.png", self.log_entry.source, vectors)
        
        self.splunk_data = [
            IDData(id_of_log),
            LogEntryName(self.log_entry.identifier),
            LogEntryTimeStamp(self.log_entry.timestamp),
            LogEntryDescription(self.log_entry.content),
            RandEventTeamWidget(),
            RandEventTeamWidget(),
            LogEntryName(self.log_entry.host),
            IconWidget(),
            LogEntryDescription(self.log_entry.source),
            Vector_Add_Sub_Widget(self.log,vectors)]
        dat = self.splunk_data[3]
        



class IDData(QFrame):

    def __init__(self,id_num):
        super(IDData, self).__init__(None)

        value = randint(0, 9999)
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        self.textlable = QLabel(str(id_num))
        layout.addWidget(self.textlable)
        self.setLayout(layout)
        self.setMaximumHeight(heightoftextrow)
        return


class LogEntryName(QFrame):

    def __init__(self, log_name):
        super(LogEntryName, self).__init__(None)

        letters = string.ascii_lowercase
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.setStyleSheet("border: 1px solid black;")
        self.text_label = QLabel(log_name)
        self.text_label.setWordWrap(True)
        layout.addWidget(self.text_label)
        self.setLayout(layout)
        self.setMaximumHeight(heightoftextrow)
        self.setMaximumWidth(heightoftextrow)


class LogEntryTimeStamp(QFrame):
    def __init__(self, log_entry_timestamp):
        super(LogEntryTimeStamp, self).__init__(None)
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        self.text_label = QLabel(log_entry_timestamp)
        layout.addWidget(self.text_label)

        self.setLayout(layout)
        self.setMaximumHeight(heightoftextrow)
        return


class LogEntryDescription(QFrame):

    def __init__(self, log_entry_name, parent=None, ):
        super(LogEntryDescription, self).__init__(parent)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")

        self.text_label = QLabel(log_entry_name)
        self.text_label.setWordWrap(True)
        layout.addWidget(self.text_label)
        self.setLayout(layout)
        self.setMaximumHeight(heightoftextrow)
        self.setMaximumWidth(heightoftextrow)

        return
   # def setup_clicked(item):
        


class RandomFileTextWidget(QFrame):

    def __init__(self, parent=None):
        super(RandomFileTextWidget, self).__init__(parent)

        letters = string.ascii_lowercase
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.setStyleSheet("border: 1px solid black;")

        randomfiletext = ''.join(random.choice(letters) for i in range(randint(0, 15)))
        randomfiletext = randomfiletext + '.txt'
        self.textlable = QLabel(randomfiletext)

        layout.addWidget(self.textlable)
        self.setLayout(layout)
        self.setMaximumHeight(heightoftextrow)
        return


class Vector_Add_Sub_Widget(QFrame):

    def __init__(self, this_log, vectors, parent=None):
        super(Vector_Add_Sub_Widget, self).__init__(parent)
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")

        self.log_add_vector_button = QPushButton()
        self.log_add_vector_button.setIcon(QIcon(QPixmap("bin/assets/add.png")))
        #self.log_add_vector_button.clicked.connect(lambda: OpenVectorAddPopup(this_log,vectors))
        #self.log_add_vector_button.clicked.connect(lambda: OpenVectorAddPopup(this_log,vectors))
        # self.log_add_vector_button.clicked.connect(lambda:self.whichbtn(self.b2))
        self.layout.addWidget(self.log_add_vector_button)

        self.log_remove_vector_button = QPushButton()
        self.log_remove_vector_button.setIcon(QIcon(QPixmap("bin/assets/subtract.png")))
        #self.log_remove_vector_button.clicked.connect(lambda: OpenVectorRemovePopup())
        # self.log_remove_vector_button.clicked.connect(lambda:self.whichbtn(self.b2))
        self.layout.addWidget(self.log_remove_vector_button)
        
        y = 0
        self.widget_list_vectors = []
        for x in range(0, y):
            b = "Random Sample Vector" + str(x)
            objectv = QLabel(b)
            objectv.setStyleSheet("border: 1px solid white;")
            self.widget_list_vectors.append(objectv)
            self.layout.addWidget(objectv)
            objectv.setMaximumHeight(16)
            
        self.log_add_vector_button.clicked.connect(lambda: OpenVectorAddPopup(this_log,vectors,self.widget_list_vectors))
        #self.log_add_vector_button.clicked.connect(lambda: vectorapopup(this_log,vectors,self.widget_list_vectors))
        self.log_remove_vector_button.clicked.connect(lambda: OpenVectorRemovePopup(this_log,vectors,widget_list_vectors))

        self.setLayout(self.layout)
        self.setMaximumHeight(heightofrows)
        return
    def return_layout():
        return self.layout
    def return_self():
        return self
    def add_vector(vector_to_add):
        objectv = QLabel(str(vector_to_add))
        objectv.setStyleSheet("border: 1px solid white;")
        self.layout.addWidget(objectv)
        objectv.setMaximumHeight(16)

    def vectorapopup(this_log,vectors,layout):
        
        return

class RandEventTeamWidget(QFrame):

    def __init__(self, parent=None):
        super(RandEventTeamWidget, self).__init__(parent)
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        rvalue = randint(1, 3)
        self.setStyleSheet("border: 1px solid black;")
        color = ""
        if rvalue == 1:
            color = "white"
        if rvalue == 2:
            color = "blue"
        if rvalue == 3:
            color = "red"
        labeli = QLabel(color)
        labeli.setScaledContents(True)
        layout.addWidget(labeli)

        # print(labeli.hasScaledContents())
        # print(labeli.size())

        self.setLayout(layout)
        self.setMaximumHeight(heightofrows)
        self.setMaximumWidth(widthofcolumns)
        return


class IconWidget(QFrame):

    def __init__(self, parent=None):
        super(IconWidget, self).__init__(parent)
        rvalueg = 1
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        labeli = QLabel(self)
        self.setStyleSheet("border: 1px solid black;")
        if rvalueg == 1:
            labeli.setPixmap(QPixmap("bin/assets/white.png"))
        if rvalueg == 2:
            labeli.setPixmap(QPixmap("bin/assets/blue.png"))
        if rvalueg == 3:
            labeli.setPixmap(QPixmap("bin/assets/red.png"))
        labeli.setScaledContents(True)
        labeli.setMaximumHeight(100)
        labeli.setMaximumWidth(120)

        layout.addWidget(labeli)

        self.setLayout(layout)
        self.setMaximumHeight(heightofrows)
        self.setMaximumWidth(widthofcolumns)
        return
