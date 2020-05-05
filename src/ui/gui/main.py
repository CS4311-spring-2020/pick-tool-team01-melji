import sys
import qdarkstyle
import os
os.environ['QT_API'] = 'pyqt5'
from PyQt5.QtWidgets import *


def window():
    app = QApplication(sys.argv)
    
    
    
    w = Paths()
    w.showpaths()
    #testing = (["IDText","NameText","DescriptionText","FileText"])
    #a = ActionView(testing)

    #a.show_view()
    #node_list = []
    #vectorlist = []
    #vectorlist.append(Vector(0,"testvector",None,None,"this is a test",node_list))
    #b = Make_Vector(vectorlist)

    #b.show()
    stylesheet = qdarkstyle.load_stylesheet()
    app.setStyleSheet(stylesheet+"QPushButton { min-height: 0px; min-width: 15px }"+"QLabel { border: 0px; }")
    sys.exit(app.exec())

print('cwd is %s' %(os.getcwd()))
sys.path.append(os.getcwd())
print('cwd is %s' %(os.getcwd()))
from popups.team_configuration import Configure_Team
#from src.objects import Log
from popups.select_path import Paths
from popups.Make_Vector import Make_Vector
from src.objects.Vector import Vector
from action_view.Action_Report_View import ActionView
window()
