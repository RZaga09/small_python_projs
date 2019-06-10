#Prints out number of words and characters (not counting spaces) in myfile.txt

f = open('myfile.txt', 'r')
contents = f.read()
chars = []
words = []
words2 = []
x = 0

for i in contents:
	words.append(i)
	if i != ' ':
		chars.append(i)

for i in range(0, ((len(words)) - 1)):
	if words[i] != words [i + 1]:
		words2.append(words[i + 1])


if words2[len(words2) - 1] == ' ':
	words2.pop(len(words2) - 1)

for i in words2:
	if i == ' ':
		x += 1

print(f'Char Count: {len(chars)}')
print(f'Word Count: {x + 1}')