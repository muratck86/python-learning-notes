import sys
from PyQt5.QtWidgets import QWidget, QApplication, \
    QCheckBox, QLabel, QPushButton, QVBoxLayout


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.checkBox = QCheckBox("Search only in not seen movies")
        self.text_area = QLabel("")
        self.button = QPushButton("Search")


        v_box = QVBoxLayout()

        v_box.addWidget(self.checkBox)
        v_box.addWidget(self.text_area)
        v_box.addWidget(self.button)

        self.setLayout(v_box)

        self.setWindowTitle("My Movies Library")

        self.button.clicked.connect(lambda: self.click(self.checkBox.isChecked(),
                                                       self.text_area))
        self.show()

    def click(self, checked, text_area):
        if checked:
            text_area.setText("Searching in not seen movies...")
        else:
            text_area.setText("Searching in all movies")


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
