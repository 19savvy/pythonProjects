theBoard = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
possibleNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rows = 3
cols = 3

def printBoard(board):
    print(str(board[0][0]) + '|' + str(board[0][1]) + '|' + str(board[0][2]))
    print('-+-+-')
    print(str(board[1][0]) + '|' + str(board[1][1]) + '|' + str(board[1][2]))
    print('-+-+-')
    print(str(board[2][0]) + '|' + str(board[2][1]) + '|' + str(board[2][2]))

def changeBoard(num, turn):
    num -= 1

    if num == 0:
        theBoard[0][0] = turn
    elif num == 1:
        theBoard[0][1] = turn
    elif num == 2:
        theBoard[0][2] = turn
    elif num == 3:
        theBoard[1][0] = turn
    elif num == 4:
        theBoard[1][1] = turn
    elif num == 5:
        theBoard[1][2] = turn
    elif num == 6:
        theBoard[2][0] = turn
    elif num == 7:
        theBoard[2][1] = turn
    elif num == 8:
        theBoard[2][2] = turn
        
leaveLoop = False
turn = 'X'
turnCount = 0

def checkWinner(theBoard):
    #rows
    if (theBoard[0][0] == 'X' and theBoard[0][1] == 'X' and theBoard[0][2] == 'X'):
        print('X wins!')
        return 'X'
    elif (theBoard[0][0] == 'O' and theBoard[0][1] == 'O' and theBoard[0][2] == 'O'):
        print('O wins!')
        return 'O'
    if (theBoard[1][0] == 'X' and theBoard[1][1] == 'X' and theBoard[1][2] == 'X'):
        print('X wins!')
        return 'X'
    elif (theBoard[1][0] == 'O' and theBoard[1][1] == 'O' and theBoard[1][2] == 'O'):
        print('O wins!')
        return 'O'
    if (theBoard[2][0] == 'X' and theBoard[2][1] == 'X' and theBoard[2][2] == 'X'):
        print('X wins!')
        return 'X'
    elif (theBoard[2][0] == 'O' and theBoard[2][1] == 'O' and theBoard[2][2] == 'O'):
        print('O wins!')
        return 'O'
    
    #columns
    if (theBoard[0][0] == 'X' and theBoard[1][0] == 'X' and theBoard[2][0] == 'X'):
        print('X wins!')
        return 'X'
    elif (theBoard[0][0] == 'O' and theBoard[1][0] == 'O' and theBoard[2][0] == 'O'):
        print('O wins!')
        return 'O'
    if (theBoard[0][1] == 'X' and theBoard[1][1] == 'X' and theBoard[2][1] == 'X'):
        print('X wins!')
        return 'X'
    elif (theBoard[0][1] == 'O' and theBoard[1][1] == 'O' and theBoard[2][1] == 'O'):
        print('O wins!')
        return 'O'
    if (theBoard[0][2] == 'X' and theBoard[1][2] == 'X' and theBoard[2][2] == 'X'):
        print('X wins!')
        return 'X'
    elif (theBoard[0][2] == 'O' and theBoard[1][2] == 'O' and theBoard[2][2] == 'O'):
        print('O wins!')
        return 'O'
    
    #diagonals
    if (theBoard[0][0] == 'X' and theBoard[1][1] == 'X' and theBoard[2][2] == 'X'):
        print('X wins!')
        return 'X'
    elif (theBoard[0][2] == 'O' and theBoard[1][1] == 'O' and theBoard[2][0] == 'O'):
        print('O wins!')
        return 'O'

    

while leaveLoop == False:
    printBoard(theBoard)
    
    if turnCount % 2 == 1:
        turn = 'O'
    else:
        turn = 'X'
    print('It\'s ' + turn + '\' turn')
    print('pick a space')
    try:
        move = int(input('pick a number (1-9)\n'))
        if move >= 1 and move <10 and move in possibleNumbers:
            turnCount += 1
            printBoard(theBoard)
            changeBoard(move, turn)
            possibleNumbers.remove(move)
        elif move not in possibleNumbers:
            print('this number has been selected')
        else:
            print('enter a number between 1 and 9')
    except ValueError:
        print('Enter an integer')   
    exitGame = checkWinner(theBoard)
    if exitGame == 'O' or exitGame == 'X':
        leaveLoop = True 



printBoard(theBoard)
