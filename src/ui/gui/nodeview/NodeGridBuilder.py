#############################################################################
##  This code shoveswhatever is in an array of "LogInfo" into individual spaces - todo
##  Thanks - Micheal 2/1/20
#############################################################################
from random import randint

from PyQt5.QtWidgets import QWidget, QGridLayout, QSizePolicy, QListWidget, QAbstractItemView
from nodeview.NodeGridButtonBuilder import GetNodeGridWidgets
from nodeview.SampleNodeDataMaker import GetNodeSampleWidgets

from src.ui.gui.model.log_entry import LogEntry


class NodeGridMake(QListWidget):
    def __init__(self, parent=None):
        super(NodeGridMake, self).__init__(parent)
        self.scrollmake()

    def initUI(self):

        self.SelectionMode(QAbstractItemView.SingleSelection)
        self.setDragDropMode(True)
        self.addItems();

    def addItems(self):
        example_log_entry = LogEntry()



    def addLogEntryItem(self, log_entry, op_code):
        pass


    def scrollmake(self):
        self.widget = QWidget()

        self.layoutgrid = QGridLayout()
        self.layoutgrid.setSpacing(0)
        self.layoutgrid.setHorizontalSpacing(0)
        self.layoutgrid.setContentsMargins(0, 0, 0, 0)
        # self.layoutgrid.setDragEnable(True)

        i = 0
        n = 0
        data = GetNodeGridWidgets()
        arrayofwidgets = data.arrayofwidgets

        numofsample = 0
        numofsample = randint(2, 98)

        for y in range(0,
                       numofsample):  # this code will detect what is in the datatype and put it into spaces in grid layout
            sampledata = GetNodeSampleWidgets()
            for x in range(0, 11):
                if y < 2:
                    widgettoad = arrayofwidgets[i]
                    # widgettoad.setDragEnable(True)
                    self.layoutgrid.addWidget(widgettoad, y, x)
                    i = i + 1

                else:
                    arrayofsamplewidgets = sampledata.arrayofsamplewidgets
                    widgettoad = arrayofsamplewidgets[x]
                    # widgettoad.setDragEnabled(True)
                    self.layoutgrid.addWidget(widgettoad, y, x)
                    n = n + 1

        self.widget.setLayout(self.layoutgrid)
        self.widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.setWidgetResizable(True)
        self.setWidget(self.widget)
        self.updateGeometry
        # this code sets borders to 1px
        # QRegExp regexp(".*border: *(\\d+)px.*");
        # if (regexp.indexIn(btn->styleSheet()) >= 0)
        # qDebug() << regexp.cap(1);

        return
