import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.init()
	def init(self):
		self.s=QtWidgets.QSlider(QSlider.Horizontal)
		self.s.setMinimum(1)
		self.s.setValue(25)
		self.s.setTickInterval(5)
		hb=QHBoxLayout()
		hb.addWidget(self.s)
		self.setLayout(hb)
		
		self.s.valueChanged.connect(self.chh)
		
		self.show()
	def chh():
		print(self.s.value())


app=QApplication(sys.argv)


w=Window()
sys.exit(app.exec_())


