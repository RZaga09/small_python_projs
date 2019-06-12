'''
Tic-Tac-Toe in Python

Stuff not implemented here
1. Not allowing overlay over spots already having a thing
2. No checking for draws
'''
r1 = [' ', ' ', ' ']
r2 = [' ', ' ', ' ']
r3 = [' ', ' ', ' ']
game = True
xturn = True

def play():
	global game

	print(r1)
	print(r2)
	print(r3)
	check()
	if game == True:
		choice()

def check():
	global game

	if r1[0] != ' ':
		if r1[0] == r1[1] == r1[2]:
			print(f'{r1[0]} wins')
			game = False
		elif r1[0] == r2[0] == r3[0]:
			print(f'{r1[0]} wins')
			game = False
		elif r1[0] == r2[1] == r3[2]:
			print(f'{r1[0]} wins')
			game = False

	elif r3[0] != ' ':
		if r3[0] == r3[1] == r3[2]:
			print(f'{r3[0]} wins')
			game = False
		elif r3[0] == r2[1] == r1[2]:
			print(f'{r3[0]} wins')
			game = False

	elif r2[1] != ' ':
		if r2[1] == r1[1] == r3[1]:
			print(f'{r2[1]} wins')
			game = False
		elif r2[1] == r2[0] == r2[2]:
			print(f'{r2[1]} wins')
			game = False

	elif r1[2] != ' ':
		if r1[2] == r2[2] == r3[2]:
			print(f'{r1[2]} wins')
			game = False


def choice():
	global xturn

	if xturn == True:
		print('X')
		row = int(input('Row:'))
		col = int(input('Column:'))
		if row == 1:
			r1[col - 1] = 'X'
		elif row == 2:
			r2[col - 1] = 'X'
		elif row == 3:
			r3[col - 1] = 'X'
		xturn = False
		play()

	else:
		print('O')
		row = int(input('Row:'))
		col = int(input('Column:'))
		if row == 1:
			r1[col - 1] = 'O'
		elif row == 2:
			r2[col - 1] = 'O'
		elif row == 3:
			r3[col - 1] = 'O'
		xturn = True
		play()


play()