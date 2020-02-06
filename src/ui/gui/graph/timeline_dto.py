
from graph.gr_timeline import GRTimeline


#The orientation of the Timeline
VERTICAL = 1
HORIZONTAL = 2

#Interval units
SECONDS = 1
MINUTES = 2
HOURS = 3

class Timeline():

    def __init__(self, scene, interval_units = SECONDS, orientation=VERTICAL):
        super().__init__()

        self.scene = scene
        self.interval_units = interval_units
        self.orientation = orientation

        self.gr_timeline = GRTimeline(self)
        self.scene.setTimeline(self.gr_timeline)
        self.scene.grScene.addItem(self.gr_timeline)

    @property
    def pos(self):
        return self.gr_timeline.pos()
    def setPor(self, x, y):
        self.gr_timeline.setPos(x, y)
