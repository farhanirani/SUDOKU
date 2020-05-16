# THIS CODE IS TO JUST SOLVE AND SAVE THE SOLVED BOARD QUICKLY
fixed = [[0 for _ in range(9)] for _ in range(9)]

f = open('board.txt', 'r')
lines = f.readlines()
board = [[ int(n) for n in line.split() ] for line in lines ]
f.close()

for i in range(9):
    for j in range(9):
        if board[i][j] != 0:
            fixed[i][j] = 1

def checkIfPlacingIsPossible(currentRow,currentCol,number):
    gridRowNum = int( currentRow / 3)
    gridColNum = int( currentCol / 3)
    for r in range(9):
        if board[r][currentCol] == number + 1 :
            return 0
    for c in range(9):
        if board[currentRow][c] == number + 1 :
            return 0
    for r in range(gridRowNum * 3, gridRowNum * 3 + 3):
        for c in range( gridColNum * 3, gridColNum * 3 + 3 ):
            if r == currentRow and c == currentCol:
                pass
            elif board[r][c] == number + 1:
                return 0
    return 1

def nextPos(currentRow,currentCol):
    if currentCol == 8:
        currentCol = 0 
        currentRow += 1
    else:
        currentCol += 1
    while True:
        if currentRow > 8:

            open('board-solved.txt', 'w').close()
            f = open('board-solved.txt','a')
            for line in board:
                for num in line:
                    f.write("%d " %num)
                f.write("\n")
            f.close()

            exit()
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

####### MAIN LOOP
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

startx = 0
starty = 0
found = False
for i in range(9):
    if not found:
        for j in range(9):
            if fixed[i][j] == 0:
                startx = i
                starty = j
                found = True
                break
sudoku(startx,starty)

