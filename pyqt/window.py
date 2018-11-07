import sys
from PyQt5 import QtWidgets

def window():
	app=QtWidgets.QApplication(sys.argv)
	w=QtWidgets.QWidget()
	l=QtWidgets.QLabel(w)
	l.setText("hello world")
	w.setWindowTitle('PyQt5')
	l.move(50,0)
	w.show()
	w.setGeometry(10,200,300,300)
	sys.exit(app.exec_())

window()
