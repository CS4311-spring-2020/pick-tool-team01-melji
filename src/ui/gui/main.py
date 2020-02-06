import sys
from PyQt5.QtWidgets import *
from graph.graph_window import GraphWindow
from logview.LogView import LogView
def window():
    app = QApplication(sys.argv)
    window = GraphWindow()
    ex = LogView()
    sys.exit(app.exec())


window()
