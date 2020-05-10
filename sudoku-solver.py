# SUDOKU USING BACKTRACKING 
import time, os

fixed = [[0 for _ in range(9)] for _ in range(9)]


f = open('board.txt', 'r')
lines = f.readlines()
board = [[ int(n) for n in line.split() ] for line in lines ]
f.close()


# simple ---------------------------------------------------
# to mark fixed entered numbers

for i in range(9):
    for j in range(9):
        if board[i][j] != 0:
            fixed[i][j] = 1

def printBoard():
    for i in range(9):
        if i%3 == 0 and i != 0:
            for _ in range(9):
                print(" - ",end="")
            print() 
        for j in range(9):
            print(board[i][j],end=" ")
            if j%3 == 2 and j != 8:
                print(" | ",end="")
            
        print()
# -----------------------------------------------------------



# MAIN SHIT ################################################################################################

def checkIfPlacingIsPossible(currentRow,currentCol,number):
    gridRowNum = int( currentRow / 3)
    gridColNum = int( currentCol / 3)

    # check for the column, traversing each row
    for r in range(9):
        if board[r][currentCol] == number + 1 :
            return 0

    # check for the row, traversing each column
    for c in range(9):
        if board[currentRow][c] == number + 1 :
            return 0

    # checking for the square it belongs inside
    for r in range(gridRowNum * 3, gridRowNum * 3 + 3):
        for c in range( gridColNum * 3, gridColNum * 3 + 3 ):
            if r == currentRow and c == currentCol:
                pass
            elif board[r][c] == number + 1:
                return 0

    # if no error, return 1
    return 1



def nextPos(currentRow,currentCol):
    if currentCol == 8:
        currentCol = 0 
        currentRow += 1
    else:
        currentCol += 1
    while True:
        if currentRow > 8:
            printBoard()
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

#################################################################################################




####### MAIN LOOP
def sudoku(currentrow,currentcol):
    
    for number in range(9):

        # to erase current and previous(ie. next) position
        # board[currentrow][currentcol] = 0
        nextx, nexty = seekNextPosition(currentrow,currentcol)
        board[nextx][nexty] = 0

        # if you can place number + 1 here then place
        if checkIfPlacingIsPossible(currentrow,currentcol,number) == 1 :

            board[currentrow][currentcol] = number + 1

            # for visuals, remove the below 3 lines for the direct solution
            printBoard()
            time.sleep(0.1)
            os.system(('cls'))

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

