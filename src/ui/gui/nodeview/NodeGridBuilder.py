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
from nodeview.NodeGridButtonBuilder import GetNodeGridWidgets
from nodeview.SampleNodeDataMaker import GetNodeSampleWidgets
from nodeview.SampleNodeDataMakerSplunk import GetNodeWidgets
from services.intake_service import IntakeService
from random import seed, randint
import random

from src.ui.gui.model.log_entry import LogEntry
from src.ui.gui.nodeview.SampleNodeDataMakerSplunk import LogRandIDTextWidget

OP_CODE_LOG_ENTRY = 1
LISTBOX_MIMETYPE = "application/LogEntry"


class GRLogEntry(QWidget):
    def __init__(self, log_entry_frame, parent=None):
        super(GRLogEntry, self).__init__(parent)

        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(0)
        self.grid_layout.setHorizontalSpacing(0)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.max_height = 50

        for i in range(0, 10):
            arr = log_entry_frame.arrayofsamplewidgets
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
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setDragDropMode(True)

        self.intake_service = IntakeService()
        self.entries = self.intake_service.ingest_files(
            "/Users/eddie/Documents/SchoolProjects/pick-tool-team01-melji/example/")
        # self.entries = [LogEntry("identifier", "timestamp", "content", "host", "source", "sourcetype")]
        gr_log_entry_list = list()
        for entry in self.entries:
            entry_frame = GetNodeWidgets(entry)
            gr_log_entry_list.append(entry_frame)

        self.addLogEntries(gr_log_entry_list)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumHeight(self.sizeHintForRow(0))

    def addLogEntries(self, log_entries):
        for idx, log_entry_frame in enumerate(log_entries):
            item = QListWidgetItem(self)
            self.addItem(item)

            widget = GRLogEntry(log_entry_frame)
            # widget = QLabel("example fomr gss")
            s = QSize()
            s.setHeight(widget.max_height)
            s.setWidth(widget.width())
            item.setSizeHint(s)

            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsDragEnabled)
            item.setData(Qt.UserRole, OP_CODE_LOG_ENTRY)
            node = log_entry_frame.arrayofsamplewidgets[1]
            node_id = node.value
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

    def scrollmake(self):
        self.widget = QWidget()

        self.layoutgrid = QGridLayout()
        self.layoutgrid.setSpacing(0)
        self.layoutgrid.setHorizontalSpacing(0)
        self.layoutgrid.setContentsMargins(0, 0, 0, 0)
        i = 0
        n = 0
        data = GetNodeGridWidgets()
        arrayofwidgets = data.arrayofwidgets

        self.intake_service = IntakeService()
        self.entries = self.intake_service.ingest_files(
            "/Users/eddie/Documents/SchoolProjects/pick-tool-team01-melji/example/")
        for y in range(len(
                self.entries)):  # this code will detect what is in the datatype and put it into spaces in grid layout
            sampledata = GetNodeWidgets(self.entries[y])
            for x in range(0, 10):
                if y < 2:
                    widgettoad = arrayofwidgets[i]
                    self.layoutgrid.addWidget(widgettoad, y, x)
                    i = i + 1


                else:
                    arrayofsamplewidgets = sampledata.arrayofsamplewidgets
                    widgettoad = arrayofsamplewidgets[x]
                    self.layoutgrid.addWidget(widgettoad, y, x)

        self.widget.setLayout(self.layoutgrid)
        self.widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setWidgetResizable(True)
        self.setWidget(self.widget)
        self.updateGeometry

        return
