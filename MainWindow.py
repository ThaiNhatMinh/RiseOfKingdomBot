import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWindow():
    WIDHT = 400
    HEIGHT = 600

    def __init__(self):
        QCoreApplication.setApplicationName("Rise Of Kingdome Bot")
        self.window()

    def window(self):
        self.app = QApplication(sys.argv)
        self.root = QWidget()
        self.root.setGeometry(100, 100, self.WIDHT, self.HEIGHT)
        self.root.setFixedSize(self.WIDHT, self.HEIGHT)
        self.root.show()

        b = QLabel(self.root)
        b.setText("Hello World!")
        b.move(50,20)
        self.app.exec_()

    def root(self) -> QWidget:
        return self.root