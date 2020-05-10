import os
import z_sudoku_backtracking_visualized

os.system("python z_solve_board_quick.py")

f = open('board.txt', 'r')
lines = f.readlines()
board = [[ int(n) for n in line.split() ] for line in lines ]
f.close()
f = open('board-solved.txt', 'r')
lines = f.readlines()
solvedboard = [[ int(n) for n in line.split() ] for line in lines ]
f.close()

fixed = [[0 for _ in range(9)] for _ in range(9)]
for i in range(9):
    for j in range(9):
        if board[i][j] != 0:
            fixed[i][j] = 1
            


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
                surface.blit(text, ((j)*(600/9)+25, (i)*(600/9)+20) )
    win.blit(surface, (50,50))
    pygame.display.update()

def redrawtemp(): # only for drawing the board and numbers after success/failure flash
    for j in range(9):
        for i in range(9):
            if board[i][j] != 0: 
                text = font.render(str(board[i][j]), 1, (0,0,0))
                surface.blit(text, ((j)*(600/9)+25, (i)*(600/9)+20) )
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
font = pygame.font.SysFont('8-Bit-Madness', 45)
text = font.render("SUDOKU", 1, (0,0,0))
win.blit(text, (300,10) )
redraw()


while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()
            if event.key == K_s:
                fun()
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