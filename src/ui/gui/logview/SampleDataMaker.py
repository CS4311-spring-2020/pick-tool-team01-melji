import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QCheckBox ,QAction, QFrame
from PyQt5.QtGui import QIcon, QPixmap
from random import seed,randint
from popups.AddVector import OpenVectorAddPopup
from popups.RemoveVector import OpenVectorRemovePopup
import random
import string

widthofcolumns = 200
heightofrows=180
heightoftextrow = 180
rvalueg = 1  # for the program to know the color of the icon
global sample
class GetSampleWidgets(QFrame):
    def __init__(self, parent=None):
        super(GetSampleWidgets,self).__init__(parent)
        global sample
        
        sample = open('text.txt', 'w') 
        self.arrayofsamplewidgets= [
            LogRandIDTextWidget()
            ,LogRandNameTextWidget()
            ,RandTimeWidget()
            ,LogRandDescriptionTextWidget()
            ,RandEventTeamWidget()
            ,RandEventTeamWidget()
            ,LogRandNameTextWidget()
            ,IconWidget()
            ,RandomFileTextWidget()
            ,RandVectorWidget()]
        
        
        sample.close() 

        return 

    




class LogRandIDTextWidget(QFrame):

    def __init__(self, parent=None):
        super(LogRandIDTextWidget,self).__init__(parent)

        value1 = randint(0, 9999)
        self.value = str(value1)
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        self.textlable = QLabel(self.value)
        layout.addWidget(self.textlable)
        self.setLayout(layout)    
        self.setMaximumHeight(heightoftextrow)
        return




class LogRandNameTextWidget(QFrame):

    def __init__(self, parent=None):
        super(LogRandNameTextWidget,self).__init__(parent)

        letters = string.ascii_lowercase
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        
        a =  randint(1, 8)
        randomtext = ''
        for x in range(0,a):
            randomtextvar =''.join( random.choice(letters) for i in range(randint(0, 20)))
            randomtext = randomtext + ' ' + randomtextvar
        
        
        self.textlable = QLabel(randomtext)
        self.textlable.setWordWrap(True)
        layout.addWidget(self.textlable)
        self.setLayout(layout)  
        self.setMaximumHeight(heightoftextrow)
        self.setMaximumWidth(heightoftextrow)

        return


class RandTimeWidget(QFrame):

    def __init__(self, parent=None):
        super(RandTimeWidget,self).__init__(parent)

        value1 = randint(1, 12)
        value2 = randint(1, 31)
        value3 = randint(0, 3000)
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        date = str(value1) + "/" + str(value2) + "/" + str(value3)
        self.textlable = QLabel(str(date))
        layout.addWidget(self.textlable)
        self.setLayout(layout)    
        self.setMaximumHeight(heightoftextrow)
        return


