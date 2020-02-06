
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import math


class GRTimeline(QGraphicsItem):

    def __init__(self, node):
        super().__init__()

        self.node = node
        self.height = 400
        self._interval_seperation = 30
        self.width = 100
        self._color_background = QColor("#FF0000FF")

        self._pen_default = QPen(QColor("#FF0000FF"))
        self._pen_default.setWidth(3)
        self._pen_selected = QPen(QColor("#32CAF6"))
        self._pen_selected.setWidth(3)
        self._brush = QBrush(self._color_background)


    def boundingRect(self):
        return QRectF(
            0,
            0,
            self.width,
            self.height
        )
    
    def paint( self, painter, item, widget=None):

        main_line = QLineF(0, 0, 0, self.height)
        interval_lines = []
        interval_lines.append(main_line)
        for y in range(0, self.height, self._interval_seperation):
            interval_lines.append(QLineF(-20, y, 20, y))

        painter.setBrush(self._brush)
        painter.setPen(self._pen_default)
        painter.drawLines(interval_lines)

