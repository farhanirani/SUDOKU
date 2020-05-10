import pygame
from pygame.locals import *
pygame.init()
pygame.display.set_caption("SET BOARD")
clock = pygame.time.Clock()
logoIMG = pygame.image.load("logo.png")
pygame.display.set_icon(logoIMG)

win = pygame.display.set_mode((700,700))
win.fill((255,255,255))
pygame.draw.rect(win, (0,0,0), (48,48,604,604), 3)

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
                surface.blit(text, ((j)*(600/9)+25, (i)*(600/9)+20) )
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

#--------------------------------------------------------


board = [[0 for _ in range(9)] for _ in range(9)]
font = pygame.font.SysFont('8-Bit-Madness', 45)
text = font.render("Press Enter to Save", 1, (0,0,0))
win.blit(text, (220,10) )

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
            y,x = pygame.mouse.get_pos()
            y -= 50
            x -= 50
            x = int(x//(600/9))
            y = int(y//(600/9))
            if x < 9 and x >= 0 and y >= 0 and y < 9:
                highlight(x,y)
            else:
                redraw()
                
        if event.type == KEYDOWN:
            if event.key == K_0 or event.key == K_KP0 :
                board[x][y] = 0
            elif event.key == K_1 or event.key == K_KP1:
                board[x][y] = 1
            elif event.key == K_2 or event.key == K_KP2 :
                board[x][y] = 2
            elif event.key == K_3 or event.key == K_KP3 :
                board[x][y] = 3
            elif event.key == K_4 or event.key == K_KP4 :
                board[x][y] = 4
            elif event.key == K_5 or event.key == K_KP5 :
                board[x][y] = 5
            elif event.key == K_6 or event.key == K_KP6 :
                board[x][y] = 6
            elif event.key == K_7 or event.key == K_KP7 :
                board[x][y] = 7
            elif event.key == K_8 or event.key == K_KP8 :
                board[x][y] = 8
            elif event.key == K_9 or event.key == K_KP9 :
                board[x][y] = 9
            redraw()