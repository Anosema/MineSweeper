from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys, random


class Cell():
	marker = False
	def __init__(self, x, y, Frame):
		self.x = x
		self.y = y
		self.bombed    = False
		self.near_bomb = 0
		self.state     = ""
		self.checked   = False
		self.marked    = False

		self.button = QPushButton('', Frame)
		self.button.resize(Cell.width, Cell.height)
		self.button.clicked.connect(self.check)
		self.button.setFont(QFont('Arial', 25)) 
		self.button.move(int(x*Cell.width), int(y*Cell.height))

	def check(self):
		if Cell.marker:
			if self.marked:
				self.marked = False
				self.state  = ""
			else:
				if self.state == "":
					self.marked = True
					self.state  = "⚑"
		else:
			if self.state == "":
				if self.marked == False:
					if self.bombed:
						self.state  = "💣"
						self.button.setStyleSheet("background-color : #c0392b")
						self.button.setEnabled(False)
						solve()
						NG.GameOver.show()
						NG.show()
					else:
						self.checked   = True
						adj_cells      =[(self.y-1, self.x-1), (self.y-1, self.x), (self.y-1, self.x+1),
									     (self.y  , self.x-1),                     (self.y  , self.x+1),
									     (self.y+1, self.x-1), (self.y+1, self.x), (self.y+1, self.x+1)]
						self.near_bomb = 0
						# Counting near bombs
						for coords in adj_cells:
							if 0 <= coords[1] < width and 0 <= coords[0] < height and grid[coords[0]][coords[1]].bombed:
								self.near_bomb += 1
			
						# Showing near bombs
						if self.near_bomb == 0:
							self.state    = "0"
							# Reveal adjacents cells when selected a 0 cell
							for coords in adj_cells:
								if 0 <= coords[1] < width and 0 <= coords[0] < height and grid[coords[0]][coords[1]].checked == False:
									grid[coords[0]][coords[1]].check()
						elif self.near_bomb == 1:
							self.state = f"{self.near_bomb}"
							self.button.setStyleSheet("color : blue")
						elif 2 <= self.near_bomb < 3:
							self.state = f"{self.near_bomb}"
							self.button.setStyleSheet("color : green")
						elif 3 <= self.near_bomb:
							self.state = f"{self.near_bomb}"
							self.button.setStyleSheet("color : red")
						self.button.setEnabled(False)
		self.button.setText(self.state)
	def bomb(self):
		self.bombed = True

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Minesweeper')
		self.setFixedWidth (500)
		self.setFixedHeight(500)
		self.MarkerButton = QPushButton('⚑' , self)
		self.CheckButton  = QPushButton('😎', self)
		self.Bomb_Canva   = QFrame(self)
		self.MarkerButton.resize(220, 30)
		self.CheckButton .resize(220, 30)
		self.Bomb_Canva  .resize(440, 440)
		self.MarkerButton.move(30 , 470)
		self.CheckButton .move(250, 470)
		self.Bomb_Canva  .move(30 , 30)
		self.MarkerButton.setFont(QFont('Arial', 15)) 
		self.CheckButton .setFont(QFont('Arial', 15))
		self.MarkerButton.setToolTip('Toggle Marker Mode (OFF)')
		self.CheckButton .setToolTip('Check If Grid Clear')


		self.CheckButton .clicked.connect(finalcheck)
		self.MarkerButton.clicked.connect(self.mark_onoff)

	def mark_onoff(self):
		if Cell.marker:
			Cell.marker = False
			self.MarkerButton.setToolTip('Toggle Marker Mode (OFF)')
		else:
			Cell.marker = True
			self.MarkerButton.setToolTip('Toggle Marker Mode (ON)')

class NewGame(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('New Game')
		self.setFixedWidth(350)
		self.setFixedHeight(150)
		self.GameOver     = QLabel("Game Over", self)
		self.LabelExplain = QLabel("Create New Game", self)
		self.GameOver    .resize(300, 25)
		self.LabelExplain.resize(300, 25)
		self.GameOver    .setAlignment(Qt.AlignCenter)
		self.LabelExplain.setAlignment(Qt.AlignCenter)
		self.GameOver    .setFont(QFont('Arial', 17))
		self.LabelExplain.setFont(QFont('Arial', 17))
		self.GameOver    .move(25,25)
		self.LabelExplain.move(25,50)

		self.GameOver.close()

		self.S5  = QPushButton('5x5\n5 Bombs', self)
		self.S7  = QPushButton('7x7\n7 Bombs', self)
		self.S10 = QPushButton('10x10\n15 Bombs', self)
		self.S15 = QPushButton('15x15\n25 Bombs', self)
		self.S5 .resize(75,50)
		self.S7 .resize(75,50)
		self.S10.resize(75,50)
		self.S15.resize(75,50)
		self.S5 .move  (25 , 75)
		self.S7 .move  (100, 75)
		self.S10.move  (175, 75)
		self.S15.move  (250, 75)
		self.S5 .clicked.connect(lambda: new_game(5 , 5 , 5 ))
		self.S7 .clicked.connect(lambda: new_game(7 , 7 , 7 ))
		self.S10.clicked.connect(lambda: new_game(10, 10, 15))
		self.S15.clicked.connect(lambda: new_game(15, 15, 25))

def finalcheck():
	global width, height
	breaked = False
	for x in range(width):
		for y in range(height):
			if grid[y][x].state == "" and grid[y][x].bombed == False:
				breaked = True
				break
		if breaked:
			break
	if not breaked:
		#win
		solve()
		NG.show()

def solve():
	global width, height
	for x in range(width):
		for y in range(height):
			if not grid[x][y].checked:
				grid[x][y].check()

def new_game(w, h, b):
	global width, height, grid, Game
	try:
		Game.close()
		del Game
	except NameError:
		pass
	Game = MainWindow()
	Game.setWindowTitle(f'Minesweeper {w}x{h}')

	width, height, bomb_number = w, h, b
	Cell.height, Cell.width = int(440/height), int(440/width)
	grid = []
	for i in range(0,height):
		grid.append([Cell(j, i, Game.Bomb_Canva) for j in range(0,width)])
	for i in range(bomb_number):
		while 1:
			bomb = random.choice(random.choice(grid))
			if not bomb.bombed:
				bomb.bomb()
				break
	NG.close()
	NG.GameOver.close()
	Game.show()

app = QApplication(sys.argv)

NG = NewGame()
NG.show()
app.exec_()