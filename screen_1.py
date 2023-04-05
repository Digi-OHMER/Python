from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QCheckBox
from PyQt5.QtGui import QFont
from PyQt5 import QtGui

from setdata_class import SetData_class
from screen_2 import Screen_2



class Screen_1(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget

        self.setData = SetData_class()
        self.scene2 = Screen_2(self.stacked_widget)
        self.statusExam1 = False
        
        self.background = QLabel(self)
        pixmap = QtGui.QPixmap("images/bg_3_2.png")
        pixmap = pixmap.scaled(1280, 720)
        self.background.setPixmap(pixmap)
        self.background.setGeometry(0, 0, 1280, 720)
        self.setFixedSize(1280, 720)
        
        font = QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)

        self.btn1_next = QPushButton('ถัดไป', self)
        self.btn1_next.setGeometry(875, 620, 190, 50)
        self.btn1_next.setFont(font)

        self.box1 = QCheckBox('', self)
        self.box1.setChecked(False)
        self.box1.setGeometry(863, 258, 190, 50)

        # สั่งใช้งานปุ่ม
        self.box1.clicked.connect(self.checkBoxClicker1)
        self.btn1_next.clicked.connect(lambda: self.btn_clickNext())
        

    def checkBoxClicker1(self):
        if self.box1.isChecked():
            self.statusExam1 = True
        else:
            self.statusExam1 = False


    def btn_clickNext(self):
        self.setData.set_ExamPages(self.statusExam1)    #ส่ง
        self.resetValue()
        # self.stacked_widget.setCurrentIndex(1)
        d1 = self.setData.get_ExamPages()
        if(d1 == True):
            print("Screen 1 get True")

        self.scene2.checkDoingTest1()

    def resetValue(self):
        self.box1.setChecked(False)
        self.statusExam1 = False
