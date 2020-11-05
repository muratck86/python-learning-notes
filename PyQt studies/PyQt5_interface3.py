import sys
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.text_area = QtWidgets.QLineEdit()
        self.clear = QtWidgets.QPushButton("Clear")
        self.write = QtWidgets.QPushButton("Print")
        self.print_area = QtWidgets.QLabel("")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.text_area)

        def write_action():
            new_line = QtWidgets.QLabel("")
            v_box.addWidget(new_line)
            new_line.setText(self.text_area.text())

        v_box.addWidget(self.clear)
        v_box.addWidget(self.write)
        v_box.addWidget(self.print_area)

        self.setLayout(v_box)

        self.clear.clicked.connect(self.click_action)
        v_box.addStretch()
        self.write.clicked.connect(write_action)

        self.show()

    def click_action(self):
        self.text_area.clear()


app = QtWidgets.QApplication(sys.argv)
window1 = Window()
sys.exit(app.exec_())
