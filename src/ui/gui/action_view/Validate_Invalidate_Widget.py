import sys
from PyQt5.QtCore import *
#from Qt import AlignHCenter, AlignVCenter

from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QCheckBox ,QAction, QFrame

widthofcolumns = 200
heightofrows=180
heightoftextrow = 180

class Validate_Invalidate_Widget(QFrame):

    def __init__(self, parent=None):
        super(Validate_Invalidate_Widget,self).__init__(parent)
        layout_h = QHBoxLayout()
        layout_h.setContentsMargins(0,0,0,0)
        layout_h.setSpacing(0)

        layout_v = QVBoxLayout()
        layout_v.setContentsMargins(0,0,0,0)
        layout_v.setSpacing(0)

        layout_i = QVBoxLayout()
        layout_i.setContentsMargins(0,0,0,0)
        layout_i.setSpacing(0)

        frame_v = QFrame()
        frame_i = QFrame()

        #self.setStyleSheet("border: 1px solid black;")
        frame_i.setStyleSheet("border: 1px solid black;")
        frame_v.setStyleSheet("border: 1px solid black;")


        self.validate_button = QPushButton("Validate")
        #self.logreportersortbutton.clicked.connect(lambda:OpenVectorAddPopup())
        #self.logreportersortbutton.clicked.connect(lambda:self.whichbtn(self.b2))
        layout_v.addWidget(self.validate_button)
        self.checkbutton = QCheckBox("Validate")
        #self.checkbutton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.checkbutton.setToolTip("This allows you to change visiblilty in this and the graph")
        self.checkbutton.setChecked(False)
        self.checkbutton.setStyleSheet(" border: 0px; ")
        layout_v.addWidget(self.checkbutton)
        layout_v.setAlignment(Qt.AlignVCenter|Qt.AlignHCenter)
        frame_v.setLayout(layout_v)
        
        self.invalidate_button = QPushButton("Invalidate")
        #self.logreportersortbutton.clicked.connect(lambda:OpenVectorAddPopup())
        #self.logreportersortbutton.clicked.connect(lambda:self.whichbtn(self.b2))
        layout_i.addWidget(self.invalidate_button)
        self.checkbutton_i = QCheckBox("Invalidate")
        #self.checkbutton_i.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.checkbutton_i.setToolTip("This allows you to change visiblilty in this and the graph")
        self.checkbutton_i.setChecked(False)
        self.checkbutton_i.setStyleSheet(" border: 0px; ")
        layout_i.addWidget(self.checkbutton_i)

        self.checkbutton.stateChanged.connect(lambda:self.btnstate(self.checkbutton))
        self.checkbutton_i.stateChanged.connect(lambda:self.btnstate(self.checkbutton_i))
        layout_i.setAlignment(Qt.AlignVCenter|Qt.AlignHCenter)
        frame_i.setLayout(layout_i)
        
        layout_h.addWidget(frame_v)
        layout_h.addWidget(frame_i)
        self.setLayout(layout_h)
        self.setMaximumHeight(heightofrows)
        return
    
    def btnstate(self,b):
        if b.text() == "Validate":
            if b.isChecked() == True:
                self.checkbutton_i.setCheckState(False)
                self.checkbutton_i.setChecked(False)
            else:
                b.setChecked(False)
                b.setCheckState(False)
        if b.text() == "Invalidate":
            if b.isChecked() == True:
                self.checkbutton.setCheckState(False)
                self.checkbutton.setChecked(False)
            else:
                b.setChecked(False)
                b.setCheckState(False)
