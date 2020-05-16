import os, time

if os.path.exists("board-solved.txt"):
    os.remove('board-solved.txt')
os.system("python z_solve_board_quick.py")

f = open('board.txt', 'r')
lines = f.readlines()
board = [[ int(n) for n in line.split() ] for line in lines ]
boardForVisual = [[ int(n) for n in line.split() ] for line in lines ]
f.close()

try:
    f = open('board-solved.txt', 'r')
except:
    print("BOARD ENTERED IS UNSOLVABLE, \nPLEASE CHECK THE NUMBERS AND TRY AGAIN")
    time.sleep(3)
    exit()


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


# Visuals ------------------------------------------------
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


def redraw():
    surface.fill((255, 255, 255))
    drawboard()
    for j in range(9):
        for i in range(9):
            if board[i][j] != 0: 
                text = font.render(str(board[i][j]), 1, (0,0,0))
                surface.blit(text, ((j)*(600/9)+22, (i)*(600/9)+15) )
    win.blit(surface, (50,50))
    pygame.display.update()

def redrawtemp(): # only for drawing the board and numbers after success/failure flash
    for j in range(9):
        for i in range(9):
            if board[i][j] != 0: 
                text = font.render(str(board[i][j]), 1, (0,0,0))
                surface.blit(text, ((j)*(600/9)+22, (i)*(600/9)+15) )
    win.blit(surface, (50,50))
    pygame.display.update()
    pygame.time.delay(400)
    redraw()


def danger(y,x):
    surface.fill((255, 255, 255))
    drawboard()
    pygame.draw.rect(surface, (255,0,0), (x*(600/9), y*(600/9), (600/9), (600/9) ) )
    redrawtemp()

def success(y,x):
    surface.fill((255, 255, 255))
    drawboard()
    pygame.draw.rect(surface, (0,255,0), (x*(600/9), y*(600/9), (600/9), (600/9) ) )
    redrawtemp()

def highlight(y,x):
    redraw()
    pygame.draw.rect(surface, (255,0,0), (x*(600/9), y*(600/9), (600/9), (600/9) ), 3)
    win.blit(surface, (50,50))
    pygame.display.update()
# Visuals over ---------------------------------------------------




# VISUALIZE BACKTRACKING ####################################################################

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

            if divideFaster <= 250:
                highlightVisualize(currentRow,currentCol)

            time.sleep(0.1/divideFaster)
            iterations += 1
            if iterations > 200:
                divideFaster += 5
                iterations = 100

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

redraw()
timee = 0
timeTimer = 0

iterations = 0
divideFaster = 1

while True:
    clock.tick(60)

    if timeTimer > 0 :
        timeTimer -= 1
    else:
        timeTimer = 50
        timee += 1
        text = font.render(str(timee), 1, (0,0,0))
        pygame.draw.rect(win, (255,255,255), (600,660,200,50) )
        win.blit(text, ( 650, 655 ) )
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()
            if event.key == K_s:
                visualizeBacktracking(startx,starty)
                exit()

        if event.type == MOUSEBUTTONDOWN:
            ty,tx = pygame.mouse.get_pos()
            ty -= 50
            tx -= 50
            tx = int(tx//(600/9))
            ty = int(ty//(600/9))
            if tx < 9 and tx >= 0 and ty >= 0 and ty < 9 and fixed[tx][ty] != 1 :
                x, y = tx, ty
                highlight(x,y)
            else:
                redraw()

        if event.type == KEYDOWN:
            num = 0
            if event.key == K_0 or event.key == K_KP0 :
                board[x][y] = 0
            elif event.key == K_1 or event.key == K_KP1:
                num = 1
            elif event.key == K_2 or event.key == K_KP2 :
                num = 2
            elif event.key == K_3 or event.key == K_KP3 :
                num = 3
            elif event.key == K_4 or event.key == K_KP4 :
                num = 4
            elif event.key == K_5 or event.key == K_KP5 :
                num = 5
            elif event.key == K_6 or event.key == K_KP6 :
                num = 6
            elif event.key == K_7 or event.key == K_KP7 :
                num = 7
            elif event.key == K_8 or event.key == K_KP8 :
                num = 8
            elif event.key == K_9 or event.key == K_KP9 :
                num = 9
            if fixed[x][y] != 1:
                if num == solvedboard[x][y] and num != 0:
                    board[x][y] = num
                    success(x,y)
                elif num != 0:
                    board[x][y] = 0
                    danger(x,y)
                else:
                    redraw()