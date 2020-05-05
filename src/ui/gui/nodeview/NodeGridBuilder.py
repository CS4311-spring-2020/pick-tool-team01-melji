
#############################################################################
##  This code shoveswhatever is in an array of "LogInfo" into individual spaces - todo
##  Thanks - Micheal 2/1/20
#############################################################################
import sys
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtGui import QDrag
from PyQt5.QtWidgets import QScrollArea, QWidget, QGridLayout, QLabel, QSizePolicy, QListWidget, QAbstractItemView, \
    QListWidgetItem, QHBoxLayout, QPushButton
from nodeview.SampleNodeDataMaker import GetNodeWidgets
from services.intake_service import IntakeService
from random import seed, randint
import random

from src.ui.gui.model.log_entry import LogEntry
from src.ui.gui.nodeview.SampleNodeDataMakerSplunk import LogRandIDTextWidget

OP_CODE_LOG_ENTRY = 1
LISTBOX_MIMETYPE = "application/LogEntry"


class GRNodeEntry(QWidget):
    def __init__(self, node_frame, parent=None):
        super(GRNodeEntry, self).__init__(parent)

        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(0)
        self.grid_layout.setHorizontalSpacing(0)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.max_height = 50

        for i in range(0, 10):
            arr = node_frame.arrayofsamplewidgets
            widget = arr[i]
            if widget.height() > self.max_height:
                max_height = widget.height()
            self.grid_layout.addWidget(widget, 0, i)
            self.grid_layout.setContentsMargins(5, 5, 5, 5)

        self.setMinimumHeight(self.max_height)
        self.setLayout(self.grid_layout)


class NodeGridMake(QListWidget):
    # def __init__(self, parent=None):
    #     super(NodeGridMake, self).__init__(parent)
    #     self.initUI()
    # self.scrollmake()
    def __init__(self, vector, parent=None):
        super(NodeGridMake, self).__init__(parent)
        self.vector = vector
        self.initUI()

    def initUI(self):
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setDragDropMode(True)

        node_list = self.vector.node_list
        gr_log_entry_list = list()
        for node in node_list:
            entry_frame = GetNodeWidgets(node)
            gr_log_entry_list.append(entry_frame)

        self.addLogEntries(gr_log_entry_list)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumHeight(self.sizeHintForRow(0))

    def addLogEntries(self, node_list):
        for idx, node in enumerate(node_list):
            item = QListWidgetItem(self)
            self.addItem(item)

            widget = GRNodeEntry(node)
            # widget = QLabel("example fomr gss")
            s = QSize()
            s.setHeight(widget.max_height)
            s.setWidth(widget.width())
            item.setSizeHint(s)

            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsDragEnabled)
            item.setData(Qt.UserRole, OP_CODE_LOG_ENTRY)
            node = node.arrayofsamplewidgets[1]
            node_id = node.text
            item.setText(str(node_id))
            self.setItemWidget(item, widget)

    def startDrag(self, *args, **kwargs):
        # print("ListBox::startDrag")

        try:
            item = self.currentItem()
            op_code = item.data(Qt.UserRole)
            print("dragging item <%d>" % op_code, item)

            # pixmap = QPixmap(item.data(Qt.UserRole))

            itemData = QByteArray()
            dataStream = QDataStream(itemData, QIODevice.WriteOnly)
            # dataStream << pixmap
            dataStream.writeInt(op_code)
            dataStream.writeQString(item.text())

            mimeData = QMimeData()
            mimeData.setData(LISTBOX_MIMETYPE, itemData)

            drag = QDrag(self)
            drag.setMimeData(mimeData)
            # drag.setHotSpot(QPoint(pixmap.width() / 2, pixmap.height() / 2))
            # drag.setPixmap(pixmap)

            drag.exec_(Qt.MoveAction)

        except Exception as e:
            print(e)