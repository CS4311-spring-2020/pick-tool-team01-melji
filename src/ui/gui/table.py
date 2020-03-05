import sys
from PyQt5.QtWidgets import *
from src.ui.gui.graph.graph_window import GraphWindow

def window():
    app = QApplication(sys.argv)
    window = GraphWindow()
    window.addNode('New Node')
    window.addNode('Another Node')
    window.removeNode('New Node')
    sys.exit(app.exec())


window()
