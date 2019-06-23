from random import randint

print("DICE ROLLING SIM")

while 1 == 1:
	num = int(input("How many dice do you want to roll?"))

	dice = []
	for i in range(1, num + 1):
		j = randint(1, 6)
		dice.append(j)
		print(f'Dice {i} = {j}')

	print()
	print(f'DICE ROLL: {sum(dice)}')