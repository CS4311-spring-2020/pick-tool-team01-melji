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
from popups.team_configuration import OpenTFPopup
    #icon = IconConfiguration()
global ex2
def window():
    app = QApplication(sys.argv)
    #OpenMenuPopup.Open()
    global ex2
    window = GraphWindow()
    #icon = IconConfiguration()
    #win2 = OpenMenuPopup()
    #win2.Open()
    #win3 = OpenVectorConfigPopup()
    #win3.Open()
    w = OpenTFPopup()
    ex2 = NodeView(window)
    ex = LogView(ex2)
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    sys.exit(app.exec())
    #self.menu = 
    #self.menu.Open()
    


window()
