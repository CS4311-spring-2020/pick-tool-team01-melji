import sys
from PyQt5.QtWidgets import *
from graph.graph_window import GraphWindow
def window():
    app = QApplication(sys.argv)
    window = GraphWindow()
    sys.exit(app.exec())


window()
