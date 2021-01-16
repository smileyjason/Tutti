import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

# MOUSE OVER EVENT FOR PYQT

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Hello World!'
        self.setWindowTitle('Hello World!')
        self.left = 10
        self.top = 30
        self.width = 400
        self.height = 400
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.textbox= QtWidgets.QTextEdit(self) #TEXTBOX
        self.textbox.move(30, 30)
        self.textbox.resize(340, 340)
        self.setCentralWidget(self.textbox)

        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Bye bye', 'Are you sure you want to exit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No )

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    win = MainWindow()
    
    #win.setGeometry(200, 200, 1100, 1100)
    #win.setWindowTitle("Hello World!")
    #win.show()
    sys.exit(app.exec_())




    