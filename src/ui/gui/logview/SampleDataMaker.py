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
        self.arrayofsamplewidgets= [LogRandIDTextWidget(),LogRandNameTextWidget(),RandTimeWidget(),LogRandDescriptionTextWidget(),RandEventTeamWidget(),RandEventTeamWidget(),IconWidget(),RandomFileTextWidget(),RandVectorWidget()]
        
         
        sample.close() 

        return 

    




class LogRandIDTextWidget(QFrame):

    def __init__(self, parent=None):
        super(LogRandIDTextWidget,self).__init__(parent)

        value = randint(0, 9999)
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        self.textlable = QLabel(str(value))
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


class LogRandDescriptionTextWidget(QFrame):

    def __init__(self, parent=None):
        super(LogRandDescriptionTextWidget,self).__init__(parent)

        letters = string.ascii_lowercase
        layoutdes = QHBoxLayout()
        layoutdes.setContentsMargins(0,0,0,0)
        layoutdes.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        
        a =  randint(0, 30)
        randomtextdes = ''
        for x in range(0,a):
            randomtextvar =''.join( random.choice(letters) for i in range(randint(0, 20)))
            randomtextdes = randomtextdes + ' ' + randomtextvar
        
       
        self.textlabledes = QLabel(randomtextdes)
        self.textlabledes.setWordWrap(True)
        layoutdes.addWidget(self.textlabledes)
        self.setLayout(layoutdes)  
        self.setMaximumHeight(heightoftextrow)
        self.setMaximumWidth(heightoftextrow)

        return



class RandomFileTextWidget(QFrame):

    def __init__(self, parent=None):
        super(RandomFileTextWidget,self).__init__(parent)


        letters = string.ascii_lowercase
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)

        self.setStyleSheet("border: 1px solid black;")

        randomfiletext =''.join(random.choice(letters) for i in range(randint(0, 15)))
        randomfiletext = randomfiletext +'.txt'
        self.textlable = QLabel(randomfiletext)

        layout.addWidget(self.textlable)
        self.setLayout(layout)  
        self.setMaximumHeight(heightoftextrow)
        return




class RandVectorWidget(QFrame):

    def __init__(self, parent=None):
        super(RandVectorWidget,self).__init__(parent)
        layout = QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        
        self.logreportersortbutton = QPushButton()
        self.logreportersortbutton.setIcon(QIcon(QPixmap("bin\\assets\\add.png")))
        self.logreportersortbutton.clicked.connect(lambda:OpenVectorAddPopup())
        #self.logreportersortbutton.clicked.connect(lambda:self.whichbtn(self.b2))
        layout.addWidget(self.logreportersortbutton)

        self.logreporterfilterbutton = QPushButton()
        self.logreporterfilterbutton.setIcon(QIcon(QPixmap("bin\\assets\\subtract.png")))
        self.logreportersortbutton.clicked.connect(lambda:OpenVectorRemovePopup())
        #self.logreporterfilterbutton.clicked.connect(lambda:self.whichbtn(self.b2))
        layout.addWidget(self.logreporterfilterbutton)
        
        
        y =  randint(0, 9)

        for x in range(0,y):

                
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
        super(RandEventTeamWidget,self).__init__(parent)
        global sample
        global rvalueg
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        rvalue = randint(1, 3)
        rvalueg = rvalue
        self.setStyleSheet("border: 1px solid black;")
        sample.write(str(rvalue))
        color = ""
        if rvalue == 1:
            color = "white"
        if rvalue == 2:
           color = "blue"
        if rvalue == 3:
            color = "red"
        sample.write(color)
        labeli = QLabel(color)
        labeli.setScaledContents(True)
        layout.addWidget(labeli)

        #print(labeli.hasScaledContents())
        #print(labeli.size())
        
        self.setLayout(layout)  
        self.setMaximumHeight(heightofrows)
        self.setMaximumWidth(widthofcolumns)
        return

class IconWidget(QFrame):

    def __init__(self, parent=None):
        super(IconWidget,self).__init__(parent)
        global sample
        global rvalueg
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        labeli = QLabel(self)
        self.setStyleSheet("border: 1px solid black;")
        if rvalueg == 1:
            labeli.setPixmap(QPixmap("bin\\assets\\white.png"))
        if rvalueg == 2:
            labeli.setPixmap(QPixmap("bin\\assets\\blue.png"))
        if rvalueg == 3:
            labeli.setPixmap(QPixmap("bin\\assets\\red.png"))
        labeli.setScaledContents(True)
        labeli.setMaximumHeight(100)
        labeli.setMaximumWidth(120)
        sample.write("HI")
        
        layout.addWidget(labeli)
        sample.write(str(rvalueg))
        
        self.setLayout(layout)  
        self.setMaximumHeight(heightofrows)
        self.setMaximumWidth(widthofcolumns)
        return
        
        