from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class GRNode(QGraphicsItem):
    def __init__(self, node, title='Node Graphics Item', parent=None):
        super().__init__(parent)
        self._title_color = Qt.black        
        self.radius = 90

        self.width = 180
        self._padding = 10.0

        self._pen_default = QPen(QColor("#7F000000"))
        self._pen_default.setWidth(3)
        self._pen_selected = QPen(QColor("#FFFFA637"))
        self._pen_selected.setWidth(3)

        self._brush_title = QBrush(QColor("#FF313131"))
        self._brush_background = QBrush(QColor("#E3212121"))

        self.initTitle()
        self.title = title


        self.initUI()


    def boundingRect(self):
        return QRectF(
            0,
            0,
            self.radius,
            self.radius
        ).normalized()
        

    def initUI(self):
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemIsMovable)


    def initTitle(self):
        self.title_item = QGraphicsTextItem(self)
        self.title_item.setDefaultTextColor(self._title_color)
        self.title_item.setPos(self._padding, 20)#TODO: Put the title of the ndoe in the middle of the ndoe
        self.title_item.setTextWidth(
            self.radius
            - 2 * self._padding
        )

    @property
    def title(self): return self._title
    @title.setter
    def title(self, value):
        self._title = value
        self.title_item.setPlainText(self._title)


    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
        path_outline = QPainterPath()
        path_outline.addEllipse(0, 0, self.radius, self.radius)
        painter.setPen(self._pen_default if not self.isSelected() else self._pen_selected)
        painter.setBrush(QBrush(Qt.white, Qt.SolidPattern))
        painter.drawPath(path_outline.simplified())
