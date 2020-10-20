import random, os, sys, time

embed_end           = '\x1b[0m'
embed_bold          = '\x1b[1m'
embed_underline     = '\x1b[4m'
embed_blink         = '\x1b[5m'
embed_black         = '\x1b[30m'
embed_red           = '\x1b[31m'
embed_green         = '\x1b[32m'
embed_yellow        = '\x1b[33m'
embed_blue          = '\x1b[34m'
embed_magenta       = '\x1b[35m'
embed_cyan          = '\x1b[36m'
embed_white         = '\x1b[37m'
embed_light_gray    = '\x1b[90m'
embed_light_red     = '\x1b[91m'
embed_light_green   = '\x1b[92m'
embed_light_yellow  = '\x1b[93m'
embed_light_blue    = '\x1b[94m'
embed_light_magenta = '\x1b[95m'
embed_light_cyan    = '\x1b[96m'
embed_light_white   = '\x1b[97m'

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
				if self.state == "#":
					self.marked = True
					self.state  = f"{embed_red}?{embed_end}"
			return True
		elif mark == "False":
			if self.state == "#":
				if self.marked == False:
					if self.bombed:
						self.state  = f"{embed_red}X{embed_end}"
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
							self.state    = f"{embed_green}0{embed_end}"
							# Reveal adjacents cells when selected a 0 cell
							for cos in adj_cells:
								if 0 <= cos[1] < width and 0 <= cos[0] < height and grid[cos[0]][cos[1]].checked == False:
									grid[cos[0]][cos[1]].check()
						elif self.near_bomb == 1:
							self.state = f"{embed_light_yellow}{self.near_bomb}{embed_end}"
						elif 2 <= self.near_bomb <= 3:
							self.state = f"{embed_yellow}{self.near_bomb}{embed_end}"
						elif 3 < self.near_bomb:
							self.state = f"{embed_magenta}{self.near_bomb}{embed_end}"
						return True
		return True

# Create minesweeper
def create_grid(opt, custom=False):
	global width, height
	if custom:
		if int(opt[2]) <= 10 and int(opt[3]) <= 10:
			width,height,bomb_number = int(opt[2]), int(opt[3]), int(opt[4])
# Selecting difficulty
	elif int(opt[1]) == 1:
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
	print(f"{embed_blue}╔{'═'*(2 * width + 5)}╗{embed_end}")
	print(f"{embed_blue}║{embed_end}{' ' * (width - 3)}{embed_light_green}Minesweeper{embed_end}{' '* (width - 3)}{embed_blue}║{embed_end}")
	print(f"{embed_blue}╠{'═'*(2 * width + 5)}╣{embed_end}")

	# Showing columns number
	print(f"{embed_blue}║   {''.join([f'{x} ' for x in range(width)])}  ║{embed_end}")
	# Showing rows
	for y in range(height):
		print(f"{embed_blue}║ {y}{embed_end} {''.join([f'{cell.state} ' for cell in grid[y]])}{embed_blue}{y} ║{embed_end}")
	# Showing columns number
	print(f"{embed_blue}║   {''.join([f'{x} ' for x in range(width)])}  ║{embed_end}")

	# Finishing frame
	if finish:
		print(f"{embed_blue}╠{'═'*(2 * width + 5)}╣{embed_end}")
	else:
		print(f"{embed_blue}╚{'═'*(2 * width + 5)}╝{embed_end}")

def play():
	to = time.time()
	playing, win = True, False
	os.system('clear')
	help()
	show_grid()
	while playing:
		choice = input(f"Enter a couple 'x,y'\n>>> {embed_white}").split(",")
		print(embed_end)
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
			elif choice[0] == "anosweeper":
				solve()
		os.system('clear')
		show_grid()
	os.system('clear')
	solve(True)
	total_time = (int(10*(time.time() - to)))/10
	if win:
		print(f"{embed_blue}║{embed_end}{' ' * (width - 2)}{embed_blink}You Won !{embed_end}{' ' * (width - 2)}{embed_blue}║{embed_end}")
	else:
		print(f"{embed_blue}║{embed_end}{' ' * (width - 2)}{embed_blink}Game Over{embed_end}{' ' * (width - 2)}{embed_blue}║{embed_end}")
	print(f"{embed_blue}║{embed_end} Time: {' '*((2 * width - 4)-len(str(total_time)))}{embed_blink}{total_time}s{embed_end} {embed_blue}║{embed_end}")
	print(f"{embed_blue}╚{'═'*(2 * width + 5)}╝{embed_end}")


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
║ - To check a cell, enter the x and the y of the cell (for example "{embed_white}1,2{embed_end}" will check{" "*13}║
║ the cell on the second row and third column){" "*51}║
║ - To mark a cell, enter the x and the y of the cell followed by ",mark" (for example "{embed_white}1,2,mark{embed_end}"║
║ will put a "?" at the place of the cell){" "*55}║
║ - To show this help page, just enter "{embed_white}help{embed_end}\"{" "*52}║
╚{"═"*96}╝""")
	time.sleep(5)
	os.system('clear')

def solve(finish=False):
	global width, height
	for x in range(width):
		for y in range(height):
			grid[x][y].check()
	show_grid(finish)

if len(sys.argv) == 2:
	grid = []
	create_grid(sys.argv)

elif len(sys.argv) == 5:
	if sys.argv[1] != 'custom':
		grid = []
		create_grid(sys.argv, True)
	else:
		print("Usage :\n    -`python  minesweeper.py [difficulty 1-3]`\n    -`python3 minesweeper.py [difficulty 1-3]`\n    or\n    -`python  minesweeper custom [x] [y] [number of bombs]`\n    -`python3 minesweeper custom [x] [y] [number of bombs]`")
else:
	print("Usage :\n    -`python  minesweeper.py [difficulty 1-3]`\n    -`python3 minesweeper.py [difficulty 1-3]`\n    or\n    -`python  minesweeper custom [x] [y] [number of bombs]`\n    -`python3 minesweeper custom [x] [y] [number of bombs]`")
