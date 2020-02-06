import sys
from PyQt5.QtWidgets import *
from graph.graph_window import GraphWindow
from logview.LogView import LogView
from popups.menupopup import OpenMenuPopup
from popups.vector_configuration import OpenVectorConfigPopup
from popups.filterTeam import Ui_Dialog
def window():
    app = QApplication(sys.argv)
    #OpenMenuPopup.Open()
    window = GraphWindow()
    win2 = OpenMenuPopup()
    win2.Open()
    win3 = OpenVectorConfigPopup()
    win3.Open()
    ex = LogView()
    sys.exit(app.exec())
    #self.menu = 
    #self.menu.Open()
    


window()
