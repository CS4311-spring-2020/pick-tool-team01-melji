import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QCheckBox ,QAction, QFrame
from PyQt5.QtGui import QIcon, QPixmap
from random import seed,randint
from action_view.Validate_Invalidate_Widget import Validate_Invalidate_Widget
import random
import string

widthofcolumns = 200
heightofrows=180
heightoftextrow = 180
rvalueg = 1  # for the program to know the color of the icon
global sample
class Get_Sample_Widgets(QFrame):
    def __init__(self, parent=None):
        super(Get_Sample_Widgets,self).__init__(parent)
        global sample
        
        sample = open('text.txt', 'w') 
        self.arrayofsamplewidgets= [RandomFileTextWidget(),RandIDTextWidget(),RandDescriptionTextWidget(),Validate_Invalidate_Widget()]
        
         
        sample.close() 

        return 

    def get_widgets(text_array):
        self.arrayofwidgets
        for i in range(0,len(text_array)):
            self.arrayofwidgets.append(IDTextWidget(text_array[i]))
            i += 1
            self.arrayofwidgets.append(NameTextWidget(text_array[i]))
            i += 1
            self.arrayofwidgets.append(DescriptionTextWidget(text_array[i]))
            i += 1
            self.arrayofwidgets.append(FileTextWidget(text_array[i]))
        return self.arrayofwidgets

            






class IDTextWidget(QFrame):

    def __init__(self,text_in, parent=None):
        super(RandIDTextWidget,self).__init__(parent)

        
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        self.textlable = QLabel(str(text_in))
        self.textlable.setStyleSheet("border: 0px solid black;")
        layout.addWidget(self.textlable)
        self.setLayout(layout)    
        self.setMaximumHeight(heightoftextrow)
        return




class NameTextWidget(QFrame):

    def __init__(self,text_in, parent=None):
        super(RandNameTextWidget,self).__init__(parent)

        letters = string.ascii_lowercase
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        
        
       
        self.textlable = QLabel(str(text_in))
        self.textlable.setWordWrap(True)
        self.textlable.setStyleSheet("border: 0px solid black;")
        layout.addWidget(self.textlable)
        self.setLayout(layout)  
        self.setMaximumHeight(heightoftextrow)
        self.setMaximumWidth(heightoftextrow)

        return


class DescriptionTextWidget(QFrame):

    def __init__(self,text_in, parent=None):
        super(RandDescriptionTextWidget,self).__init__(parent)

        letters = string.ascii_lowercase
        layoutdes = QHBoxLayout()
        layoutdes.setContentsMargins(0,0,0,0)
        layoutdes.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        
        
       
        self.textlabledes = QLabel(text_in)
        self.textlabledes.setWordWrap(True)
        self.textlabledes.setStyleSheet("border: 0px solid black;")
        layoutdes.addWidget(self.textlabledes)
        self.setLayout(layoutdes)  
        self.setMaximumHeight(heightoftextrow)
        self.setMaximumWidth(heightoftextrow)

        return



class FileTextWidget(QFrame):

    def __init__(self,text_in, parent=None):
        super(RandomFileTextWidget,self).__init__(parent)


        letters = string.ascii_lowercase
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)

        self.setStyleSheet("border: 1px solid black;")

        self.textlable = QLabel(str(text_in))
        self.textlable.setStyleSheet("border: 0px solid black;")

        layout.addWidget(self.textlable)
        self.setLayout(layout)  
        self.setMaximumHeight(heightoftextrow)
        return





class RandIDTextWidget(QFrame):

    def __init__(self, parent=None):
        super(RandIDTextWidget,self).__init__(parent)

        value = randint(0, 9999)
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        self.setStyleSheet("border: 1px solid black;")
        self.textlable = QLabel(str(value))
        self.textlable.setStyleSheet("border: 0px solid black;")
        layout.addWidget(self.textlable)
        self.setLayout(layout)    
        self.setMaximumHeight(heightoftextrow)
        return




class RandNameTextWidget(QFrame):

    def __init__(self, parent=None):
        super(RandNameTextWidget,self).__init__(parent)

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
        self.textlable.setStyleSheet("border: 0px solid black;")
        layout.addWidget(self.textlable)
        self.setLayout(layout)  
        self.setMaximumHeight(heightoftextrow)
        self.setMaximumWidth(heightoftextrow)

        return


class RandDescriptionTextWidget(QFrame):

    def __init__(self, parent=None):
        super(RandDescriptionTextWidget,self).__init__(parent)

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
        self.textlabledes.setStyleSheet("border: 0px solid black;")
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
        self.textlable.setStyleSheet("border: 0px solid black;")

        layout.addWidget(self.textlable)
        self.setLayout(layout)  
        self.setMaximumHeight(heightoftextrow)
        return


