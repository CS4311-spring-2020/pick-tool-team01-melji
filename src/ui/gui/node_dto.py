from gr_node import GRNode

class Node():
    def __init__(self, scene, title ="undifined"):
        super().__init__()
        self.scene = scene
        self.title = title
        self.grNode = GRNode(self, self.title)

        self.scene.addNode(self)
        self.scene.grScene.addItem(self.grNode)

        self.inputs = []
        self.outputs = []