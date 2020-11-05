import sys

from PyQt5.QtWidgets import QApplication, QAction, qApp, QMainWindow


class TextEditorMenu(QMainWindow):

    def __init__(self):
        super().__init__()
        menubar = self.menuBar()
        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")

        open_file = QAction("Open", self)
        open_file.setShortcut("Ctrl+o")

        save_file = QAction("Save", self)
        save_file.setShortcut("Ctrl+s")

        shutdown = QAction("Exit", self)
        shutdown.setShortcut("Ctrl+q")

        file.addAction(open_file)
        file.addAction(save_file)
        file.addAction(shutdown)

        find_replace = edit.addMenu("Find and Replace")
        find = QAction("Find", self)
        replace = QAction("Replace", self)
        clear = QAction("Clear", self)
        edit.addAction(clear)
        find_replace.addAction(find)
        find_replace.addAction(replace)

        self.setWindowTitle("My Notes v.0.1")

        shutdown.triggered.connect(qApp.quit)
        file.triggered.connect(self.response)

    def response(self, action):
        if action.text() == "Open":
            print("Open File...")
        elif action.text() == "Save":
            print("Save File...")
        elif action.text() == "Exit":
            print("Exit Program...")


app = QApplication(sys.argv)
window = TextEditorMenu()
window.show()
sys.exit(app.exec_())