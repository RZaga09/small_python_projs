'''
CHARACTER INPUT

Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:
1. Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
2. Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
'''

name = input('input your name ')
age = input('input your age ')
year = int(input('What was your most recent year where you celebrated your birthday? '))
no_iter = int(input('name one more number '))
birthyear = year - int(age)
turn_100 = birthyear + 100

for i in range(0, no_iter):
	print(f'You, {name} will be 100 in the year {turn_100}')

'''
ODD OR EVEN

Ask the user for a number. Depending on whether the number is even or odd, 
print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
Extras:
1. If the number is a multiple of 4, print out a different message.
2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''
number = int(input('input a num '))
if number % 2 == 0:
	if number % 4 == 0:
		print(f'{number} is divisible by 4')
	else:
		print(f'{number} is even')
else:
	print(f'{number} is odd')

num = int(input('enter another number '))
check = int(input('enter one more number '))
if num % check == 0:
	print(f'{num} is divisible by {check}')
else:
	print(f'{num} is not divisible by {check}')

'''
LIST LESS THAN TEN

Take a list, say for example this one:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.
Extras:
1. Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
2. Write this in one line of Python. (i failed to do this one)
3. Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
extra = []
for i in a:
	if i < 5:
		print(i)
		extra.append(i)
	else:
		continue
print(extra)
extra.clear()

comp_point = int(input('input a number '))
for i in a:
	if i < comp_point:
		print(i)
		extra.append(i)
	else:
		continue
print(extra) 

'''
DIVISORS

Create a program that asks the user for a number and then prints out 
a list of all the divisors of that number. 
(If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''

num = int(input('input a number '))
divisors = []
for i in range(1, num):
	if num % i == 0:
		divisors.append(i)
	else:
		continue
print(f'divisors: {divisors}')


'''
LIST OVERLAP

Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that 
are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:
1.    Randomly generate two lists to test this (decided not to bother with this one)
2.   Write this in one line of Python (don't know how to do this one)
'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common = []
for i in a:
	for j in b:
  		if i == j:
  			common.append(i)
  		else:
  			continue
for i in range(0, ((len(common)) - 2)):
	if common[i] == common[i + 1]:
		common.remove(common[i + 1])

print(common)