from PyQt5.QtWidgets import *
from graph_scene import GraphScene
from graph_view import GraphView
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from node_scence import Scene
from node_dto import Node
from node_connector import Socket

class GraphWindow(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.initUI()
    
    def initUI(self):
        self.setGeometry(200, 200, 800, 600)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout)

        self.scene = Scene()
        # self.grScene = self.scene.grScene
        node = Node(self.scene, "Node 1", inputs=[1], outputs=[1])
        # node2 = Node(self.scene, "Node 2")
        self.view = GraphView(self.scene.grScene,self)
        self.layout.addWidget(self.view)

        self.setWindowTitle('Graph View')
        self.show()

        # self.addDebugContent()
    
    def addDebugContent(self):
        greenBrush = QBrush(Qt.green)
        outlinePen = QPen(Qt.black)
        outlinePen.setWidth(2)

        rect = self.grScene.addRect(-100, -100, 80, 100, outlinePen, greenBrush)
        rect.setFlag(QGraphicsItem.ItemIsMovable)