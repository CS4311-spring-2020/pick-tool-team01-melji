from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QPen
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSplitter

from src.ui.gui.graph.graph_view import GraphView
from src.ui.gui.graph.node_dto import Node
from src.ui.gui.graph.node_edge import Edge, EDGE_TYPE_BEZIER
from src.ui.gui.graph.node_scence import Scene
from src.ui.gui.graph.timeline_dto import Timeline
from src.ui.gui.nodeview.NodeGridBuilder import NodeGridMake


class GraphWindow(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.initUI()

    def initUI(self):

        self.setGeometry(500, 500, 800, 600)
        self.layout = QHBoxLayout()
        self.splitter = QSplitter(Qt.Horizontal)
        #self.setStyleSheet(qdarkstyle.load_stylesheet(qt_api=os.environ('PYQTGRAPH_QT_LIB')))
        #self.splitter = .setOrientation(Qt.Horizontal)
        grid = NodeGridMake()
        #grid.setMinimumSize(500, 500)
        #self.layout.addWidget(grid)
        self.splitter.addWidget(grid)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.scene = Scene()
        # self.grScene = self.scene.grScene
        self.addNodes()

        # node2 = Node(self.scene, "Node 2")
        self.view = GraphView(self.scene.grScene, self)
        self.splitter.addWidget(self.view)
        self.layout.addWidget(self.splitter)
        #self.layout.addWidget(self.view)

        self.setWindowTitle('Graph View')
        
        #self.show()

    def addNodes(self):
        node1 = Node(self.scene, "Node 1", inputs=[1], outputs=[1])
        node2 = Node(self.scene, "Node 2", inputs=[1], outputs=[1])
        node3 = Node(self.scene, "Node 3", inputs=[1], outputs=[1])
        node1.setPos(-220, 300)
        node2.setPos(-170, 170)
        node3.setPos(-130, 20)

        edge1 = Edge(self.scene, node1.outputs[0], node2.inputs[0], edge_type=EDGE_TYPE_BEZIER)
        edge2 = Edge(self.scene, node2.outputs[0], node3.inputs[0], edge_type=EDGE_TYPE_BEZIER)
        timeline = Timeline(self.scene)
    
    def addNode(self, title):
        node = Node(self.scene, title)
        
    def removeNode(self, title):
        for node in self.scene.nodes:
            if node.title == title:
                self.scene.removeNode(node)

    def addDebugContent(self):
        greenBrush = QBrush(Qt.green)
        outlinePen = QPen(Qt.black)
        outlinePen.setWidth(2)

        rect = self.grScene.addRect(-100, -100, 80, 100, outlinePen, greenBrush)
        rect.setFlag(QGraphicsItem.ItemIsMovable)