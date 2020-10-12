import random, os, sys, time

color_Yel = '\x1b[1;33;40m'
color_Ora = '\x1b[0;33;40m'
color_Lim = '\x1b[0;32;40m'
color_Gre = '\x1b[1;32;40m'
color_Red = '\x1b[0;31;40m'
color_Blu = '\x1b[0;34;40m'
color_Whi = '\x1b[1;37;40m'
color_Pur = '\x1b[1;35;40m'
color_End = '\x1b[0m'

blink_Sta = '\033[5m'
blink_End = '\033[0m'

class Cell():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.bombed    = False
		self.near_bomb = 0
		self.state     = "#"
		self.checked   = False
		self.marked    = False

	def bomb(self):
		self.bombed    = True

	def check(self, mark = "False"):
		if mark == "mark":
			if self.marked:
				self.marked = False
				self.state  = "#"
			else:
				self.marked = True
				self.state  = f"{color_Red}?{color_End}"
			return True
		elif mark == "False":
			if self.bombed:
				self.state  = f"{color_Red}X{color_End}"
				return False
			else:
				self.checked   = True
				adj_cells      =[(self.y-1, self.x-1), (self.y-1, self.x), (self.y-1, self.x+1),
							     (self.y  , self.x-1),                     (self.y  , self.x+1),
							     (self.y+1, self.x-1), (self.y+1, self.x), (self.y+1, self.x+1)]
				self.near_bomb = 0
				
				# Counting near bombs
				for cos in adj_cells:
					if 0 <= cos[1] < width and 0 <= cos[0] < height and grid[cos[0]][cos[1]].bombed == True:
						self.near_bomb += 1
	
				# Showing near bombs
				if self.near_bomb == 0:
					self.state    = f"{color_Gre}0{color_End}"
					# Reveal adjacents cells when selected a 0 cell
					for cos in adj_cells:
						if 0 <= cos[1] < width and 0 <= cos[0] < height and grid[cos[0]][cos[1]].checked == False:
							grid[cos[0]][cos[1]].check()
				elif self.near_bomb == 1:
					self.state = f"{color_Yel}{self.near_bomb}{color_End}"
				elif 2 <= self.near_bomb <= 3:
					self.state = f"{color_Ora}{self.near_bomb}{color_End}"
				elif 3 < self.near_bomb:
					self.state = f"{color_Pur}{self.near_bomb}{color_End}"
				return True

def create_grid(opt):
	global width, height

	# Selecting difficulty
	if   int(opt[1]) == 1:
		width,height,bomb_number = 5 , 5 , 5
	elif int(opt[1]) == 2:
		width,height,bomb_number = 7 , 7 , 10
	elif int(opt[1]) == 3:
		width,height,bomb_number = 10, 10, 15

	# Adding cells
	for y in range(height):
		grid.append([Cell(x, y) for x in range(width)])

	# Adding bombs
	for i in range(bomb_number):
		random.choice(random.choice(grid)).bomb()
	# solve()
	play()

def show_grid(finish=False):
	global width, height

	# Showing frame
	print(f"{color_Blu}╔{'═'*(2 * width + 5)}╗{color_End}")
	print(f"{color_Blu}║{color_End}{' ' * (width - 3)}{color_Lim}Minesweeper{color_End}{' '* (width - 3)}{color_Blu}║{color_End}")
	print(f"{color_Blu}╠{'═'*(2 * width + 5)}╣{color_End}")

	# Showing columns number
	print(f"{color_Blu}║   {''.join([f'{x} ' for x in range(width)])}  ║{color_End}")
	# Showing rows
	for y in range(height):
		print(f"{color_Blu}║ {y}{color_End} {''.join([f'{cell.state} ' for cell in grid[y]])}{color_Blu}{y} ║{color_End}")
	# Showing columns number
	print(f"{color_Blu}║   {''.join([f'{x} ' for x in range(width)])}  ║{color_End}")

	# Finishing frame
	if finish:
		print(f"{color_Blu}╠{'═'*(2 * width + 5)}╣{color_End}")
	else:
		print(f"{color_Blu}╚{'═'*(2 * width + 5)}╝{color_End}")

def play():
	to = time.time()
	playing, win = True, False
	os.system('clear')
	help()
	show_grid()
	while playing:
		choice = input(f"Enter a couple 'x,y'\n>>> {color_Whi}").split(",")
		print(color_End)
		try:
			if 0 <= int(choice[0]) < width and 0 <= int(choice[1]) < height:
				try:
					playing = grid[int(choice[1])][int(choice[0])].check(choice[2])
				except IndexError:
					playing = grid[int(choice[1])][int(choice[0])].check()
			else:
				print("Choose a valid cell.")
				time.sleep(2.5)
		except ValueError:
			if choice[0] == "check":
				playing, win = finalcheck()
				print("You didn't finish.")
			elif choice[0] == "help":
				help()
			elif choice[0] == "labiteadudul":
				solve()
		os.system('clear')
		show_grid()
	os.system('clear')
	solve(True)
	total_time = (int(10*(time.time() - to)))/10
	if win:
		print(f"{color_Blu}║{color_End}{' ' * (width - 2)}{blink_Sta}You Won !{blink_End}{' ' * (width - 2)}{color_Blu}║{color_End}")
	else:
		print(f"{color_Blu}║{color_End}{' ' * (width - 2)}{blink_Sta}Game Over{blink_End}{' ' * (width - 2)}{color_Blu}║{color_End}")
	print(f"{color_Blu}║{color_End} Time: {' '*((2 * width - 4)-len(str(total_time)))}{blink_Sta}{total_time}{blink_End}s {color_Blu}║{color_End}")
	print(f"{color_Blu}╚{'═'*(2 * width + 5)}╝{color_End}")


def finalcheck():
	global width, height
	breaked = False
	for x in range(width):
		for y in range(height):
			if grid[y][x].state == "#" and grid[y][x].bombed == False:
				breaked = True
				break
		if breaked:
			break
	if breaked:
		return True, False
	else:
		return False, True

def help():
	os.system('clear')
	print(
f"""╔{"═"*96}╗
║  Help:{" "*89}║
║ - To check a cell, enter the x and the y of the cell (for example "{color_Whi}1,2{color_End}" will check{" "*13}║
║ the cell on the second row and third column){" "*51}║
║ - To mark a cell, enter the x and the y of the cell followed by ",mark" (for example "{color_Whi}1,2,mark{color_End}"║
║ will put a "?" at the place of the cell){" "*55}║
║ - To show this help page, just enter "{color_Whi}help{color_End}\"{" "*52}║
╚{"═"*96}╝""")
	time.sleep(5)
	os.system('clear')

def solve(finish=False):
	global width, height
	for x in range(width):
		for y in range(height):
			grid[x][y].check()
	show_grid(finish)

if len(sys.argv)==2:
	grid = []
	create_grid(sys.argv)
else:
	print("Usage : python3 mine.py [difficulty : 1-3]")