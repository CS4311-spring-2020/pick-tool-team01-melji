from PyQt5.QtWidgets import *
from graph.graph_scene import GraphScene
from graph.graph_view import GraphView
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from graph.node_scence import Scene
from graph.node_edge import Edge
from graph.node_dto import Node
from graph.node_connector import Socket


class GraphWindow(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 800, 600)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.scene = Scene()
        # self.grScene = self.scene.grScene
        self.addNodes()

        # node2 = Node(self.scene, "Node 2")
        self.view = GraphView(self.scene.grScene, self)
        self.layout.addWidget(self.view)

        self.setWindowTitle('Graph View')
        self.show()

        # self.addDebugContent()
    def addNodes(self):
        node1 = Node(self.scene, "Node 1", inputs=[1], outputs=[1])
        node2 = Node(self.scene, "Node 2", inputs=[1], outputs=[1])
        node3 = Node(self.scene, "Node 3", inputs=[1], outputs=[1])
        node1.setPos(-350, -250)
        node2.setPos(-75, 0)
        node3.setPos(200, -150)

        edge1 = Edge(self.scene, node1.outputs[0], node2.inputs[0])
        edge2 = Edge(self.scene, node2.outputs[0], node3.inputs[0], type=2)

    def contextMenuEvent(self, event):
        contextMenu = QMenu(self)
        
        removeNodeAction = contextMenu.addAction("Remove Node\tCtr-R")
        connectNode = contextMenu.addAction("Connect Node\tCtr-C")
        deConnectNode = contextMenu.addAction("Deconnect Node\tCtr-D")
        undoChanges = contextMenu.addAction("Undo Changes\tCtr-Z")
        redoChanges = contextMenu.addAction("Redo Changes\tCtr-Y")
        settings = contextMenu.addAction("Settings\tCtr-A")

        action = contextMenu.exec_(self.mapToParent(event.pos()))


    def addDebugContent(self):
        greenBrush = QBrush(Qt.green)
        outlinePen = QPen(Qt.black)
        outlinePen.setWidth(2)

        rect = self.grScene.addRect(-100, -100, 80, 100, outlinePen, greenBrush)
        rect.setFlag(QGraphicsItem.ItemIsMovable)
