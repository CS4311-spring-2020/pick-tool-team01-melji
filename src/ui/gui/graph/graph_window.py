
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget , QHBoxLayout,QSplitter
from graph.graph_scene import GraphScene
from graph.graph_view import GraphView
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from graph.node_scence import Scene
from graph.node_edge import Edge, EDGE_TYPE_BEZIER
from graph.node_dto import Node
from graph.node_connector import Socket
from graph.timeline_dto import Timeline
from nodeview.NodeGridBuilder import NodeGridMake

from src.ui.gui.nodeview.NodeGridBuilder import LISTBOX_MIMETYPE


class GraphWindow(QWidget):

    def __init__(self, wind, parent=None):
        super().__init__(parent=parent)
        self.initUI(wind)

    def initUI(self,wind):
        
        self.setGeometry(500, 500, 800, 600)
        self.layout = QHBoxLayout()
        self.splitter = QSplitter(Qt.Horizontal)
        #self.setStyleSheet(qdarkstyle.load_stylesheet(qt_api=os.environ('PYQTGRAPH_QT_LIB')))
        #self.splitter = .setOrientation(Qt.Horizontal)
        grid = NodeGridMake(wind.vector)
        #grid.setMinimumSize(500, 500)
        #self.layout.addWidget(grid)
        self.splitter.addWidget(wind)#grid)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.scene = Scene()
        # self.scene.addDragEnterListener(self.onDragEnter)
        # self.scene.addDropListener(self.onDrop)
        # self.grScene = self.scene.grScene
        self.addNodes()

        # node2 = Node(self.scene, "Node 2")
        self.view = GraphView(self.scene.grScene, self)

        self.view.addDragEnterListener(self.onDragEnter)
        self.view.addDropListener(self.onDrop)

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

    def contextMenuEvent(self, event):
        contextMenu = QMenu(self)
        
        removeNodeAction = contextMenu.addAction("Add node")
        connectNode = contextMenu.addAction("Add relationship")
        deConnectNode = contextMenu.addAction("Delete node")
        undoChanges = contextMenu.addAction("Delete relationship")
        redoChanges = contextMenu.addAction("Edit node")
        settings = contextMenu.addAction("Edit relationship")
        settings = contextMenu.addAction("Timeline orientation")
        settings = contextMenu.addAction("Interval units")

        action = contextMenu.exec_(self.mapToParent(event.pos()))


    def addDebugContent(self):
        greenBrush = QBrush(Qt.green)
        outlinePen = QPen(Qt.black)
        outlinePen.setWidth(2)

        rect = self.grScene.addRect(-100, -100, 80, 100, outlinePen, greenBrush)
        rect.setFlag(QGraphicsItem.ItemIsMovable)

    def onDragEnter(self, event):
        print("on Drag enter")
        if event.mimeData().hasFormat(LISTBOX_MIMETYPE):
            event.acceptProposedAction()
        else:
            # print(" ... denied drag enter event")
            event.setAccepted(False)

    def onDrop(self, event):
        print("on Drop")
        if event.mimeData().hasFormat(LISTBOX_MIMETYPE):
            eventData = event.mimeData().data(LISTBOX_MIMETYPE)
            dataStream = QDataStream(eventData, QIODevice.ReadOnly)
            # pixmap = QPixmap()
            # dataStream >> pixmap
            op_code = dataStream.readInt()
            text = dataStream.readQString()

            mouse_position = event.pos()
            scene_position = self.scene.grScene.views()[0].mapToScene(mouse_position)

            print("GOT DROP: [%d] '%s'" % (op_code, text), "mouse:", mouse_position, "scene:", scene_position)

            node = Node(self.scene, text, inputs=[1], outputs=[1])
            node.setPos(scene_position.x(), scene_position.y())
            self.scene.addNode(node)

            event.setDropAction(Qt.MoveAction)
            event.accept()
        else:
            # print(" ... drop ignored, not requested format '%s'" % LISTBOX_MIMETYPE)
            event.ignore()

