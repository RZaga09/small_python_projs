from copy import deepcopy
import random

board = [
    [2, 4, 8, 16],
    [4, 8, 16, 1024],
    [2, 16, 8, 2],
    [8, 4, 1024, 4]
]

printNums = {
    0: '   0',
    2: '   2',
    4: '   4',
    8: '   8',
    16: '  16',
    32: '  32',
    64: '  64',
    128: ' 128',
    256: ' 256',
    512: ' 512',
    1024: '1024',
    2048: '2048'
}


def initBoard():
    tempBoard = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    for i in range(0, 2):
        i = random.randint(0, 3)
        j = random.randint(0, 3)
        tempBoard[i][j] = 2
    return tempBoard


def showBoard():
    print(' ---- ---- ---- ----')
    for i in range(0, 4):
        print(
            f'|{printNums[board[i][0]]}|{printNums[board[i][1]]}|{printNums[board[i][2]]}|{printNums[board[i][3]]}|')
        print(' ---- ---- ---- ----')
    print('')


def moveUP():
    tempValue = 4
    for i in range(0, 4):
        for j in range(0, 3):
            if j == tempValue:
                tempValue = 4
                continue
            if board[j][i] == board[j + 1][i] and board[j][i] != 0:
                board[j][i] *= 2
                board[j + 1][i] = 0
                tempValue = j + 1
            elif board[j + 1][i] != 0:
                continue
            elif j < 2:
                if board[j][i] == board[j + 2][i] and board[j][i] != 0:
                    board[j][i] *= 2
                    board[j + 2][i] = 0
                    tempValue = j + 1
                elif board[j + 2][i] != 0:
                    continue
                elif j < 1:
                    if board[j][i] == board[j + 3][i] and board[j][i] != 0:
                        board[j][i] *= 2
                        board[j + 3][i] = 0
                        tempValue = j + 1

        for _ in range(0, 4):
            for j in range(1, 4):
                if board[j - 1][i] == 0:
                    board[j - 1][i] = board[j][i]
                    board[j][i] = 0


def moveDOWN():
    tempValue = 4
    for i in range(0, 4):
        for j in range(3, 0, -1):
            if j == tempValue:
                tempValue = 4
                continue
            if board[j][i] == board[j - 1][i] and board[j][i] != 0:
                board[j][i] *= 2
                board[j - 1][i] = 0
                tempValue = j - 1
            elif board[j - 1][i] != 0:
                continue
            elif j > 1:
                if board[j][i] == board[j - 2][i] and board[j][i] != 0:
                    board[j][i] *= 2
                    board[j - 2][i] = 0
                    tempValue = j - 1
                elif board[j - 2][i] != 0:
                    continue
                elif j > 2:
                    if board[j][i] == board[j - 3][i] and board[j][i] != 0:
                        board[j][i] *= 2
                        board[j - 3][i] = 0
                        tempValue = j - 1

        for _ in range(0, 4):
            for j in range(2, -1, -1):
                if board[j + 1][i] == 0:
                    board[j + 1][i] = board[j][i]
                    board[j][i] = 0


def moveRIGHT():
    tempValue = 4
    for i in range(0, 4):
        for j in range(3, 0, -1):
            if j == tempValue:
                tempValue = 4
                continue
            if board[i][j] == board[i][j - 1] and board[i][j] != 0:
                board[i][j] *= 2
                board[i][j - 1] = 0
                tempValue = j - 1
            elif board[i][j - 1] != 0:
                continue
            elif j > 1:
                if board[i][j] == board[i][j - 2] and board[i][j] != 0:
                    board[i][j] *= 2
                    board[i][j - 2] = 0
                    tempValue = j - 1
                elif board[i][j - 2] != 0:
                    continue
                elif j > 2:
                    if board[i][j] == board[i][j - 3] and board[i][j] != 0:
                        board[i][j] *= 2
                        board[i][j - 3] = 0
                        tempValue = j - 1

        for _ in range(0, 4):
            for j in range(2, -1, -1):
                if board[i][j + 1] == 0:
                    board[i][j + 1] = board[i][j]
                    board[i][j] = 0


def moveLEFT():
    tempValue = 4
    for i in range(0, 4):
        for j in range(0, 3):
            if j == tempValue:
                tempValue = 4
                continue
            if board[i][j] == board[i][j + 1] and board[i][j] != 0:
                board[i][j] *= 2
                board[i][j + 1] = 0
                tempValue = j + 1
            elif board[i][j + 1] != 0:
                continue
            elif j < 2:
                if board[i][j] == board[i][j + 2] and board[i][j] != 0:
                    board[i][j] *= 2
                    board[i][j + 2] = 0
                    tempValue = j + 1
                elif board[i][j - 2] != 0:
                    continue
                elif j < 1:
                    if board[i][j] == board[i][j + 3] and board[i][j] != 0:
                        board[i][j] *= 2
                        board[i][j + 3] = 0
                        tempValue = j + 1

        for _ in range(0, 4):
            for j in range(1, 4):
                if board[i][j - 1] == 0:
                    board[i][j - 1] = board[i][j]
                    board[i][j] = 0


def addNew():
    tempList = []
    for i in range(0, 4):
        for j in range(0, 4):
            if board[i][j] == 0:
                tempList.append([i, j])
    random.shuffle(tempList)
    i = random.choice(tempList)
    j = random.randint(0, 3)
    board[i[0]][i[1]] = 2 if j < 3 else 4


def userInput():
    print('UP/DOWN/LEFT/RIGHT\n')
    while 1 == 1:
        move = input('Your Move: ')
        if move.upper() == 'UP':
            moveUP()
            break
        elif move.upper() == 'DOWN':
            moveDOWN()
            break
        elif move.upper() == 'LEFT':
            moveLEFT()
            break
        elif move.upper() == 'RIGHT':
            moveRIGHT()
            break
        else:
            print('Type UP/DOWN/LEFT/RIGHT\n')


def checkWin():
    for i in board:
        for j in i:
            if j == 2048:
                return True
    return False


def checkLose():
    for i in board:
        if 0 in i:
            return False
        else:
            for j in range(0, 3):
                if i[j] == i[j + 1]:
                    return False

    for i in range(0, 4):
        for j in range(0, 3):
            if board[j][i] == board[j + 1][i]:
                return False

    return True


board = initBoard()
debugBoard = deepcopy(board)
showBoard()
while 1 == 1:
    while 1 == 1:
        userInput()
        if board == debugBoard:
            print('Move not valid!')
        else:
            break
    addNew()
    debugBoard = deepcopy(board)
    showBoard()
    if checkWin():
        print('WIN!')
        break
    if checkLose():
        print('LOSE!')
        break
