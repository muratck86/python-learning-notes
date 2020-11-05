import sys
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication, QMainWindow


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.statusBar().showMessage("Ready")
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Status bar')
        self.show()

    def closeEvent(self, event):

        # reply = QMessageBox.question(self, 'Message',
        #                              "Are you sure to quit?", QMessageBox.Yes |
        #                              QMessageBox.No, QMessageBox.No | QMessageBox.Cancel,)
        reply = QMessageBox.question(self, 'Warning!', 'Are you sure?', QMessageBox.Yes | QMessageBox.No |
                                     QMessageBox.Cancel, QMessageBox.Cancel)
        # QCloseEvent.
        if reply == QMessageBox.Yes:

            event.accept()
        elif reply == QMessageBox.No:

            event.accept()
        else:
            event.ignore()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()