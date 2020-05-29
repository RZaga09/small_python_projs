print('Adder using binary adder gates\n')


def input_number(letter):
    num = int(input(f'Number {letter}: '))
    if num >= 0:
        return num
    else:
        print('Type a positive numbers')


def convert_to_binary(num):
    binary = []
    while num != 0:
        binary.insert(0, int(num % 2))
        num /= 2
        if num.is_integer() == False:
            num -= 0.5
    return binary


def half_adder(a, b):
    val = 1 if (a or b == 1) and (a != b) else 0
    carry = 1 if (a == b) and (a == 1) else 0
    return val, carry


def full_adder(a, b, c):
    tempV, tempC = half_adder(a, b)
    finalV, finalC = half_adder(tempV, c)
    finalC = 1 if (finalC or tempC == 1) else 0
    return finalV, finalC


a = input_number('A')
b = input_number('B')
binary_a = list(reversed(convert_to_binary(a)))
binary_b = list(reversed(convert_to_binary(b)))
sum = []
c = 0


for i in range(0, min(len(binary_a), len(binary_b))):
    s, c = full_adder(binary_a[i], binary_b[i], c)
    sum.append(s)

if len(binary_a) > len(binary_b):
    for i in range(len(binary_b), len(binary_a)):
        s, c = half_adder(binary_a[i], c)
        sum.append(s)
elif len(binary_b) > len(binary_a):
    for i in range(len(binary_a), len(binary_b)):
        s, c = half_adder(binary_b[i], c)
        sum.append(s)
else:
    sum.append(c)

n = 1
answer = 0
for i in sum:
    answer += (i * n)
    n *= 2
print(f'Answer: {answer}')
