################################### hack the north 2021


import sys

from PyQt5 import QtGui, QtCore,QtWidgets

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import *


class Main(QtWidgets.QMainWindow):
 
    def __init__(self, parent = None):
        #QtWidgets.QMainWindow.__init__(self,parent)
        QtWidgets.QMainWindow.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint)
        self.initUI()

     ############################################################################
    def initToolbar(self):
    
        self.toolbar = self.addToolBar("Options")
        
        # Makes the next toolbar appear underneath this one
        self.addToolBarBreak()
    #add a tool bar
    def initFormatbar(self):
    
        self.formatbar = self.addToolBar("Format")
    #make the tool bar
    def initMenubar(self):
    
        menubar = self.menuBar()
        
        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        view = menubar.addMenu("View")
    
    def initUI(self):
    
        self.text = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text)
    
        self.initToolbar()
        self.initFormatbar()
        self.initMenubar()
    
        # Initialize a statusbar for the window
        self.statusbar = self.statusBar()
    
        # x and y coordinates on the screen, width, height
        self.setGeometry(10,30,500,1030)
    
        self.setWindowTitle("Notepad")

def main():
 
    app = QtWidgets.QApplication(sys.argv)
 
    main = Main()
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()