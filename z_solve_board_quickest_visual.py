import os, time

if os.path.exists("board-solved.txt"):
    os.remove('board-solved.txt')
os.system("python z_solve_board_quickest.py")

try:
    f = open('board-solved.txt', 'r')
    lines = f.readlines()
    solvedboard = [[ int(n) for n in line.split() ] for line in lines ]
    f.close()
except:
    print("BOARD ENTERED IS UNSOLVABLE, \nPLEASE CHECK THE NUMBERS AND TRY AGAIN")
    time.sleep(3)
    exit()

f = open('board.txt', 'r')
lines = f.readlines()
board = [[ int(n) for n in line.split() ] for line in lines ]
f.close()

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

boardForVisual = [[ n for n in line ] for line in board ]

fixed = [[0 for _ in range(9)] for _ in range(9)]
for i in range(9):
    for j in range(9):
        if board[i][j] != 0:
            fixed[i][j] = 1

# for start of board for visualization
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


def drawboard():
    for i in range(9):
        if i%3 == 2:
            pygame.draw.line(surface, (0, 0, 0), ((i+1)*(600/9), 0), ((i+1)*(600/9), 600), 3)
        else:
            pygame.draw.line(surface, (0, 0, 0), ((i+1)*(600/9), 0), ((i+1)*(600/9), 600), 1)
    for i in range(9):
        if i%3 == 2:
            pygame.draw.line(surface, (0, 0, 0), (0, (i+1)*(600/9)), (600, (i+1)*(600/9)), 3)
        else:
            pygame.draw.line(surface, (0, 0, 0), (0, (i+1)*(600/9)), (600, (i+1)*(600/9)), 1)

# VISUALIZE BACKTRACKING ####################################################################
def forVeryHardBoardTLE():
    surface.fill((255, 255, 255))
    drawboard()
    for j in range(9):
        for i in range(9):
            if solvedboard[i][j] != 0: 
                text = font.render(str(solvedboard[i][j]), 1, (0,0,0))
                surface.blit(text, ((j)*(600/9)+22, (i)*(600/9)+15) )

    win.blit(surface, (50,50))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit()
                    
def redrawVisualize():
    surface.fill((255, 255, 255))
    drawboard()
    for j in range(9):
        for i in range(9):
            if boardForVisual[i][j] != 0: 
                text = font.render(str(boardForVisual[i][j]), 1, (0,0,0))
                surface.blit(text, ((j)*(600/9)+22, (i)*(600/9)+15) )

    win.blit(surface, (50,50))
    pygame.display.update()

def highlightVisualize(y,x):
    # to exit while recurrsion
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()

    redrawVisualize()

    for i in range(9):
        for j in range(9):
            if boardForVisual[i][j] != 0 and fixed[i][j] != 1 :
                pygame.draw.rect(surface, (0,255,0), (j*(600/9) + 4, i*(600/9) + 4, (600/9)-8, (600/9)-8 ), 3)
    pygame.draw.rect(surface, (255,0,0), (x*(600/9), y*(600/9), (600/9), (600/9) ), 3)

    win.blit(surface, (50,50))
    pygame.display.update()
    
def checkIfPlacingIsPossible(currentRow,currentCol,number):
    gridRowNum = int( currentRow / 3)
    gridColNum = int( currentCol / 3)
    for r in range(9):
        if boardForVisual[r][currentCol] == number + 1 :
            return 0
    for c in range(9):
        if boardForVisual[currentRow][c] == number + 1 :
            return 0
    for r in range(gridRowNum * 3, gridRowNum * 3 + 3):
        for c in range( gridColNum * 3, gridColNum * 3 + 3 ):
            if r == currentRow and c == currentCol:
                pass
            elif boardForVisual[r][c] == number + 1:
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
            redrawVisualize()
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            pygame.quit()
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



def visualizeBacktracking(currentRow,currentCol):
    global iterations, divideFaster
    for number in range(9):
        nextx, nexty = seekNextPosition(currentRow,currentCol)
        boardForVisual[nextx][nexty] = 0
        if checkIfPlacingIsPossible(currentRow,currentCol,number) == 1 :
            boardForVisual[currentRow][currentCol] = number + 1

            if divideFaster <= 20:
                highlightVisualize(currentRow,currentCol)
            else:
                forVeryHardBoardTLE()

            time.sleep(0.1/divideFaster)
            iterations += 1
            if iterations > 200:
                divideFaster += 2
                iterations = 0

            nextx, nexty = nextPos(currentRow,currentCol)
            visualizeBacktracking(nextx,nexty)
        else:
            boardForVisual[currentRow][currentCol] = 0

# ##################################### END OF VISUALIZING BACKTRACKING


# pygame
import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_caption("SUDOKU")
clock = pygame.time.Clock()
logoIMG = pygame.image.load("logo.png")
pygame.display.set_icon(logoIMG)

win = pygame.display.set_mode((700,700))
win.fill((255,255,255))
pygame.draw.rect(win, (0,0,0), (48,48,604,604), 3)
surface = pygame.Surface((600,600))
font = pygame.font.SysFont('Calibri', 45)

iterations = 0
divideFaster = 1

visualizeBacktracking(startx,starty)
