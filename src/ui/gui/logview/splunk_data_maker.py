from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, \
    QCheckBox, QAction, QFrame
from PyQt5.QtGui import QIcon, QPixmap
from random import seed
from random import randint
from popups.AddVector import OpenVectorAddPopup
from popups.RemoveVector import OpenVectorRemovePopup
import random
import string

from model import log_entry
from services.intake_service import IntakeService

widthofcolumns = 200
heightofrows = 180
heightoftextrow = 180
rvalueg = 1


# TODO: refactor this in graphical representation of a LogEntry
class SplunkData(QFrame):
    def __init__(self, log_entry):
        super(SplunkData, self).__init__(parent=None)
        self.ingestion_service = IntakeService()

        self.log_entry = log_entry
        self.splunk_data = [
            RandomIDData(),
            LogEntryName(self.log_entry.identifier),
            LogEntryTimeStamp(self.log_entry.timestamp),
            LogEntryDescription(self.log_entry.content),
            RandEventTeamWidget(),
            RandEventTeamWidget(),
            LogEntryName(self.log_entry.host),
            IconWidget(),
            RandomFileTextWidget(),
            RandVectorWidget()]


class RandomIDData(QFrame):

    def __init__(self):
        super(RandomIDData, self).__init__(None)

        value = randint(0, 9999)
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        self.textlable = QLabel(str(value))
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


class RandVectorWidget(QFrame):

    def __init__(self, parent=None):
        super(RandVectorWidget, self).__init__(parent)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")

        self.logreportersortbutton = QPushButton()
        self.logreportersortbutton.setIcon(QIcon(QPixmap("bin/assets/add.png")))
        self.logreportersortbutton.clicked.connect(lambda: OpenVectorAddPopup())
        # self.logreportersortbutton.clicked.connect(lambda:self.whichbtn(self.b2))
        layout.addWidget(self.logreportersortbutton)

        self.logreporterfilterbutton = QPushButton()
        self.logreporterfilterbutton.setIcon(QIcon(QPixmap("bin/assets/subtract.png")))
        self.logreporterfilterbutton.clicked.connect(lambda: OpenVectorRemovePopup())
        # self.logreporterfilterbutton.clicked.connect(lambda:self.whichbtn(self.b2))
        layout.addWidget(self.logreporterfilterbutton)

        y = randint(0, 9)

        for x in range(0, y):
            b = "Random Sample Vector" + str(x)
            object = QLabel(b)
            object.setStyleSheet("border: 1px solid white;")
            layout.addWidget(object)
            object.setMaximumHeight(16)

        self.setLayout(layout)
        self.setMaximumHeight(heightofrows)
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
