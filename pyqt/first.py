from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
import sys
class firstW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title="first window"
        self.top=100
        self.left=100
        self.width=600
        self.height=500
        self.setWindowIcon(QtGui.QIcon("1.jpg"))
        b=QPushButton("click",self)
        b.move(200,0)
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.show()



App=QApplication(sys.argv)
w=firstW()
sys.exit(App.exec())        
