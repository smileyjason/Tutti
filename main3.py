# toggle theme added
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QDialog, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon, QFont
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QInputDialog, QDialog, QLineEdit, QMessageBox
import speech_recognition   
import csv
 
 
class MainWindow(QDialog):

    def setupUi(self, Dialog):

        self.theme = 1
        
        self.subWindow = None
        self. setWindowFlags(self.windowFlags()| QtCore.Qt.WindowStaysOnTopHint)
        Dialog.setObjectName("Dialog")
        Dialog.setGeometry(40,40,1000,1000)
        Dialog.resize(500, 700) #width and height
        Dialog.setStyleSheet("background-image: url(C://Users//asus//Desktop//chrome_extension//HackTheNorth//Chrome_extension//sky.png); ")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(Dialog)

        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        
        #add button
        self.pushButton_add = QtWidgets.QPushButton(Dialog)
        self.pushButton_add.setObjectName("pushButton_add")
        self.verticalLayout.addWidget(self.pushButton_add)
        
        #edit button
        self.pushButton_edit = QtWidgets.QPushButton(Dialog)
        self.pushButton_edit.setObjectName("pushButton_edit")
        self.verticalLayout.addWidget(self.pushButton_edit)

        #remove button
        self.pushButton_remove = QtWidgets.QPushButton(Dialog)
        self.pushButton_remove.setObjectName("pushButton_remove")
        self.verticalLayout.addWidget(self.pushButton_remove)

        ##this is the button to move up
        self.pushButton_up = QtWidgets.QPushButton(Dialog)
        self.pushButton_up.setObjectName("pushButton_up")
        self.verticalLayout.addWidget(self.pushButton_up)
        
        ##this is the button to move down
        self.pushButton_down = QtWidgets.QPushButton(Dialog)
        self.pushButton_down.setObjectName("pushButton_down")
        self.verticalLayout.addWidget(self.pushButton_down)

        ##this is the button to sort
        self.pushButton_sort = QtWidgets.QPushButton(Dialog)
        self.pushButton_sort.setObjectName("pushButton_sort")
        self.verticalLayout.addWidget(self.pushButton_sort)
        
        #spacer btwn types of buttons
        spacerItem = QtWidgets.QSpacerItem(5, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        #toggle theme button
        self.pushButton_toggletheme = QtWidgets.QPushButton(Dialog)
        self.pushButton_toggletheme.setObjectName("pushButton_toggletheme")
        self.verticalLayout.addWidget(self.pushButton_toggletheme)
        
        #Open csv button

        self.pushButton_open = QtWidgets.QPushButton(Dialog)
        self.pushButton_open.setObjectName("pushButton_open")
        self.verticalLayout.addWidget(self.pushButton_open)

        #Save csv button
        self.pushButton_save = QtWidgets.QPushButton(Dialog)
        self.pushButton_save.setObjectName("pushButton_save")
        self.verticalLayout.addWidget(self.pushButton_save)
    
        #hover/hide button (FIX)
        self.pushButton_hide = QtWidgets.QPushButton(Dialog)
        self.pushButton_hide.setObjectName("pushButton_hide")
        self.verticalLayout.addWidget(self.pushButton_hide)

    
        #push to talk button
        self.voiceButton = QtWidgets.QPushButton(Dialog)
        self.voiceButton.setObjectName("voiceButton")
        self.verticalLayout.addWidget(self.voiceButton)

        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        ##this is the quit button        
        self.pushButton_quit = QtWidgets.QPushButton(Dialog)
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.verticalLayout.addWidget(self.pushButton_quit)


 
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        #directing the buttons to different functions when clicked
        self.pushButton_add.clicked.connect(self.add)
        self.pushButton_edit.clicked.connect(self.edit)
        self.pushButton_remove.clicked.connect(self.remove)
        self.pushButton_up.clicked.connect(self.up)
        self.pushButton_down.clicked.connect(self.down)
        self.pushButton_sort.clicked.connect(self.sort)
        self.pushButton_hide.clicked.connect(self.hide)
        self.voiceButton.clicked.connect(self.voicerecognition)
        self.pushButton_open.clicked.connect(self.opencsv)
        self.pushButton_save.clicked.connect(self.saveFileDialog)
        self.pushButton_quit.clicked.connect(self.quit)
        self.pushButton_toggletheme.clicked.connect(self.toggletheme)

        self.TASK()

        
 
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Tutti"))

        Dialog.setWindowIcon(QIcon("icon.png"))

        self.pushButton_add.setText(_translate("Dialog", "Add"))
        self.pushButton_add.setStyleSheet("font: 10pt Comic Sans MS")

        self.pushButton_edit.setText(_translate("Dialog", "Edit"))
        self.pushButton_edit.setStyleSheet("font: 10pt Comic Sans MS")

        self.pushButton_remove.setText(_translate("Dialog", "Remove"))
        self.pushButton_remove.setStyleSheet("font: 10pt Comic Sans MS")

        self.pushButton_up.setText(_translate("Dialog", "Up"))
        self.pushButton_up.setStyleSheet("font: 10pt Comic Sans MS")

        self.pushButton_down.setText(_translate("Dialog", "Down"))
        self.pushButton_down.setStyleSheet("font: 10pt Comic Sans MS")

        self.pushButton_sort.setText(_translate("Dialog", "Sort"))
        self.pushButton_sort.setStyleSheet("font: 10pt Comic Sans MS")

        self.pushButton_hide.setText(_translate("Dialog", "Hide"))
        self.pushButton_hide.setStyleSheet("font: 10pt Comic Sans MS")

        self.pushButton_toggletheme.setText(_translate("Dialog", "Toggle Theme"))
        self.pushButton_toggletheme.setStyleSheet("font: 10pt Comic Sans MS")

        self.pushButton_quit.setText(_translate("Dialog", "Quit"))
        self.pushButton_quit.setStyleSheet("font: 10pt Comic Sans MS")

        self.voiceButton.setText(_translate("Dialog", "Speech to Text"))
        self.voiceButton.setStyleSheet("font: 10pt Comic Sans MS")

        self.pushButton_open.setText(_translate("Dialog", "Open"))
        self.pushButton_open.setStyleSheet("font: 10pt Comic Sans MS")

        self.pushButton_save.setText(_translate("Dialog", "Save"))
        self.pushButton_save.setStyleSheet("font: 10pt Comic Sans MS")


    def TASK(self):

        self.tasks = {}
        row = self.listWidget.currentRow()
        self.listWidget.insertItem(row, "Task" + "     " + "Deadline")
        self.listWidget.setCurrentRow(0)
 
 
    def add(self):
        date = " "
        
        row = self.listWidget.currentRow()
        text, ok = QInputDialog.getText(self, "To-do List", "Enter Task")
        while date != "" and (len(date) != 10 or date[4] != "/" or date[7] != "/" or not ok2):
            date, ok2 = QInputDialog.getText(self, "Do by", "Enter Date (yyyy/mm/dd)")
            
        if ok and text is not None and date == "":
            self.listWidget.insertItem(row, text)
            self.tasks.update({text : text})


        elif ok and text is not None and ok2 and date is not None:
            self.listWidget.insertItem(row, text + "     " + date.split(".")[0])
            while date in self.tasks.keys():
                date = date + "."
            
            self.tasks.update({date : text})
        

    def edit(self):
        row = self.listWidget.currentRow()
        item = self.listWidget.item(row)
 
        if item is not None:
            string, ok = QInputDialog.getText(self, "To-do List", "Edit Task",
                                              QLineEdit.Normal, item.text().split("     ")[0])
            deadline = " "
            while deadline != "" and (len(deadline) != 10 or deadline[4] != "/" or deadline[7] != "/" or not ok2):
                deadline, ok2 = QInputDialog.getText(self, "To-do List", "Edit Deadline", QLineEdit.Normal, item.text().split("     ")[1])
            
            if ok and string is not None:
                if deadline == "":
                    item.setText(string)
                    text = str(item.text())
                    self.tasks.update({text : text})
                
                else:
                    item.setText(string + "     " + deadline)
                    self.tasks.update({deadline : string})
    
 
    def remove(self):
        
        row = self.listWidget.currentRow()
        item = self.listWidget.item(row)
 
        if item is None:
            return
 
        reply = QMessageBox.question(self, "Remove Task", "Do You Want To Remove Task: " + str(item.text()),
                QMessageBox.Yes|QMessageBox.No)
 
        if reply == QMessageBox.Yes:
            item = self.listWidget.takeItem(row)
            text = str(item.text())

            if len(text.split("     ")) == 1:
                del self.tasks[text.split("     ")[0]]
                del item
            else:
                date = text.split("     ")[1]
                task = text.split("     ")[0]
                while self.tasks[date] != task:
                    date = date + "."
                del self.tasks[date]
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
        row = len(self.tasks.items())
        sorteditems = sorted(self.tasks.items())
        self.listWidget.clear()
        nodeadline = []
        for item in sorteditems:
            if item[0] == item[1]:
                nodeadline.append(item)
            else:
                self.listWidget.insertItem(row, item[1].split(".")[0] + "     " + item[0])
        for nodead in nodeadline:
            self.listWidget.insertItem(row, nodead[1])
 
 
    def quit(self):
        quit()
 
    def hide(self):
        #self.setWindowOpacity(0.)
        Dialog.close()
        self.callAnotherQMainWindow()
        return True
        
    #TO DO

    def toggletheme(self):
        if self.theme == 7:
            self.theme == 1
        else:
            self.theme += 1

        if self.theme == 1:
            pass
        elif self.theme == 2:
            pass
        elif self.theme == 3: 
            pass
        elif self.theme == 4:
            pass
        elif self.theme == 5:
            pass
        elif self.theme == 6:
            pass
        elif self.theme == 7:
            pass

    
    def callAnotherQMainWindow(self):
        self.subWindow = ChildWindow(self)
        self.newWindow = True
        return self.subWindow

    def voicerecognition(self):
        try:
            # read the audio data from the default microphone
            text = self.speechtotext()
            if " " not in text:
                command = text
            else:
                command = text.split()[0]
                text = text[text.index(" ") + 1:]

            if command == "add":
                reply = QMessageBox.question(self, "Add Task", "Do You Want To Add Task: " + text, QMessageBox.Yes|QMessageBox.No)
                if reply == QMessageBox.Yes:

                    row = self.listWidget.currentRow()
                    if text is not None:
                        self.listWidget.insertItem(row, text)

                    else:
                        return
                else:
                    return


            elif command == "edit":
                reply = QMessageBox.question(self, "Edit Task", "Do You Want To Edit Task To: " + text, QMessageBox.Yes|QMessageBox.No)
                if reply == QMessageBox.Yes:

                    row = self.listWidget.currentRow()
                    item = self.listWidget.item(row)
                
                    if item is not None and text is not None:
                        item.setText(text)
                    else:
                        return
                else:
                    return

            elif command == "remove":
                reply = QMessageBox.question(self, "Remove Task", "Do You Want To Remove Task: " + text, QMessageBox.Yes|QMessageBox.No)
                if reply == QMessageBox.Yes:

                    row = self.listWidget.currentRow()
                    item = self.listWidget.item(row)
                    if item is None:
                        return
                    else:
                        item = self.listWidget.takeItem(row)
                        del item

            elif command == "up":

                row = self.listWidget.currentRow()
                if row >= 1:
                    item = self.listWidget.takeItem(row)
                    self.listWidget.insertItem(row - 1, item)
                    self.listWidget.setCurrentItem(item)

            elif command == "down":
                row = self.listWidget.currentRow()
                if row < self.listWidget.count() - 1:
                    item = self.listWidget.takeItem(row)
                    self.listWidget.insertItem(row + 1, item)
                    self.listWidget.setCurrentItem(item)

            elif command == "sort":
                self.listWidget.sortItems()

            elif command == "close":
                quit()
            else:
                reply = QMessageBox.question(self, "Error", "Here's what I heard: " + "\"" + text + "\"", QMessageBox.Ok)
                return


        except Exception as ex:
            reply = QMessageBox.question(self, "Sorry", "Sorry. I didn't catch that.", QMessageBox.Ok)
            return

    def speechtotext(self):
        recognizer = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as src:
            audio_data = recognizer.record(src, duration=4)
            print("Recognizing...")
            # convert speech to text
            text = recognizer.recognize_google(audio_data)
            print(text)       
            return text

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        fileName, _ = QFileDialog.getSaveFileName(self,"Save File","","CSV Files (*.csv)")

        try:
            
            with open(fileName, "w") as fileInput:
                fileWriter = csv.writer(fileInput, delimiter = ",", quotechar = '"', quoting = csv.QUOTE_MINIMAL) 
                for row in self.tasks.items():
                    if row:
                        if row[0] == row[1]:
                            fileWriter.writerow([row[1]])
                        else:
                            fileWriter.writerow([row[1], row[0]])
        except:
            return    

            #### MAKE NEW CSV WITH THE CURRENT DICT
    def opencsv(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Load File","","CSV Files (*.csv)")
        try:
            with open(fileName, "r") as fileInput:
                for row in csv.reader(fileInput):
                    if row:
                        if "\t" in row[0]:
                            date = row[0].split("\t")[1]
                            date = date.replace("-","/")
                            text = row[0].split("\t")[0]

                            if date == "":
                                self.tasks.update({text : text})
                            else:
                                while date in self.tasks.keys():
                                    date = date + "."    
                                self.tasks.update({date : text})
                        else:
                            text = row[0]
                            if len(row) == 1:
                                self.tasks.update({text : text})
                            elif len(row) == 2:
                                date = row[1]
                                while date in self.tasks.keys():
                                    date = date + "."
                                self.tasks.update({date : row[0]})
                self.sort()
        except:
            return
                

    
class ChildWindow(QtWidgets.QMainWindow):
    def __init__(self,children = None):
        super().__init__(children)
        self.children = children
        self.subWindow = None
        self.setGeometry(200,400,100,20)
        
        self.setWindowFlags(
                Qt.FramelessWindowHint

            |   Qt.SplashScreen
        )

       #makes the button
        self.button = QtWidgets.QPushButton("Hover", self)
        self.button.setGeometry(11,1,50,20) # x,y, width, height
        self.button.installEventFilter(self)
        sg = QDesktopWidget().availableGeometry() # height of the screen
        self.move(0,(sg.height() - self.geometry().height())/2)

        

        self.show()

    
    def eventFilter(self, object, event):
        if event.type() == QtCore.QEvent.Enter and self.subWindow == None:
            self.subWindow = True
            self.callAnotherQMainWindow()

            #self.close()
          
            return True    

            
        return False

    def callAnotherQMainWindow(self):
        
        self.setWindowOpacity(0.)
        
        Dialog.show()
        
       

    def closeEvent(self, QCloseEvent):
        pass
 
stylesheet = """
    MainWindow {
        background-image: url("C://Users//asus//Desktop//Hack the North//sky.png"); 
        background-repeat: no-repeat; 
        background-position: center;
    }
"""

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    Dialog = QtWidgets.QDialog()

    Dialog.setStyleSheet(stylesheet)

    ui = MainWindow()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())