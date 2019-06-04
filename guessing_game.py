from random import randint
loop = True
loop2 = True
loop3 = True

def check(x, ans):
	while loop3 == True:	
		if ans > x:
			print('Lower')
			continue
		elif ans < x:
			print('Higher')
			continue
		elif ans == x:
			print('You Win!')
			break

while loop == True:
	x = randint(1, 100)
	print('Guessing Game!')
	print('Type a number between 1 and 100')

	while loop2 == True:
		ans = input()

		try:
			ans = (int(ans))
			if ans > 100 or ans < 1:
				print('Number must be between 1 and 100')
				continue
			elif ans > x:
				print('Lower')
				continue
			elif ans < x:
				print('Higher')
				continue
			elif ans == x:
				print('You Win!')
				break

		except ValueError:
			print('Enter a number')
			loop2 = True
			continue
