from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QRect
import sys

#button=QPushButton("Click me")

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Window"
        self.top = 200
        self.left = 300
        self.width = 400
        self.height = 300


        self.InitButton()
        self.InitWindow()


    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("15.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def InitButton(self):
        button=QPushButton("Click me", self)
        button.setGeometry(QRect(100, 100, 111, 28))
        button.setToolTip("<h3><i>This Is Click Button<\i><h3>")

        button.clicked.connect(self.ButtonAction)

    def ButtonAction(self):
        if(self.title == "Hello World"):
            print("yes!!!!!!!!!")
        else:
            print("Hello World")



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())