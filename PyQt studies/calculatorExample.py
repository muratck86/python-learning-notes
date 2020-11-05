"""
Explanation
"""

import sys
from functools import partial
from PyQt5.QtWidgets import QWidget, QAction, QMainWindow, QApplication, QPushButton, QMenu, qApp, QGridLayout, \
    QMessageBox, QRadioButton, QCheckBox, QTextEdit, QHBoxLayout, QVBoxLayout, QLabel


class CalculatorExample(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.edit_area = QTextEdit()
        self.edit_area_token = self.edit_area
        self.history = QLabel("No History")
        v_history_area = QVBoxLayout()
        v_history_area.addWidget(self.history)
        v_history_area.addStretch()

        h_edit_and_func = QHBoxLayout()
        h_edit_and_func.addWidget(self.edit_area)
        h_edit_and_func.addLayout(v_history_area)
        h_edit_and_func.addStretch(1)

        v_main_layout = QVBoxLayout()
        v_main_layout.addLayout(h_edit_and_func)
        v_main_layout.addStretch(1)

        buttons = ['Clear', '<--', '(', ')', 'π', 'Close',
                   'sin', 'cos', 'tan', 'cot', 'deg->rad', 'rad->deg',
                   '7', '8', '9', '/', '%', 'e',
                   '4', '5', '6', '*', 'x²', 'x³',
                   '1', '2', '3', '-', 'sqrt', 'log',
                   '.', '0', '=', '+', 'x!', 'ln']

        g_grid_layout = QGridLayout()
        positions = [(i, j) for i in range(6) for j in range(6)]
        for position, button in zip(positions, buttons):
            push_button = QPushButton(button)
            g_grid_layout.addWidget(push_button, *position)
            push_button.clicked.connect(partial(self.button_action, push_button))

        v_main_layout.addLayout(g_grid_layout)
        self.setLayout(v_main_layout)

    def button_action(self, action):
        if action.text() == "Clear":
            print("Clear button pressed")
            self.edit_area.clear()
        elif action.text() == "<--":
            print("BackSpace button pressed")
            if len(self.edit_area_token.toPlainText()) > 0:
                self.edit_area.setText(self.edit_area.toPlainText()[:-1])
        elif action.text() == '(':
            self.edit_area_token.setText(self.edit_area_token.toPlainText() + '(')
            print("( button pressed")
        elif action.text() == ')':
            self.edit_area_token.setText(self.edit_area_token.toPlainText() + ')')
            print(") button pressed")
        elif action.text() == 'π':
            self.edit_area_token.setText(self.edit_area_token.toPlainText() + 'π')
            print("π button pressed")
        elif action.text() == 'Close':
            print("Close button pressed")
            qApp.quit()
        elif action.text() == 'sin':
            self.edit_area_token.setText(self.edit_area_token.toPlainText() + 'sin(')
            print("sin button pressed")
        elif action.text() == 'cos':
            self.edit_area_token.setText(self.edit_area_token.toPlainText() + 'cos(')
            print("cos button pressed")
        elif action.text() == 'tan':
            self.edit_area_token.setText(self.edit_area_token.toPlainText() + 'tan(')
            print("tan button pressed")
        elif action.text() == 'cot':
            self.edit_area_token.setText(self.edit_area_token.toPlainText() + 'cot(')
            print("cot button pressed")
        elif action.text() == 'deg->rad':
            self.edit_area_token.setText(self.edit_area_token.toPlainText() + 'rad(')
            print("degree to radian button pressed")
        elif action.text() == 'rad->deg':
            self.edit_area_token.setText(self.edit_area_token.toPlainText() + 'deg(')
            print("radian to degree button pressed")
        elif action.text() == '7':
            self.edit_area_token.setText(self.edit_area_token.toPlainText() + '7')
            print("7 button pressed")
        elif action.text() == '8':
            self.edit_area_token.setText(self.edit_area_token.toPlainText() + '8')
            print("8 button pressed")
        elif action.text() == '9':
            self.edit_area_token.setText(self.edit_area_token.toPlainText() + '9')
            print("9 button pressed")
        elif action.text() == '/':
            self.edit_area_token.setText(self.edit_area_token.toPlainText() + '/')
            print("/ button pressed")
        elif action.text() == '%':
            self.edit_area_token.setText(self.edit_area_token.toPlainText() + '%')
            print("% button pressed")
        elif action.text() == 'e':
            self.edit_area_token.setText(self.edit_area_token.toPlainText() + 'e')
            print("e button pressed")
        elif action.text() == '4':
            self.edit_area_token.setText(self.edit_area_token.toPlainText() + '4')
            print("4 button pressed")
        elif action.text() == '5':
            self.edit_area_token.setText(self.edit_area_token.toPlainText() + '5')
            print("5 button pressed")
        elif action.text() == '6':
            self.edit_area_token.setText(self.edit_area_token.toPlainText() + '6')
            print("6 button pressed")
        elif action.text() == '*':
            self.edit_area_token.setText(self.edit_area_token.toPlainText() + '*')
            print("* button pressed")
        elif action.text() == 'x²':
            self.edit_area_token.setText(self.edit_area_token.toPlainText() + '²')
            print("x² button pressed")
        elif action.text() == 'x³':
            self.edit_area_token.setText(self.edit_area_token.toPlainText() + '³')
            print("x³ button pressed")
        elif action.text() == '1':
            self.edit_area_token.setText(self.edit_area_token.toPlainText() + '1')
            print("1 button pressed")
        elif action.text() == '2':
            self.edit_area_token.setText(self.edit_area_token.toPlainText() + '2')
            print("2 button pressed")
        elif action.text() == '3':
            self.edit_area_token.setText(self.edit_area_token.toPlainText() + '3')
            print("3 button pressed")
        elif action.text() == '-':
            self.edit_area_token.setText(self.edit_area_token.toPlainText() + '-')
            print("- button pressed")
        elif action.text() == 'sqrt':
            self.edit_area_token.setText(self.edit_area_token.toPlainText() + 'sqrt(')
            print("sqrt button pressed")
        elif action.text() == 'log':
            self.edit_area_token.setText(self.edit_area_token.toPlainText() + 'log(')
            print("log button pressed")
        elif action.text() == '.':
            self.edit_area_token.setText(self.edit_area_token.toPlainText() + '.')
            print(". button pressed")
        elif action.text() == '0':
            self.edit_area_token.setText(self.edit_area_token.toPlainText() + '0')
            print("0 button pressed")
        elif action.text() == '=':
            if len(self.edit_area.toPlainText()) != 0:
                result = str(self.calculate())
                if self.history.text() == 'No History':
                    self.history.setText(self.edit_area_token.toPlainText() + '\n' + '=' + result + '\n\n')
                else:
                    self.history.setText(self.history.text() + self.edit_area_token.toPlainText() + '\n' +
                                         '=' + result + '\n\n')
            self.edit_area.clear()
            print("= button pressed")
        elif action.text() == '+':
            self.edit_area_token.setText(self.edit_area_token.toPlainText() + '+')
            print("+ button pressed")
        elif action.text() == 'x!':
            self.edit_area_token.setText(self.edit_area_token.toPlainText() + '!')
            print("x! button pressed")
        elif action.text() == 'ln':
            self.edit_area_token.setText(self.edit_area_token.toPlainText() + 'ln(')
            print('ln button pressed')

    def calculate(self):
        return 'to be calculated...'


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.window = CalculatorExample()
        self.setCentralWidget(self.window)
        self.setGeometry(1000, 300, 150, 300)
        self.setWindowTitle("My Calculator V Alpha 1")

        self.show()


def main():
    app = QApplication(sys.argv)
    calculator = Main()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
