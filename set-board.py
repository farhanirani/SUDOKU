import pygame
from pygame.locals import *
pygame.init()
pygame.display.set_caption("SET BOARD")
clock = pygame.time.Clock()
logoIMG = pygame.image.load("logo.png")
pygame.display.set_icon(logoIMG)

win = pygame.display.set_mode((700,700))
win.fill((255,255,255))
pygame.draw.rect(win, (0,0,0), (47,47,604,604), 3)

surface = pygame.Surface((600,600))

#--------------------------------------------------------

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

def highlight(y,x):
    redraw()
    pygame.draw.rect(surface, (255,0,0), (x*(600/9), y*(600/9), (600/9), (600/9) ), 3)
    win.blit(surface, (50,50))
    pygame.display.update()

def saveBoard():
    print("BOARD SAVED!!!!!!!!!!!!!")
    open('board.txt', 'w').close()
    f = open('board.txt','a')
    for line in board:
        for num in line:
            f.write("%d " %num)
        f.write("\n")
    f.close()
    pygame.quit()
    exit()

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

#--------------------------------------------------------

f = open('board.txt', 'r')
lines = f.readlines()
board = [[ int(n) for n in line.split() ] for line in lines ]
f.close()

font = pygame.font.SysFont('Calibri', 35)
text = font.render("Press Enter to Save", 1, (0,0,0))
win.blit(text, (220,5) )
text = font.render("Reset", 1, (255,255,255))
font = pygame.font.SysFont('Calibri', 45)
pygame.draw.rect(win, (80,80,80), (300,658,100,35))
win.blit(text, (305,660) )

x = 0
y = 0
redraw()
# main loop
while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key ==K_ESCAPE:
                pygame.quit()
                exit()
            if event.key == K_RETURN or event.key == K_KP_ENTER :
                saveBoard()

        if event.type == MOUSEBUTTONDOWN:
            ty,tx = pygame.mouse.get_pos()
            if ty > 300 and ty < 400 and tx > 658 and tx < 693 :
                for i in range(9):
                    for j in range(9):
                        board[i][j] = 0
                redraw()
            else:
                ty -= 50
                tx -= 50
                tx = int(tx//(600/9))
                ty = int(ty//(600/9))
                if tx < 9 and tx >= 0 and ty >= 0 and ty < 9 :
                    x, y = tx, ty
                    highlight(x,y)
                else:
                    redraw()
                
        if event.type == KEYDOWN:
            num = 0
            if event.key == K_0 or event.key == K_KP0 :
                board[x][y] = 0
            elif event.key == K_1 or event.key == K_KP1:
                num =  1
            elif event.key == K_2 or event.key == K_KP2 :
                num =  2
            elif event.key == K_3 or event.key == K_KP3 :
                num =  3
            elif event.key == K_4 or event.key == K_KP4 :
                num =  4
            elif event.key == K_5 or event.key == K_KP5 :
                num =  5
            elif event.key == K_6 or event.key == K_KP6 :
                num =  6
            elif event.key == K_7 or event.key == K_KP7 :
                num =  7
            elif event.key == K_8 or event.key == K_KP8 :
                num =  8
            elif event.key == K_9 or event.key == K_KP9 :
                num =  9

            if checkIfPlacingIsPossible(x,y,num-1) == 1 :
                board[x][y] = num
            else:
                board[x][y] = 0

            redraw()