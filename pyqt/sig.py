import sys
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.init()
	def init(self):
		self.b=QtWidgets.QPushButton('Push Me')
		self.l=QtWidgets.QLabel('iiii')
		hb=QtWidgets.QHBoxLayout()
		hb.addStretch()
		hb.addWidget(self.l)
		hb.addStretch()
		
		vb=QtWidgets.QVBoxLayout()
		vb.addWidget(self.b)
		vb.addLayout(hb)
		self.setLayout(vb)
		self.show()
		print("ok")
		self.b.clicked.connect(self.xx)
	def xx(self):
		print("hello")
app=QtWidgets.QApplication(sys.argv)
w=Window()
sys.exit(app.exec_())

