# FIRST WILL GENERATE 3 DIAGONAL GRIDS, ONLY CHECKING FOR EACH RANDOM NUMBER THE SAME GRID ERROR( ie if the number is in the same grid )
# IT WILL THEN FILL IN THE REMAINING GRID NUMBERRS RECURSIVELY

import random

board = [[0 for _ in range(9)] for _ in range(9)]

# placing the first 3 diagonal grids 
# --------------------------------------------------------- #
num = 0
for gridNumber in range(3):
    for currentRow in range(gridNumber * 3, gridNumber * 3 + 3):
        for currentCol in range(gridNumber * 3, gridNumber * 3 + 3):

            run = True
            while run:

                run = False

                num = random.randint(1,9)
                
                for r in range(gridNumber * 3, gridNumber * 3 + 3):
                    if not run:
                        for c in range( gridNumber * 3, gridNumber * 3 + 3 ):
                            if board[r][c] == num :
                                run = True
                                break

            board[currentRow][currentCol] = num
            # print(num)
            # for i in range(9):
            #     print(board[i])
# --------------------------------------------------------- #

fixed = [[0 for _ in range(9)] for _ in range(9)]
for i in range(9):
    for j in range(9):
        if board[i][j] != 0:
            fixed[i][j] = 1
            
# _____________________ finding values for remaining grids recursively ____________________________________ #

def SaveBoardAndExit():
    for _ in range(60):
        board[random.randint(0,8)][random.randint(0,8)] = 0
    open('board.txt', 'w').close()
    f = open('board.txt','a')
    for line in board:
        for num in line:
            f.write("%d " %num)
        f.write("\n")
    f.close()
    exit()

def nextPos(currentRow,currentCol):
    if currentCol == 8:
        currentCol = 0 
        currentRow += 1
    else:
        currentCol += 1
    while True:
        if currentRow > 8:
            SaveBoardAndExit()

        if fixed[currentRow][currentCol] == 0:            
            return currentRow, currentCol
        else:
            currentCol += 1
            if currentCol > 8:
                currentCol = 0 
                currentRow += 1

def seekNextPosition(currentRow,currentCol) :
    tr = currentRow * 1
    tc = currentCol * 1
    if currentCol == 8:
        currentCol = 0 
        currentRow += 1
    else:
        currentCol += 1
    while True:
        if currentRow > 8:
            return tr, tc
        if fixed[currentRow][currentCol] == 0:            
            return currentRow, currentCol
        else:
            currentCol += 1
            if currentCol > 8:
                currentCol = 0 
                currentRow += 1

def checkIfPlacingIsPossible(currentRow,currentCol,number):
    gridRowNum = int( currentRow / 3)
    gridColNum = int( currentCol / 3)
    for r in range(9):
        if board[r][currentCol] == number + 1 or board[currentRow][r] == number + 1 :
            return 0
    for r in range(gridRowNum * 3, gridRowNum * 3 + 3):
        for c in range( gridColNum * 3, gridColNum * 3 + 3 ):
            if r == currentRow and c == currentCol:
                pass
            elif board[r][c] == number + 1:
                return 0
    return 1                
# _________________________________________________________ #


def sudoku(currentrow,currentcol):
    for number in range(9):
        nextx, nexty = seekNextPosition(currentrow,currentcol)
        board[nextx][nexty] = 0
        if checkIfPlacingIsPossible(currentrow,currentcol,number) == 1 :
            board[currentrow][currentcol] = number + 1
            nextx, nexty = nextPos(currentrow,currentcol)
            sudoku(nextx,nexty)
        else:
            board[currentrow][currentcol] = 0


sudoku(0,3)

