from src.ui.gui.graph.gr_node_connector import GRSocket

LEFT_TOP = 1
LEFT_BOTTOM = 2
RIGHT_TOP = 3
RIGHT_BOTTOM = 4


class Socket():
    def __init__(self, node, index=0, position=LEFT_TOP):
        self.node = node
        self.index = index
        self.position = position

        self.grSocket = GRSocket(self)
        self.grSocket.setPos(*self.node.getSocketPosition(index, position))

        self.edge = None

    def getSocketPosition(self):
        res = self.node.getSocketPosition(self.index, self.position)
        return res

    def setConnectedEdge(self, edge=None):
        self.edge = edge

    def hasEdge(self):
        return self.edge is not None
