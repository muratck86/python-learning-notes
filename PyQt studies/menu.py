"""
This simple example shows how to create a menu bar and sub menus and actions in it...
Also there is a checkable menu action example too
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QMenu
from PyQt5.QtGui import QIcon


class MenuExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # The & sign before the x letter enables the using menus and actions with alt+x for exit or
        # alt+F for file and so on..
        # The QIcon object which has search.png will show the icon left next to Exit action in the menu
        exit_action = QAction(QIcon("search.png"), "E&xit", self)
        exit_action.setShortcut("Ctrl+q")
        # when we hover mouse pointer over the exit action, the tip below will appear in the status bar.
        exit_action.setStatusTip("Exit program")
        exit_action.triggered.connect(qApp.quit)

        # to enable status bar...
        self.statusBar = self.statusBar()
        self.statusBar.showMessage("Ready")

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")

        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)

        file_menu.addAction(viewStatAct)

        imp_action_xls = QAction("From xlsx", self)
        imp_action_xls.setStatusTip("Import an MS Excel spreadsheet")
        imp_action_docx = QAction("From docx", self)
        imp_action_docx.setStatusTip("Import an MS Word document")

        imp_menu = QMenu("Import", self)
        imp_menu.addAction(imp_action_xls)
        imp_menu.addAction(imp_action_docx)

        file_menu.addAction(exit_action)

        # menu_bar.addMenu(imp_menu)
        file_menu.addMenu(imp_menu)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("Simple Menu Bar")

        self.show()

    def toggleMenu(self, state):
        if state:
            self.statusBar.show()
        else:
            self.statusBar.hide()


def main():
    app = QApplication(sys.argv)
    ex = MenuExample()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
