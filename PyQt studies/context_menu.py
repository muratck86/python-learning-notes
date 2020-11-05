"""
This example shows how to create a context menu (right click menu)
"""

import sys
from PyQt5.QtWidgets import QAction, QApplication, QMenu, QMainWindow


class ContextExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("Context Menu Example")
        self.show()

    #     Reimplementation of the method
    def contextMenuEvent(self, event):
        context_menu = QMenu(self)

        new_act = context_menu.addAction("New")
        open_act = context_menu.addAction("Open")
        clear_act = context_menu.addAction("Clear")
        quit_act = context_menu.addAction("Quit")

        # exec_() method displays the context menu
        # To get the mouse pointer coordinates pos() method is used
        # mapToGlobal() method translates the widget coordinates to the screen coordinates
        action = context_menu.exec_(self.mapToGlobal(event.pos()))

        if action == quit_act:
            self.close()


def main():
    app = QApplication(sys.argv)
    ex = ContextExample()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
