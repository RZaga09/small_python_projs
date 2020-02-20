# Take an input string parameter and determine if exactly 3
# question marks exist between every pair of numbers that add up to 10.
# arrb6???4xxbl5???ee5 (true)
# acc?7??sss?3rr1??????5 (true)
# 5??aaaaaaaaaaaaaaaa?5?5 (false)
# 9???1???9???1???9 (true)
# aa6?9 (false)

x = input()
digit = []
mark = []
yes = False

for i in range(0, len(x)):
    y = x[i]
    try:
        int(y)
        digit.append(i)
    except:
        pass
    if x[i] == "?":
        mark.append(i)

for i in range(0, len(digit) - 1):
    marks = 0
    if int(x[digit[i]]) + int(x[digit[i + 1]]) == 10:
        for j in range(0, len(mark)):
            if mark[j] > digit[i] and mark[j] < digit[i + 1]:
                marks += 1
        if marks == 3:
            yes = True
        else:
            yes = False
            break
    else:
        pass

print(yes)
