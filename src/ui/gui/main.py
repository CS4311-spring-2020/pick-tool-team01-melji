import sys
import qdarkstyle
import os
os.environ['QT_API'] = 'pyqt5'
from PyQt5.QtWidgets import *
from graph.graph_window import GraphWindow
from logview.LogView import LogView
from nodeview.NodeView import NodeView
from popups.menupopup import OpenMenuPopup
from popups.vector_configuration import OpenVectorConfigPopup
from popups.IconConfiguration import IconConfiguration
from popups.team_configuration import Configure_Team
from popups.select_path import Paths
    #icon = IconConfiguration()
global ex2

def window():
    app = QApplication(sys.argv)
    #OpenMenuPopup.Open()
    global ex2
    stylesheet = qdarkstyle.load_stylesheet()
    #stylesheet().append("QPushButton { min-height: 0px; min-width: 0px }")
    window = GraphWindow()
    #icon = IconConfiguration()
    #win2 = OpenMenuPopup()
    #win2.Open()
    #win3 = OpenVectorConfigPopup()
    #win3.Open()
    w = Paths()
    w.showpaths()
    ex2 = NodeView(window)
    ex = LogView(ex2)
    #app.setStyleSheet(stylesheet+"QPushButton { min-height: 0px; min-width: 15px }"+"QLabel { border: 0px; }")
    #app.setStyleSheet(qdarkstyle.load_stylesheet().append(QString("QPushButton { min-height: 0px; min-width: 0px }")))
    sys.exit(app.exec())
    #self.menu = 
    #self.menu.Open()
    


window()
