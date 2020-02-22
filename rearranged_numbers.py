#Given a number, return the difference between the maximum and 
#minimum numbers that can be formed when the digits are rearranged.

def rearranged_difference(num):
	digits = []

	for i in num:
		i = int(i)
		digits.append(i)

	digits.sort()

	for i in range(0, len(digits)):
		digits[i] = str(digits[i])

	smallest = int(''.join(digits))

	digits.sort(reverse = True)

	largest = int(''.join(digits))

	diff = largest - smallest

	print(f'{largest} - {smallest} = {diff}')

num = input()
rearranged_difference(num)