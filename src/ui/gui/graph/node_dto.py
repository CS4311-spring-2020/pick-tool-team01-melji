from graph.gr_node import GRNode
from graph.node_connector import *
class Node():
    def __init__(self, scene, title ="undifined", inputs = [], outputs = []):
        super().__init__()
        self.scene = scene
        self.title = title
        self.grNode = GRNode(self, self.title)

        self.scene.addNode(self)
        self.scene.grScene.addItem(self.grNode)

        self.inputs = []
        self.outputs = []
        counter = 0
        for iterm in inputs:
            socket = Socket(node=self, index=counter, position=LEFT_TOP)
            counter += 1
            self.inputs.append(socket)
        counter = 0
        for item in outputs:
            socket = Socket(node=self, index=counter, position=RIGHT_TOP)
            counter += 1
            self.outputs.append(socket)
    @property
    def pos(self):
        return self.grNode.pos()        # QPointF
    def setPos(self, x, y):
        self.grNode.setPos(x, y)

    
    def getSocketPosition(self, index, position):
        x = 0 if position in (LEFT_TOP, LEFT_BOTTOM) else self.grNode.radius
        # x = self.grNode.radius 
        y = index * 20
        
        return x, y