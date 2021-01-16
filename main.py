from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QDialog, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
import speech_recognition
 
 
class MainWindow(QDialog):

    def setupUi(self, Dialog):
        self.subWindow = None
        #Dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        Dialog.setObjectName("Dialog")
        Dialog.resize(574, 470)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_add = QtWidgets.QPushButton(Dialog)
        self.pushButton_add.setObjectName("pushButton_add")
        
        self.verticalLayout.addWidget(self.pushButton_add)
        self.pushButton_edit = QtWidgets.QPushButton(Dialog)
        self.pushButton_edit.setObjectName("pushButton_edit")
        
        self.verticalLayout.addWidget(self.pushButton_edit)
        self.pushButton_remove = QtWidgets.QPushButton(Dialog)
        self.pushButton_remove.setObjectName("pushButton_remove")
        
        self.verticalLayout.addWidget(self.pushButton_remove)
        self.pushButton_up = QtWidgets.QPushButton(Dialog)
        self.pushButton_up.setObjectName("pushButton_up")
        self.verticalLayout.addWidget(self.pushButton_up)
        self.pushButton_down = QtWidgets.QPushButton(Dialog)
        self.pushButton_down.setObjectName("pushButton_down")
        self.verticalLayout.addWidget(self.pushButton_down)
        self.pushButton_sort = QtWidgets.QPushButton(Dialog)
        self.pushButton_sort.setObjectName("pushButton_sort")
        self.verticalLayout.addWidget(self.pushButton_sort)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_close = QtWidgets.QPushButton(Dialog)
        self.pushButton_close.setObjectName("pushButton_close")
        self.verticalLayout.addWidget(self.pushButton_close)
    
        

        self.hoverButton = QtWidgets.QPushButton(Dialog)
        self.hoverButton.setObjectName("hoverButton")
        self.verticalLayout.addWidget(self.hoverButton)
        
        self.voiceButton = QtWidgets.QPushButton(Dialog)
        self.voiceButton.setObjectName("voiceButton")
        self.verticalLayout.addWidget(self.voiceButton)

        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
 
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton_add.clicked.connect(self.add)
        self.pushButton_edit.clicked.connect(self.edit)
        self.pushButton_remove.clicked.connect(self.remove)
        self.pushButton_up.clicked.connect(self.up)
        self.pushButton_down.clicked.connect(self.down)
        self.pushButton_sort.clicked.connect(self.sort)
        self.pushButton_close.clicked.connect(self.close)
        self.hoverButton.installEventFilter(self)
        self.voiceButton.clicked.connect(self.voicerecognition)
 
        self.TASK()
        
 
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "To-do List"))
        Dialog.setWindowIcon(QIcon("icon.png"))
        self.pushButton_add.setText(_translate("Dialog", "Add"))
        self.pushButton_edit.setText(_translate("Dialog", "Edit"))
        self.pushButton_remove.setText(_translate("Dialog", "Remove"))
        self.pushButton_up.setText(_translate("Dialog", "Up"))
        self.pushButton_down.setText(_translate("Dialog", "Down"))
        self.pushButton_sort.setText(_translate("Dialog", "Sort"))
        self.pushButton_close.setText(_translate("Dialog", "Close"))
        self.hoverButton.setText(_translate("Dialog", "Hover"))
        self.voiceButton.setText(_translate("Dialog", "Speech to Text"))
 
 
 
 
    def TASK(self):
 
 
        self.tasks = ["MAT185"]
        self.listWidget.addItems(self.tasks)
        self.listWidget.setCurrentRow(0)
 
 
    def add(self):
        row = self.listWidget.currentRow()
        text, ok = QInputDialog.getText(self, "To-do List", "Enter Task")
        if ok and text is not None:
            self.listWidget.insertItem(row, text)
        

 
 
 
    def edit(self):
        row = self.listWidget.currentRow()
        item = self.listWidget.item(row)
 
        if item is not None:
            string, ok = QInputDialog.getText(self, "To-do List", "Edit Task",
                                              QLineEdit.Normal, item.text())
            if ok and string is not None:
                item.setText(string)
    
 
 
    def remove(self):
        row = self.listWidget.currentRow()
        item = self.listWidget.item(row)
 
        if item is None:
            return
 
        reply = QMessageBox.question(self, "Remove Task", "Do You Want To Remove Task: " + str(item.text()),
                QMessageBox.Yes|QMessageBox.No)
 
        if reply == QMessageBox.Yes:
            item = self.listWidget.takeItem(row)
            del item
        
 
 
 
    def up(self):
        row = self.listWidget.currentRow()
        if row >= 1:
            item = self.listWidget.takeItem(row)
            self.listWidget.insertItem(row - 1, item)
            self.listWidget.setCurrentItem(item)
 
 
    def down(self):
        row = self.listWidget.currentRow()
        if row < self.listWidget.count() - 1:
            item = self.listWidget.takeItem(row)
            self.listWidget.insertItem(row + 1, item)
            self.listWidget.setCurrentItem(item)
 
 
 
    def sort(self):
        self.listWidget.sortItems()
 
 
 
    def close(self):
        quit()
 
 
    def eventFilter(self, object, event):
        if event.type() == QtCore.QEvent.Enter and self.subWindow == None:
            self.subWindow = True
            self.callAnotherQMainWindow()
            return True
        elif event.type() == QtCore.QEvent.Leave and self.subWindow != None:
            self.subWindow.close()
            self.subWindow = None
            return False
        return False
    
    def callAnotherQMainWindow(self):
        self.subWindow = ChildWindow(self)
        self.setWindowOpacity(0.)
        self.newWindow = True
        return self.subWindow

    def voicerecognition(self):
        try:
            # read the audio data from the default microphone
            command = self.speechtotext()

            if command == "add":
                try:
                    text = self.speechtotext()

                    row = self.listWidget.currentRow()
                    if text is not None:
                        self.listWidget.insertItem(row, text)

                except:
                    print("Sorry. Could not understand.")


            elif command == "edit":
                try:
                    text = self.speechtotext()

                    row = self.listWidget.currentRow()
                    item = self.listWidget.item(row)
                
                    if item is not None and text is not None:
                        item.setText(text)

                except:
                    print("Sorry. Could not understand.")
                   

            elif command == "remove":
                try:
                    text = self.speechtotext()

                    row = self.listWidget.currentRow()
                    item = self.listWidget.item(row)
            
                    if item is None:
                        return
                    item = self.listWidget.takeItem(row)
                    del item

                except:
                    print("Sorry. Could not understand.")
                
            elif command == "up":
                try:
                    text = self.speechtotext()

                    row = self.listWidget.currentRow()
                    if row >= 1:
                        item = self.listWidget.takeItem(row)
                        self.listWidget.insertItem(row - 1, item)
                        self.listWidget.setCurrentItem(item)

                except:
                    print("Sorry. Could not understand.")
            
            elif command == "down":
                try:
                    text = self.speechtotext()

                    row = self.listWidget.currentRow()
                    if row < self.listWidget.count() - 1:
                        item = self.listWidget.takeItem(row)
                        self.listWidget.insertItem(row + 1, item)
                        self.listWidget.setCurrentItem(item)

                except:
                    print("Sorry. Could not understand.")

            elif command == "sort":
                try:
                    text = self.speechtotext()

                    self.listWidget.sortItems()

                except:
                    print("Sorry. Could not understand.")
                    
            elif command == "close":
                try:
                    text = self.speechtotext()

                    quit()

                except:
                    print("Sorry. Could not understand.")


        except Exception as ex:
            print("Sorry. Could not understand.")
            
    def speechtotext(self):
        recognizer = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as src:
            audio_data = recognizer.record(src, duration=4)
            print("Recognizing...")
            # convert speech to text
            text = recognizer.recognize_google(audio_data)
            print(text)       
            return text

    
class ChildWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.parent = parent
        self.show()
        

    def closeEvent(self, QCloseEvent):
        self.parent.setWindowOpacity(1.)
 
 
 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = MainWindow()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())