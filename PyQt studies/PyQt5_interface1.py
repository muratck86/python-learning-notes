import sys
from PyQt5 import QtWidgets


def window():
    app = QtWidgets.QApplication(sys.argv)
    okButton = QtWidgets.QPushButton("Okay") #Define buttons
    cancelButton = QtWidgets.QPushButton("Cancel")
    backButton = QtWidgets.QPushButton("<<Back")
    forwardButton = QtWidgets.QPushButton("Forward>>")

    hBox1 = QtWidgets.QHBoxLayout() #create a horizontal layout.
    #hBox1.addStretch() #add a strechable space between border and widgets
    hBox1.addWidget(backButton)
    #hBox1.addStretch() #add a strechable space between widgets
    hBox1.addWidget(forwardButton)
    hBox1.addStretch() #add a strechable space between widgets and border

    hBox2 = QtWidgets.QHBoxLayout() #create another horizontal layout

    hBox2.addStretch()
    hBox2.addWidget(okButton)
    hBox2.addWidget(cancelButton)
    #vBox.addStretch()

    vBox1 = QtWidgets.QVBoxLayout() #create a vertical layout
    vBox1.addLayout(hBox1)
    vBox1.addStretch()
    vBox1.addLayout(hBox2)


    window = QtWidgets.QWidget()
    window.setWindowTitle("My Movie Library V.0.2")

    window.setGeometry(250,200,800,500)
    #window.setLayout(hBox1)
    window.setLayout(vBox1)
    window.show()

    sys.exit(app.exec_())

window()