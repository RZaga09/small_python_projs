'''
Mind The Gap (by Donnamae on edabit.com)

A number is gapful if it is at least 3 digits long and is divisible by the number formed by stringing the first and last numbers together. 
The smallest number that fits this description is 100. First digit is 1, last digit is 0, forming 10, which is a factor of 100. Therefore, 100 is gapful.

*The original challenge has the printed value being the closest gap number. For simplicity's sake I
will have it print the next gap number instead
'''

def check(x):
	global y
	for i in str(x):
		num_li.append(i)
	if x % int(str(num_li[0]) + str(num_li[len(num_li) - 1])) == 0:
		if len(num_li) >= 3:
			print(f'Nearest Gapful Number = {x}')
		else:
			y += 1
			x = z + y
			num_li.clear()
			check(x)
	else:
		y += 1
		x = z + y
		num_li.clear()
		check(x)

while 1 == 1:
	num_li = []
	x = int(input('Input Number '))
	y = 0
	z = x
	check(x)