import sys
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.textArea = QtWidgets.QLabel("No clicks yet...")
        self.button = QtWidgets.QPushButton("Click Here")
        self.count = 0

        vBox1 = QtWidgets.QVBoxLayout()

        vBox1.addWidget(self.button)
        vBox1.addWidget(self.textArea)
        vBox1.addStretch()

        hBox1 = QtWidgets.QHBoxLayout()

        hBox1.addStretch()
        hBox1.addLayout(vBox1)
        hBox1.addStretch()

        self.setLayout(hBox1)

        self.button.clicked.connect(self.increaseCount)

        self.show()

    def increaseCount(self):
        self.count += 1
        self.textArea.setText(f"Clicked {self.count} times")


application = QtWidgets.QApplication(sys.argv)
window1 = Window()
sys.exit(application.exec_())