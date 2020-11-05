import sys, sqlite3
from PyQt5 import QtWidgets


class UserLogin(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.connect_db()
        self.init_ui()

    def connect_db(self):
        connection = sqlite3.connect("database.db")

        self.cursor = connection.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS users "+
                            "(user_name TEXT, password TEXT)")
        connection.commit()

    def init_ui(self):
        self.user_name = QtWidgets.QLineEdit()
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login = QtWidgets.QPushButton("Login")
        self.text_area = QtWidgets.QLabel("")

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.user_name)
        v_box.addWidget(self.password)
        v_box.addWidget(self.text_area)
        v_box.addStretch()

        v_box.addWidget(self.login)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.setWindowTitle("User Login")
        self.login.clicked.connect(self.sign_in)
        self.show()

    def sign_in(self):
        username = self.user_name.text()
        password = self.password.text()

        query = (f"SELECT * FROM users " +
                            f"WHERE user_name = '{username}'" +
                            f" AND password = '{password}'")

        # Alternative query syntax
        query2 = "SELECT * FROM users WHERE user_name = ? AND password = ?"
        self.cursor.execute(query2, (username, password))
        # self.cursor.execute(query)
        data = self.cursor.fetchall()

        if len(data) > 0:
            self.text_area.setText("Welcome "+username)
        else:
            self.text_area.setText("Invalid username or password\n"+
                                   "Please try again...")


app = QtWidgets.QApplication(sys.argv)

login = UserLogin()

exit(app.exec_())