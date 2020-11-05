import sys, os
from PyQt5 import QtGui
from PyQt5.QtWidgets import QAction, QVBoxLayout, QHBoxLayout, QApplication, \
    QFileDialog, QTextEdit, QPushButton, QLabel, QMainWindow, qApp, QWidget, QMessageBox


class TextEditorTextArea(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.text_area = QTextEdit()
        self.clear = QPushButton("Clear")
        self.open = QPushButton("Open")
        self.save_as = QPushButton("Save As")
        self.save = QPushButton("Save")
        self.file_name = tuple()

        h_box = QHBoxLayout()
        h_box.addWidget(self.clear)
        h_box.addWidget(self.open)
        h_box.addWidget(self.save_as)
        h_box.addWidget(self.save)

        v_box = QVBoxLayout()
        v_box.addWidget(self.text_area)

        v_box.addLayout(h_box)

        self.setLayout(v_box)

        self.clear.clicked.connect(self.text_area.clear)
        self.open.clicked.connect(self.open_file)
        self.save_as.clicked.connect(self.save_as_file)
        self.save.clicked.connect(self.save_file)

    def open_file(self):
        print("Opening a file...")
        file_name = tuple()
        try:
            file_name = QFileDialog.getOpenFileName(self, "Open File",
                                                    os.getenv("HOME"))
            with open(file_name[0], "r") as file:
                self.text_area.setText(file.read())
            print('file open successful')
        except:
            pass
        editor.setWindowTitle("My Text Editor V.0.1 - " + file_name[0].rsplit("/")[-1])
        return file_name

    def save_as_file(self):
        print('Save as called...')
        try:
            file_name = QFileDialog.getSaveFileName(self, "Save File As..")
            with open(file_name[0], "w") as file:
                file.write(self.text_area.toPlainText())
        except:
            pass
        editor.setWindowTitle("My Text Editor V.0.1 - " + file_name[0].rsplit("/")[-1])
        return file_name

    def save_file(self):
        print("save function called")
        with open(self.file_name[0], "r+") as file:
            file.write(self.text_area.toPlainText())
        print("file saved")

    def is_file_changed(self):
        print('is file changed method called')
        if len(self.file_name) == 0:
            if len(self.text_area.toPlainText()) != 0:
                answer = True
            else:
                answer = False
        else:
            with open(self.file_name[0], "r") as file:
                answer = file.read() != self.text_area.toPlainText()
        print("is file changed? " + str(answer))
        return answer


class MyTextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.active_file = "New File.txt"
        self.text_edit = TextEditorTextArea()
        self.setCentralWidget(self.text_edit)
        self.setWindowTitle("My Text Editor V.0.1 - " + self.active_file)
        self.create_menus()
        self.setGeometry(1000, 200, 450, 550)
        self.show()

    def create_menus(self):
        menubar = self.menuBar()

        file = menubar.addMenu("File")
        open_file = QAction("Open...", self)
        open_file.setShortcut("Ctrl+O")
        file.addAction(open_file)
        save = QAction("Save", self)
        save.setShortcut("Ctrl+s")
        file.addAction(save)
        save_as = QAction("Save As...", self)
        save_as.setShortcut("Shift+s")
        file.addAction(save_as)
        close = QAction("Exit", self)
        close.setShortcut("Ctrl+q")
        file.addAction(close)

        edit = menubar.addMenu("Edit")
        undo = QAction("Undo", self)
        undo.setShortcut("Ctrl+z")
        edit.addAction(undo)
        redo = QAction("Redo", self)
        redo.setShortcut("Ctrl+Shift+z")
        edit.addAction(redo)
        clear = QAction("Clear", self)
        edit.addAction(clear)

        file.triggered.connect(self.file_actions)
        edit.triggered.connect(self.edit_actions)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'MyTextEditor',
                                     "I suggest you save your changes! Do you want to save your changes?",
                                     QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)

        if reply == QMessageBox.Yes:
            # Save file and close
            self.text_edit.save_file()
            event.accept()
        elif reply == QMessageBox.No:
            # Don't save and close file and program
            event.accept()
        else:
            # Go back to the file and don't do anything
            event.ignore()

    def file_actions(self, action):
        if action.text() == "Open...":
            print('File action Open called')
            if self.text_edit.is_file_changed():
                print('file changed asking to save')
                ask = QMessageBox.question(self, 'MyTextEditor',
                                           "I suggest you save your changes! Do you want to save your changes?",
                                           QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)
                if ask != QMessageBox.Cancel:
                    if ask == QMessageBox.Yes:
                        if len(self.text_edit.file_name) == 0:
                            self.text_edit.file_name = self.text_edit.save_file_as()
                    self.text_edit.file_name = self.text_edit.open_file()
        elif (action.text() == "Save" and len(self.text_edit.file_name) == 0) or action.text() == "Save As...":
            self.text_edit.file_name = self.text_edit.save_as_file()
        elif action.text() == "Save":
            self.text_edit.save_file()
        elif action.text() == "Exit":
            self.close()

    def edit_actions(self, action):
        if action.text() == "Undo":
            pass
        elif action.text() == "Redo":
            pass
        elif action.text() == "Clear":
            self.text_edit.text_area.clear()


app = QApplication(sys.argv)
editor = MyTextEditor()
sys.exit(app.exec_())
