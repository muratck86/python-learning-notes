import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QLabel, \
    QPushButton, QVBoxLayout


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.text_area = QTextEdit()
        self.clear = QPushButton("Clear")

        v_box = QVBoxLayout()

        v_box.addWidget(self.text_area)
        v_box.addWidget(self.clear)

        self.setWindowTitle("Text editing area")

        self.setLayout(v_box)
        self.clear.clicked.connect(self.click)
        self.show()

    def click(self):
        self.text_area.clear()


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())