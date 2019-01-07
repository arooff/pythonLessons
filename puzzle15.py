from PyQt5.QtWidgets import QApplication, QPushButton, QGridLayout, QGroupBox, QVBoxLayout, QButtonGroup, QWidget, QAction, QMainWindow, QMessageBox
import sys, random
from PyQt5 import QtGui, QtCore

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.stepen=[
            [1,4], [0,2,5], [1,3,6], [2,7],
            [0,5,8], [1,4,6,9], [2,5,7,10], [3,6,11],
            [4,9,12], [5,8,10,13], [6,9,11,14], [7,10,15],
            [8,13], [9,12,14], [10,13,15], [11,14]
            ]
        self.workingList=[]
        self.__emptyButtonId=0
        self.numberOfClicks=0

        self.listSize = 16
        self.title = "Puzzle"
        self.top = 200
        self.left = 400
        self.width = 320
        self.height = 320
        self.iconName = '15.png'

        self.fillList(self.listSize)
        self.InitWindow()


    def setEmptyButtonId(self, id):
        self.__emptyButtonId = id

    def getEmptyButtonId(self):
        return self.__emptyButtonId

    def fillList(self, size):
        self.workingList = list(range(size))
        random.shuffle(self.workingList)
        for i in self.workingList:
            if self.workingList[i] == 0:
                self.setEmptyButtonId(i)

    def InitWindow(self):


        self.CreateLayout()
        self.setCentralWidget(self.groupBox)

        menubar = self.menuBar()
        gameMenu = menubar.addMenu('&Game')
        aboutGame = menubar.addMenu('&About')

        newGameAction = QAction('New game', self)
        newGameAction.setShortcut('Ctrl+N')
        newGameAction.triggered.connect(self.newGame)

        leaderList = QAction('Leader List', self)
        leaderList.setShortcut('Ctrl+L')
        leaderList.triggered.connect(self.leaderList)

        exitGame = QAction('Exit', self)
        exitGame.setShortcut('Ctrl+Q')
        exitGame.triggered.connect(self.close)

        gameMenu.addAction(newGameAction)
        gameMenu.addAction(leaderList)
        gameMenu.addAction(exitGame)

        aboutGameAction = QAction('About', self)
        aboutGameAction.setShortcut('Ctrl+O')
        aboutGameAction.triggered.connect(self.about)

        aboutGame.addAction(aboutGameAction)
        #vbox = QVBoxLayout()
        #vbox.addWidget(self.groupBox)

        #self.setLayout(vbox)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(320,320)

        self.show()

    def newGame(self):
        pass
    def leaderList(self):
        pass
    def about(self):
        QMessageBox.question(self, 'Version Info', "Puzzle Game v.1.0.", QMessageBox.Yes)

    def CreateLayout(self):
        self.buttongroup = QButtonGroup()
        self.buttongroup.buttonClicked[int].connect(self.on_button_clicked)
        #self.groupBox = QGroupBox("  That's your field!")
        self.groupBox = QGroupBox()
        gridLayout = QGridLayout()
        row=0
        column=0
        groupElement=0
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
                button = QPushButton(str(i)  if i != 0 else "", self)
                button.setIconSize(QtCore.QSize(40, 40))
                button.setMinimumHeight(60)
                gridLayout.addWidget(button, row, column)
                column = column + 1
            self.buttongroup.addButton(button, groupElement)
            groupElement = groupElement +1

        self.groupBox.setLayout(gridLayout)

    def on_button_clicked(self, id):
        self.numberOfClicks += 1
        if self.ifMovePossible(id,self.stepen):
            digit=self.buttongroup.button(id).text()
            self.buttongroup.button(id).setText("")
            self.workingList[id] = 0
            self.buttongroup.button(self.getEmptyButtonId()).setText(str(digit))
            self.workingList[self.getEmptyButtonId()] = digit
            self.setEmptyButtonId(id)

    def checkResult(self):
        #self.workingList=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
        result = True
        for i in range(1,self.listSize):
            if i != self.workingList[i-1]:
                result = False
        return result

    def ifMovePossible(self, pressedButtonIndex, stepen):
        res = False
        if pressedButtonIndex == self.getEmptyButtonId(): return res
        for i in stepen[pressedButtonIndex]:
            if i == self.getEmptyButtonId():
                res = True
                break
        return res

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
#    print(window.getEmptyButtonId())
    sys.exit(app.exec())
