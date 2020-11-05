import sys
from PyQt5.QtWidgets import QWidget, QApplication, QRadioButton, \
    QLabel, QPushButton, QVBoxLayout


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.radio_text = QLabel("Pick one of the options below:")
        self.op1 = QRadioButton("Option 1")
        self.op2 = QRadioButton("Option 2")
        self.op3 = QRadioButton("Option 3")

        self.text_area = QLabel("")

        self.button = QPushButton("Submit")

        v_box = QVBoxLayout()

        v_box.addWidget(self.radio_text)
        v_box.addWidget(self.op1)
        v_box.addWidget(self.op2)
        v_box.addWidget(self.op3)
        v_box.addStretch()
        v_box.addWidget(self.text_area)
        v_box.addWidget(self.button)

        self.setLayout(v_box)

        self.button.clicked.connect(lambda:
                                    self.click(self.op1.isChecked(),
                                               self.op2.isChecked(),
                                               self.op3.isChecked(),
                                               self.text_area))

        self.setWindowTitle("Choose Options")

        self.show()

    def click(self, op1, op2, op3, text_area):
        if op1:
            text_area.setText("Option 1 selected.")
        if op2:
            text_area.setText("Option 2 selected.")
        if op3:
            text_area.setText("Option 3 selected.")


app = QApplication(sys.argv)
window = Window()

sys.exit(app.exec_())
