# THIS WILL SOLVE THE BOARD WITH ONE OF THE QUICKEST METHOD POSSIBLE, GETTING THE SQUARE WITH THE HIGHEST NUMBER OF DIGITS TO THE FIRST POSITION, USE BACKTRACKING AND SOLVE IT, AND REPOSITION THE BOARD AFTER SOLVING
fixed = [[0 for _ in range(9)] for _ in range(9)]

f = open('board.txt', 'r')
lines = f.readlines()
board = [[ int(n) for n in line.split() ] for line in lines ]
f.close()

# ###########################################################
# to get the grid with most numbers to the first square position
maxNUMBERSgridNox = 0
maxNUMBERSgridNoy = 0
max = 0
for i in range(3):
    for j in range(3):
        tempmax = 0
        for r in range(i * 3, i * 3 + 3):
            for c in range( j * 3, j * 3 + 3 ):
                if board[r][c] != 0 :
                    tempmax += 1
        if tempmax > max:
            max = tempmax
            maxNUMBERSgridNox = i
            maxNUMBERSgridNoy = j
maxNUMBERSgridNox *= 3
maxNUMBERSgridNoy *= 3

# to shift the columns
for i in range(3):
    for j in range(9):
        board[j][i], board[j][maxNUMBERSgridNoy+i] = board[j][maxNUMBERSgridNoy+i], board[j][i]
# to shift the rows
for i in range(3):
    board[i], board[maxNUMBERSgridNox+i] = board[maxNUMBERSgridNox+i], board[i]
# ###########################################################


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
            # ###########################################################
            for i in range(3):
                for j in range(9):
                    board[j][i], board[j][maxNUMBERSgridNoy+i] = board[j][maxNUMBERSgridNoy+i], board[j][i]
            # to shift the rows
            for i in range(3):
                board[i], board[maxNUMBERSgridNox+i] = board[maxNUMBERSgridNox+i], board[i]
            # ###########################################################

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

