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
class Get_Widgets(QFrame):
    def __init__(self,text_array, parent=None):
        super(Get_Sample_Widgets,self).__init__(parent)

        self.arrayofwidgets
        for i in range(0,len(text_array)):
            self.arrayofwidgets.append(IDTextWidget(text_array[i]))
            i += 1
            self.arrayofwidgets.append(NameTextWidget(text_array[i]))
            i += 1
            self.arrayofwidgets.append(DescriptionTextWidget(text_array[i]))
            i += 1
            self.arrayofwidgets.append(FileTextWidget(text_array[i]))
        
        return 


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