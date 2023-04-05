import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from screen_1 import Screen_1
from screen_2 import Screen_2

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget()
        
        self.scene1 = Screen_1(self.stacked_widget)
        self.scene2 = Screen_2(self.stacked_widget)

        # เพิ่ม screen ที่จะใช้งาน
        self.stacked_widget.addWidget(self.scene1)
        self.stacked_widget.addWidget(self.scene2)

        self.setCentralWidget(self.stacked_widget)
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    sys.exit(app.exec_())
