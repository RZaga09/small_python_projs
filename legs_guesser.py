#Checks how many legs are present when there is a certain number of chickens, cows, and pigs

print('How many:')
chickens = int(input('Chickens: '))
cows = int(input('Cows: '))
pigs = int(input('Pigs: '))

ch_legs = chickens * 2
co_legs = cows * 4
pi_legs = pigs * 4
total = ch_legs + co_legs + pi_legs

print(f'{chickens} Chickens: {ch_legs} legs')
print(f'{cows} Cows: {co_legs} legs')
print(f'{pigs} Pigs: {pi_legs} legs')
print(f'Total Legs: {total}')