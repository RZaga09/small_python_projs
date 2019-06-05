'''
LIST ENDS

Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new 
list of only the first and last elements of the given list. For practice, write this code inside a function.
'''
a = [5, 10, 15, 20, 25]
b = []

def firlas():
	b.append(a[0])
	b.append(a[len(a) - 1])
	print(b)

firlas()


'''
FIBONACCI

Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.
'''

a = [0, 1]
num = int(input('Type a number '))

def fibonacci(i):
	for i in range(0, num):
		a.append(a[i] + a[i+1])

if num == 0:
	print('[]')
elif num == 1:
	print('[0]')
elif num == 2:
	print('[0, 1]')
else:
	num = num - 2
	fibonacci(num)
	print(a)
