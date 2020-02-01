
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

class TemplateforPICK(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        #this is where the toolbar elements are set up

        self.toolbar = self.addToolBar('UI')

        fileAct = QAction(QIcon('bin\\assets\\file.png'), 'file', self)
        fileAct.setShortcut('Ctrl+X')

        #use following code for actions 
        #fileAct.triggered.connect(filepopup()**note function call may not be correct**) 
        #self.toolbar.addAction(fileAct)

        saveAct = QAction(QIcon('bin\\assets\\save.png'), 'save', self)
        saveAct.setShortcut('Ctrl+S')
        #saveAct.triggered.connect(saveaction())
        #self.toolbar.addAction(saveAct)
        
        vcAct = QAction(QIcon('bin\\assets\\VC.jpg'), 'version control', self)
        vcAct.setShortcut('Ctrl+N')
        #vcAct.triggered.connect(versionpopup())
        #self.toolbar.addAction(vcAct)

        settingsAct = QAction(QIcon('bin\\assets\\settings.png'), 'settings', self)
        settingsAct.setShortcut('Ctrl+I')
        #settingsAct.triggered.connect(settingspopup())
        #self.toolbar.addAction(settingsAct)

        logviewAct = QAction(QIcon('bin\\assets\\logview.png'), 'log view', self)
        logviewAct.setShortcut('Ctrl+T')
        #logviewAct.triggered.connect(logview())
        #self.toolbar.addAction(logviewAct)

        historyAct = QAction(QIcon('bin\\assets\\history.png'), 'history', self)
        historyAct.setShortcut('Ctrl+H')
        #historyAct.triggered.connect(history popup())
        #self.toolbar.addAction(historyAct)

        
        redoAct = QAction(QIcon('bin\\assets\\redo.png'), 'redo change', self)
        redoAct.setShortcut('Ctrl+Y')
        #redoAct.triggered.connect(redo())
        #self.toolbar.addAction(redoAct)

        undoAct = QAction(QIcon('bin\\assets\\undo.png'), 'undo change', self)
        undoAct.setShortcut('Ctrl+Z')
        #undoAct.triggered.connect(undo())
        #self.toolbar.addAction(undoAct)

        #to-do lock toolbar?
        self.toolbar.addAction(fileAct)
        self.toolbar.addAction(saveAct)
        self.toolbar.addAction(vcAct)
        self.toolbar.addAction(settingsAct)
        self.toolbar.addAction(logviewAct)
        self.toolbar.addAction(historyAct)
        self.toolbar.addAction(redoAct)
        self.toolbar.addAction(undoAct)
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle(currtitle)  
        self.show()
        
        
if __name__ == '__main__':
    currtitle = 'PICK System'  #Use this var to change title
    app = QApplication(sys.argv)
    ex = TemplateforPICK()
    sys.exit(app.exec_())