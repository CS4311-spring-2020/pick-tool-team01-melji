import sys
import qdarkstyle
import os
os.environ['QT_API'] = 'pyqt5'
from PyQt5.QtWidgets import *
#from graph.graph_window import GraphWindow
#from logview.LogView import LogView
#from nodeview.NodeView import NodeView
    #icon = IconConfiguration()
#global ex2

def window():
    app = QApplication(sys.argv)
    #OpenMenuPopup.Open()
    #global ex2
    
    #stylesheet().append("QPushButton { min-height: 0px; min-width: 0px }")
    #window = GraphWindow()
    #icon = IconConfiguration()
    #win2 = OpenMenuPopup()
    #win2.Open()
    #win3 = OpenVectorConfigPopup()
    #win3.Open()
    w = Paths()
    #print('cwd is %s' %(os.getcwd()))
    w.showpaths()
    #a = ActionView()
    #a.show_view()
    #ex2 = NodeView(window)
    #ex = LogView(ex2)
    stylesheet = qdarkstyle.load_stylesheet()
    app.setStyleSheet(stylesheet+"QPushButton { min-height: 0px; min-width: 15px }"+"QLabel { border: 0px; }")
    #app.setStyleSheet(qdarkstyle.load_stylesheet().append(QString("QPushButton { min-height: 0px; min-width: 0px }")))
    sys.exit(app.exec())
    #self.menu = 
    #self.menu.Open() def closeMyApp_OpenNewApp(self): self.close() self.Open = NewApp.NewApp() self.Open.show()
    
print('cwd is %s' %(os.getcwd()))
sys.path.append(os.getcwd())
print('cwd is %s' %(os.getcwd()))
from popups.team_configuration import Configure_Team
from src.objects.Log import Log
from popups.select_path import Paths
window()
