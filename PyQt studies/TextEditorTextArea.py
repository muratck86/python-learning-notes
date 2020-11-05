import sys
import os
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QApplication, \
    QTextEdit, QLabel, QPushButton, QVBoxLayout, QFileDialog


class TextEditorTextArea(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.text_area = QTextEdit()
        self.clear = QPushButton("Clear")
        self.open = QPushButton("Open")
        self.save_as = QPushButton("Save As")
        self.save = QPushButton("Save")

        h_box = QHBoxLayout()
        h_box.addWidget(self.clear)
        h_box.addWidget(self.open)
        h_box.addWidget(self.save_as)
        h_box.addWidget(self.save)

        v_box = QVBoxLayout()
        v_box.addWidget(self.text_area)

        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.setWindowTitle("MyNotes v.0.1")

        self.clear.clicked.connect(self.text_area.clear)
        self.open.clicked.connect(self.open_file)
        self.save_as.clicked.connect(self.save_as_file)
        self.save.clicked.connect(self.save_file)


    def open_file(self):
        file_name = QFileDialog.getOpenFileName(self, "Open File",
                                                os.getenv("HOME"))
        with open(file_name[0],"r") as file:
            self.text_area.setText(file.read())

    def save_as_file(self):
        file_name = QFileDialog.getSaveFileName(self, "Save File As..")
        with open(file_name[0],"w") as file:
            file.write(self.text_area.toPlainText())

    def save_file(self):
        pass


# app = QApplication(sys.argv)
# notes = TextEditorTextArea()
# notes.show()
# sys.exit(app.exec_())
