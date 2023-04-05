# Refer https://www.cleanpng.com/free/ishihara-test.html
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from PyQt5.QtGui import QFont
from PyQt5 import QtGui

from setdata_class import SetData_class


class Screen_2(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget

        self.setData = SetData_class()

        self.background = QLabel(self)
        pixmap = QtGui.QPixmap("images/background.png")
        pixmap = pixmap.scaled(1280, 720)
        self.background.setPixmap(pixmap)
        self.background.setGeometry(0, 0, 1280, 720)
        self.setFixedSize(1280, 720)

        font = QFont()
        font.setFamily("Tahoma")
        font.setPointSize(44)

        self.btn1 = QPushButton('Text Button', self)
        self.btn1.setGeometry(420, 300, 401, 100)
        self.btn1.setStyleSheet('background-color: #DF2041')
        self.btn1.setFont(font)


#----------------- Function ----------------

    def checkDoingTest1(self):
        getExT1 = self.setData.get_ExamPages()
        if getExT1 == True:
            print("True screen 2")
        elif getExT1 == False:
            print("False screen 2")
        else:
            print("None screen 2")