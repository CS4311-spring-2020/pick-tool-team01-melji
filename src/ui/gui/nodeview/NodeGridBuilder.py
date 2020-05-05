#############################################################################
##  This code shoveswhatever is in an array of "LogInfo" into individual spaces - todo
##  Thanks - Micheal 2/1/20
#############################################################################
from PyQt5.QtCore import *
from PyQt5.QtGui import QDrag
from PyQt5.QtWidgets import QWidget, QGridLayout, QListWidget, QAbstractItemView, \
    QListWidgetItem
from nodeview.SampleNodeDataMaker import GetNodeWidgets

from src.ui.gui.nodeview.NodeGridButtonBuilder import GetNodeGridWidgets
from src.ui.gui.nodeview.SampleNodeDataMaker import heightofrows

OP_CODE_LOG_ENTRY = 1
LISTBOX_MIMETYPE = "application/LogEntry"


class GRNodeEntry(QWidget):
    def __init__(self, node_frame, margin=5, parent=None):
        super(GRNodeEntry, self).__init__(parent)

        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(0)
        self.grid_layout.setHorizontalSpacing(0)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.max_height = 50

        for i in range(0, len(node_frame.arrayofsamplewidgets)):
            arr = node_frame.arrayofsamplewidgets
            widget = arr[i]
            if widget.height() > self.max_height:
                max_height = widget.height()
            self.grid_layout.addWidget(widget, 0, i)
            self.grid_layout.setContentsMargins(margin, margin, margin, margin)

        # self.setMinimumHeight(self.max_height)
        self.setLayout(self.grid_layout)


class NodeGridMake(QListWidget):
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

        self.addHeader()
        self.addNodeEntries(gr_log_entry_list)

    def addHeader(self):
        data = GetNodeGridWidgets()

        top = GetNodeGridWidgets()
        top.arrayofsamplewidgets = data.arrayofsamplewidgets[0:11]

        bottom = GetNodeGridWidgets()
        bottom.arrayofsamplewidgets = data.arrayofsamplewidgets[11:22]

        gr_top = GRNodeEntry(top, margin=0)
        gr_bottom = GRNodeEntry(bottom, margin=0)

        s = QSize()
        s.setHeight(30)
        s.setWidth(gr_top.width())

        self.replaceItem(gr_bottom, s)
        self.replaceItem(gr_top, s)

    def replaceItem(self, widget, min_size):
        item = QListWidgetItem(self)
        item.setSizeHint(min_size)
        self.addItem(item)
        self.setItemWidget(item, widget)

    def addNodeEntries(self, node_list):
        for idx, node in enumerate(node_list):
            item = QListWidgetItem(self)
            self.addItem(item)

            widget = GRNodeEntry(node)
            s = QSize()
            s.setHeight(heightofrows)
            s.setWidth(widget.width())
            item.setSizeHint(s)

            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsDragEnabled)
            item.setData(Qt.UserRole, OP_CODE_LOG_ENTRY)
            node = node.arrayofsamplewidgets[1]
            node_id = node.text

            item.setText(str(node_id))
            self.setItemWidget(item, widget)

    def startDrag(self, *args, **kwargs):
        try:
            item = self.currentItem()
            op_code = item.data(Qt.UserRole)
            print("dragging item <%d>" % op_code, item)

            itemData = QByteArray()
            dataStream = QDataStream(itemData, QIODevice.WriteOnly)
            dataStream.writeInt(op_code)
            dataStream.writeQString(item.text())

            mimeData = QMimeData()
            mimeData.setData(LISTBOX_MIMETYPE, itemData)

            drag = QDrag(self)
            drag.setMimeData(mimeData)

            drag.exec_(Qt.MoveAction)

        except Exception as e:
            print(e)

