# 5*5   84px
# 7*7   60px
# 10*10 42px
0
42
84
126
168
210
252
294
336
378
420

# 15*15 28px
from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
	def __init__(self):
		super(Ui, self).__init__()
		uic.loadUi('minesweeper.ui', self)
		self.show()

	def Show_Grid(self, size):
		if size == 5:
			self.Frame7_7.hide()
		elif size == 7:
			self.Frame5_5.hide()
			self.Frame10_10.hide()



app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.Show_Grid(7)
app.exec_()