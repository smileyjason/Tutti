import sys
from PyQt5.QtWidgets import *



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

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
    
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("Hello World!")
    win.show()
    sys.exit(app.exec_())




    