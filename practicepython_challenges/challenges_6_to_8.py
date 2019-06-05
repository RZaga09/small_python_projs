'''
STRING LISTS

Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
'''


string = input(('type something '))
str_list = []
palindrome = True

for i in string:
	str_list.append(i)

if len(str_list) % 2 != 0:
	str_list.pop((int(len(str_list) / 2)))

while palindrome == True:
	if str_list[0] == str_list[len(str_list) - 1]:
		str_list.pop(0)
		str_list.pop(len(str_list) - 1)

		if len(str_list) == 0:
			print('Palindrome')
			break
		else:
			continue

	else:
		palindrome = False
		print('Not a palindrome')
		break


'''
LIST COMPREHENSIONS

Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
'''


a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [i for i in a if i % 2 == 0]
print(b)


'''
ROCK PAPER SCISSORS

Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), 
compare them, print out a message of congratulations to the winner, 
and ask if the players want to start a new game)
'''

from random import randint
again = True

choice = ['Rock', 'Paper', 'Scissors']

while again == True:

	print('1 = Rock \n2 = Paper \n3 = Scissors')
	play = int(input())

	comp = randint(1, 3)
	if play == comp:
		print(f'Player: {choice[play - 1]} \nComputer: {choice[comp - 1]} \nDraw')
	elif play == 1:
		if comp == 2:
			print(f'Player: {choice[play - 1]} \nComputer: {choice[comp - 1]} \nYou Lose')
		elif comp == 3:
			print(f'Player: {choice[play - 1]} \nComputer: {choice[comp - 1]} \nYou Win')

	elif play == 2:
		if comp == 1:
			print(f'Player: {choice[play - 1]} \nComputer: {choice[comp - 1]} \nYou Win')
		elif comp == 3:
			print(f'Player: {choice[play - 1]} \nComputer: {choice[comp - 1]} \nYou Lose')

	elif play == 3:
		if comp == 2:
			print(f'Player: {choice[play - 1]} \nComputer: {choice[comp - 1]} \nYou Win')
		elif comp == 1:
			print(f'Player: {choice[play - 1]} \nComputer: {choice[comp - 1]} \nYou Lose')

	cont = input('Start new game? (y/n) ')
	if cont == 'y':
		continue
	elif cont == 'n':
		break
