import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication, QPushButton, QGridLayout, QGroupBox, QButtonGroup
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui, QtCore


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.workingList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
        self.initUI()


    def initUI(self):

        self.buttongroup = QButtonGroup()
        #self.buttongroup.buttonClicked[int].connect(self.on_button_clicked)
        self.groupBox = QGroupBox("  That's your field!")
        #self.groupBox = QGroupBox()
        gridLayout = QGridLayout()
        row = 0
        column = 0
        groupElement = 0
        for i in self.workingList:
            if column < 4:
                button = QPushButton(str(i) if i != 0 else "", self)
                button.setIconSize(QtCore.QSize(40, 40))
                button.setMinimumHeight(60)
                gridLayout.addWidget(button, row, column)
                column = column + 1
            else:
                row = row + 1
                column = 0
                button = QPushButton(str(i) if i != 0 else "", self)
                button.setIconSize(QtCore.QSize(40, 40))
                button.setMinimumHeight(60)
                gridLayout.addWidget(button, row, column)
                column = column + 1
            self.buttongroup.addButton(button, groupElement)
            groupElement = groupElement + 1

        self.groupBox.setLayout(gridLayout)

        self.setCentralWidget(self.groupBox)

        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())