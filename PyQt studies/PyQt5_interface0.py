import sys
from PyQt5 import QtWidgets,QtGui


def window():
    app = QtWidgets.QApplication(sys.argv) #The main application
    window = QtWidgets.QWidget() #The window for my application
    window.setWindowTitle("My Movie Library V.0.1") #Set window title
    window.setGeometry(250,200,800,500) #position x,y and sizes width and height
    button = QtWidgets.QPushButton(window)
    button.setText("Search")
    button.move(10,60)
    label1 = QtWidgets.QLabel(window) # create a label (which occures in the window) and put it into
    label2 = QtWidgets.QLabel(window) # a label will contain a png or jpg file
    # the window.
    pixel = QtGui.QPixmap("search.png")
    pixel.setDevicePixelRatio(1.1) #scale the image
    label2.setPixmap(pixel)

    label1.setText("Welcome to My Movie Library, you can organize your movie library here...")
    label1.move(30,30) #Position of label1 in the window
    label2.move(100,50)
    window.show()
    sys.exit(app.exec_())
window()