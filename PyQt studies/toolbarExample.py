"""
This example shows how to create toolbars in applications
"""

import sys
from PyQt5.QtWidgets import QAction, QMainWindow, QApplication, qApp, QTextEdit, QWidget
from PyQt5.QtGui import QIcon


class ToolbarExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        textEdit = QWidget()
        self.setCentralWidget(textEdit)

        self.statusBar().showMessage("Ready")

        exit_action =QAction(QIcon("exit.png"), "Exit", self)
        exit_action.setShortcut("Ctrl+q")
        exit_action.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar("Main Tools")
        self.toolbar.addAction(exit_action)

        self.setWindowTitle("Toolbar Exapmle")

        self.show()


def main():
    app = QApplication(sys.argv)
    ex = ToolbarExample()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()