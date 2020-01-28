import pygame
import sys

from pygame.locals import * 
from random import randint

import random
import time

pygame.init()
pygame.display.init()

#human board
board_mine = []
#the places where enemy hides ships
board_enemy = []
#keep track of my choice of hit
hit_board = []
#fill the arrays with o
for x in range(10):
    board_mine.append(["O"] * 10)

for x in range(10):
    hit_board.append(["O"] * 10)

for x in range(10):
    board_enemy.append(["O"] * 10)
#global variables
score_h = 0
score_a = 0
intro = True
turn = 1
ai_b = True
LBLUE = (66,134,244)
WHITE = (255, 255, 255)
BLACK = (0,0,0)
LIME = (0,255,0)
GREY = (128,128,128)
RED = (255,0,0)
#fonts for text
largeText = pygame.font.Font('freesansbold.ttf',110)
smallText = pygame.font.Font('freesansbold.ttf',25)
stText = pygame.font.Font('freesansbold.ttf',18)
tinyText = pygame.font.Font('freesansbold.ttf',10)
#colors of objects
BACKGROUND = LBLUE
gameDisplay = pygame.display.set_mode((800,600))
#load images
hal = pygame.image.load(r'Hal.PNG')
player = pygame.image.load(r'player.png')
background_image = pygame.image.load("Background.jpg").convert()
background_image_grid = pygame.image.load("background of grid.jpg").convert()
background_image_ai = pygame.image.load("background of AI firing .jpg").convert()
background_image_h = pygame.image.load("background human firing.jpg").convert()
background_image_win = pygame.image.load("backround winner.jpg").convert()
background_image_lose = pygame.image.load("background loser.jpg").convert()

#Functions for the game in Alphabetical order

#function that checks if a coordinate is hit or miss
def check_hit(board,y,x):
    #hit
    if(board[y][x] == "S"):
        return 1
    elif(board[y][x] == "H" or board[y][x]== "M"):
        return 2
    else:
        return 0

#main display function used in main game loop. displays the main firing screen
def display_board():
    gameDisplay.blit(background_image_grid, [0, 0])
    pygame.draw.rect(gameDisplay, BLACK, (390, 100, 30, 105))
    pygame.draw.rect(gameDisplay, WHITE, (395, 105, 20, 20))
    pygame.draw.rect(gameDisplay, LBLUE, (395, 130, 20, 20))
    pygame.draw.rect(gameDisplay, GREY, (395, 155, 20, 20))
    pygame.draw.rect(gameDisplay, RED, (395, 180, 20, 20))
    TextSurf, TextRect = text_objects("Turn:", smallText)
    TextRect.center = ((400),(50))
    gameDisplay.blit(TextSurf, TextRect)
    global turn
    TextSurf, TextRect = text_objects(str(turn), smallText)
    TextRect.center = ((450),(50))
    gameDisplay.blit(TextSurf, TextRect)
    TextSurf, TextRect = text_objects("Legend:", smallText)
    TextRect.center = ((410),(85))
    gameDisplay.blit(TextSurf, TextRect)
    TextSurf, TextRect = text_objects("Miss", stText)
    TextRect.center = ((450),(115))
    gameDisplay.blit(TextSurf, TextRect)
    TextSurf, TextRect = text_objects("Empty", stText)
    TextRect.center = ((450),(140))
    gameDisplay.blit(TextSurf, TextRect)
    TextSurf, TextRect = text_objects("Ship", stText)
    TextRect.center = ((450),(165))
    gameDisplay.blit(TextSurf, TextRect)
    TextSurf, TextRect = text_objects("Hit", stText)
    TextRect.center = ((450),(190))
    gameDisplay.blit(TextSurf, TextRect)
    #button fire
    pygame.draw.rect(gameDisplay, BLACK, (355, 522, 90, 60))
    pygame.draw.rect(gameDisplay, RED, (360, 527, 80, 50))
    TextSurf, TextRect = text_objects("FIRE!", stText)
    TextRect.center = ((400),(552))
    gameDisplay.blit(TextSurf, TextRect)
    #display names for boards
    TextSurf, TextRect = text_objects("Hit Board:", stText)
    TextRect.center = ((177),(160))
    gameDisplay.blit(TextSurf, TextRect)
    TextSurf, TextRect = text_objects("Your Board:", stText)
    TextRect.center = ((622),(160))
    gameDisplay.blit(TextSurf, TextRect)
    #255 by 255
    MARGIN = 5
    WIDTH = 20
    HEIGHT = 20
    xcord = 65
    ycord = 190
    top_row = 65
    side_row = 1
    for x in range(10):
        TextSurf, TextRect = text_objects(str(side_row), smallText)
        TextRect.center = (xcord,ycord)
        gameDisplay.blit(TextSurf, TextRect)
        TextRect.center = (xcord + 445,ycord)
        gameDisplay.blit(TextSurf, TextRect)
        side_row = side_row + 1
        xcord= xcord + 25
    xcord = 30
    ycord = 215
    for y in range(10):
        TextSurf, TextRect = text_objects(chr(top_row), smallText)
        TextRect.center = (xcord,ycord)
        gameDisplay.blit(TextSurf, TextRect)
        TextRect.center = (xcord + 445,ycord)
        gameDisplay.blit(TextSurf, TextRect)
        ycord= ycord + 25
        top_row = top_row + 1
    #the first array
    xcord = 50
    ycord = 200
    pygame.draw.rect(gameDisplay, BLACK, (50, 200, 255, 255))
    for row in range(10):
        for column in range(10):
            color = BACKGROUND
            if hit_board[row][column] == "H":
                color = RED
            elif hit_board[row][column] == "M":
                color = WHITE
            elif hit_board[row][column] == "C":
                color = LIME
            pygame.draw.rect(gameDisplay, color,
                             ((xcord + (column * (WIDTH + MARGIN))) + MARGIN,
                              (ycord + (row * (HEIGHT + MARGIN))) + MARGIN,
                              WIDTH,
                              HEIGHT))
    xcord = 495
    ycord = 200
    #the Second array
    pygame.draw.rect(gameDisplay, BLACK, (495, 200, 255, 255))
    for row in range(10):
        for column in range(10):
            color = BACKGROUND
            if board_mine[row][column] == "S":
                color = GREY
            elif board_mine[row][column] == "H":
                color = RED
            elif board_mine[row][column] == "M":
                color = WHITE           
            pygame.draw.rect(gameDisplay, color,
                             ((xcord + (column * (WIDTH + MARGIN))) + MARGIN,
                              (ycord + (row * (HEIGHT + MARGIN))) + MARGIN,
                              WIDTH,
                              HEIGHT))

#display function for ship selection, it displays the grid
def draw_one_grid(size):
    gameDisplay.blit(background_image, (0, 0))
    MARGIN = 5
    WIDTH = 20
    HEIGHT = 20
    xcord = 285
    ycord = 160
    top_row = 65
    side_row = 1
    for x in range(10):
        TextSurf, TextRect = text_objects(str(side_row), smallText)
        TextRect.center = (xcord,ycord)
        gameDisplay.blit(TextSurf, TextRect)
        side_row = side_row + 1
        xcord= xcord + 25
    xcord = 255
    ycord = 190
    for y in range(10):
        TextSurf, TextRect = text_objects(chr(top_row), smallText)
        TextRect.center = (xcord,ycord)
        gameDisplay.blit(TextSurf, TextRect)
        ycord= ycord + 25
        top_row = top_row + 1
    pygame.draw.rect(gameDisplay, BLACK, (272, 172, 255, 255))
    xcord = 272
    ycord = 172
    for row in range(10):
        for column in range(10):
            color = BACKGROUND
            if board_mine[row][column] == "S":
                color = GREY
            pygame.draw.rect(gameDisplay, color,
                             ((xcord + (column * (WIDTH + MARGIN))) + MARGIN,
                              (ycord + (row * (HEIGHT + MARGIN))) + MARGIN,
                              WIDTH,
                              HEIGHT))
    TextSurf, TextRect = text_objects("Click two squares to place ship size " + str(size), smallText)
    TextRect.center = ((400),(100))
    gameDisplay.blit(TextSurf, TextRect)

#main function that manages the main game loop
def game_start():
    generate_seed(board_enemy)
    WIDTH = 20
    HEIGHT = 20
    MARGIN = 5
    #just the intro screen 
    title()
    pick_ship()
    #main game loop
    finish = True
    choosen = False
    currentP = True
    global turn
    global score_a
    global score_h
    global targetMode
    global shotStack
    global ai_b
    targetMode = False
    shotStack = []
    while finish:
        for event in pygame.event.get():
            if score_a == 17 or score_h == 17 or event.type == pygame.QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                if score_a == 17 or score_h == 17:
                    winner()
                pygame.time.wait(5000)
                pygame.quit()
                #note this is creates an error in Visual studio but works in a python environment
                sys.quit()
            elif event.type == MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if(pos[0]>= 50 and pos[0]<=305 and pos[1]>=200 and pos[1] <= 455 and choosen == False):
                    x = (pos[0]-50) // (WIDTH + MARGIN)
                    y = (pos[1]-200) // (HEIGHT + MARGIN)
                    if x == 10:
                        x = 9
                    if hit_board[y][x] == "O":
                        hit_board[y][x] = "C"
                        choosen = True
                    else:
                        choosen = False
                elif(pos[0]>= 355 and pos[0]<=445 and pos[1]>=522 and pos[1] <= 582 and choosen == True and currentP == True):
                    #this is the fire button
                    shot_human(board_enemy,y,x)
                    if ai_b == True:
                        shot_AI_brute(board_mine)
                    else:
                        shot_AI_hunt(board_mine)
                    choosen = False
                    turn = turn + 1
                elif choosen == True:
                    choosen = False
                    hit_board[y][x] = "O"
                elif choosen == False:
                    choosen = False                       
        display_board()
        pygame.display.update()

#function that generates all ship sizes 5,4,3,3,2
def generate_seed(board):
    generate_ship(board,5)
    generate_ship(board,4)
    generate_ship(board,3)
    generate_ship(board,3)
    generate_ship(board,2)

#function that generates positions of AI ships
def generate_ship(board, size):
    done = 0
    rand = randint(0,2)
    while(done == 0):
        done = 1
        #get a new point
        pos_C = randint(0,9)
        pos_R = randint(0,9)
        #for vertical
        if(rand == 0):
            hold = pos_R
            #check if point is good
            for x in range(size):
                if(pos_R < 10):
                    if(board[pos_R][pos_C]== "S"):
                        done = 0
                    pos_R = pos_R + 1
                if(pos_R > 9):
                    done = 0
            if(done == 1):
                pos_R = hold
                for x in range(size):
                    board[pos_R][pos_C] = "S"
                    pos_R =pos_R + 1
        else:
            hold = pos_C
            #check if point is good
            for x in range(size):
                if(pos_C < 10):
                    if(board[pos_R][pos_C]== "S"):
                        done = 0
                    pos_C = pos_C + 1
                if(pos_C > 9):
                    done = 0
            if(done == 1):
                pos_C = hold
                for x in range(size):
                    board[pos_R][pos_C] = "S"
                    pos_C = pos_C + 1

#function that manages the ship selection screen, users selects a ship
def pick_ship():
    intro = True
    done = False
    size = 5
    three = False
    pos = 0
    column = 0
    row = 0
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    WIDTH = 20
    MARGIN = 5
    HEIGHT = 20
    second = False
    while True:
        for event in pygame.event.get():
            if size == 1:
                done = False
                return
            if done == True:
                break
            elif event.type == MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if intro == True:
                    global ai_b
                    if pos[0] <= 490 and pos[0] >= 310 and pos[1] >= 225 and pos [1] <= 275:
                        ai_b = True
                        draw_one_grid(size) 
                        intro = False
                    elif pos[0] <= 490 and pos[0] >= 310 and pos[1] >= 280 and pos [1] <= 330:
                        ai_b = False
                        draw_one_grid(size) 
                        intro = False
                elif intro != True:
                    if pos[0] <= 527 and pos[0] >= 272 and pos[1] >= 172 and pos [1] <= 427 and second == True:
                         x2 = (pos[0]-272) // (WIDTH + MARGIN)
                         y2 = (pos[1]-172) // (HEIGHT + MARGIN)
                         if x2 <= 9 and x2 >= 0 and y2 >= 0 and y2 <=9: 
                            if board_mine[y2][x2]=="S":
                                 second = False
                                 board_mine[y1][x1]="O"
                            elif x1 + size-1 == x2 and y1 == y2:
                                 for x in range (1,size):
                                     if(board_mine[y1][x1+x] != "S"):
                                        board_mine[y1][x1+x] = "S"
                                     else:
                                        counter = x+1
                                        for i in range (counter):
                                             board_mine[y1][x1+x] = "O"
                                        second = False
                                        break
                                 second = False
                                 if size == 3 and three == False:
                                     three = True
                                 else:
                                     size= size -1
                            elif x1 - (size-1) == x2 and y1 == y2:
                                for x in range (1,size):
                                    if(board_mine[y1][x1-x] != "S"):
                                        board_mine[y1][x1-x] = "S"
                                    else:
                                        counter = x+1
                                        for i in range (counter):
                                            board_mine[y1][x1-x] = "O"
                                        second = False
                                        break
                                second = False
                                if size == 3 and three == False:
                                    three = True
                                else:
                                    size = size - 1
                            elif y1 + size-1 == y2 and x1 == x2:
                                for y in range (1,size):
                                    if(board_mine[y1+y][x1] != "S"):
                                        board_mine[y1+y][x1] = "S"
                                    else:
                                        counter = y+1
                                        for i in range (counter):
                                            board_mine[y1+y][x1] = "O"
                                        second = False
                                        break
                                second = False
                                if size == 3 and three == False:
                                    three = True
                                else:
                                    size = size - 1
                            elif y1 - (size-1) == y2 and x1 == x2:
                                for y in range (1,size):
                                    if(board_mine[y1-y][x1] != "S"):
                                        board_mine[y1-y][x1] = "S"
                                    else:
                                        counter = y+1
                                        for i in range (counter):
                                            board_mine[y1-y][x1] = "O"
                                        second = False
                                        break
                                second = False
                                if size == 3 and three == False:
                                    three = True
                                else:
                                    size = size - 1
                    elif pos[0] <= 527 and pos[0] >= 272 and pos[1] >= 172 and pos [1] <= 427:
                        x1 = (pos[0]-272) // (WIDTH + MARGIN)
                        y1 = (pos[1]-172) // (HEIGHT + MARGIN)
                        if x1 <= 9 and x1 >= 0 and y1 >= 0 and y1 <=9:
                            if board_mine[y1][x1]=="O":
                                board_mine[y1][x1] = "S"
                                second = True
                            else:
                                second = False
                    elif second == True:
                        second = False
                        board_mine[y1][x1] = "O"
                    draw_one_grid(size)            
            pygame.display.update()

#----------------------Ai functions (below) ----------------------- 
#shot function for AI. This uses brute force to decide AI firing
def shot_AI_brute(board):
    global score_a
    same_spot = 1
    while(same_spot == 1):
        ran_x = randint(0,9)
        ran_y = randint(0,9)
        check = check_hit(board, ran_y, ran_x)
        if(check==2):
            same_spot = 1
        else:
            shot_screen_A(check,ran_y,ran_x)
            same_spot = 0
            if(check == 1):
                board[ran_y][ran_x] = "H"
                score_a = score_a + 1
            else:
                board[ran_y][ran_x] = "M"    

#shot function for AI. This uses a heuristic algorithm.(hunt and target)
def shot_AI_hunt(board):
    global score_a
    global targetMode
    global shotStack
    same_spot = 1
    #ran_x = randint(0,9)
    #ran_y = randint(0,9)
    if (targetMode == False):
        while(same_spot == 1):
            ran_x = randint(0,9)
            ran_y = randint(0,9)
            check = check_hit(board, ran_y, ran_x)
            #check1 = check_hit(board, ran_y-1, ran_x)
            #check2 = check_hit(board, ran_y+1, ran_x)
            #check3 = check_hit(board, ran_y, ran_x-1)
            #check4 = check_hit(board, ran_y, ran_x+1)
            if(check==2):
                same_spot = 1
            else:
                shot_screen_A(check,ran_y,ran_x)
                same_spot = 0
                if(check == 1):
                    board[ran_y][ran_x] = "H"
                    score_a = score_a + 1
                    targetMode = True
                    if (ran_y-1 >= 0):# and (check1 != 2)):
                        check1 = check_hit(board, ran_y-1, ran_x)
                        if (check1 != 2):
                            shotStack.append([ran_x,ran_y-1])
                            print("1st append ok")
                    else:
                        continue
                    if (ran_y+1 <= 9):# and (check2 != 2)):
                        check2 = check_hit(board, ran_y+1, ran_x)
                        if (check2 != 2):
                            shotStack.append([ran_x,ran_y+1])
                            print("2nd append ok")
                    else:
                        continue
                    if (ran_x-1 >= 0):#  and (check3 != 2)):
                        check3 = check_hit(board, ran_y, ran_x-1)
                        if (check3 != 2):
                            shotStack.append([ran_x-1,ran_y])
                            print("3rd append ok")
                    else:
                        continue
                    if (ran_x+1 <= 9):# and (check4 != 2)):
                        check4 = check_hit(board, ran_y, ran_x+1)
                        if (check4 != 2):
                            shotStack.append([ran_x+1,ran_y])
                            print("4th append ok")
                    else:
                        break
                else:
                    board[ran_y][ran_x] = "M"
                    print("miss ok")
                    print("targetMode OFF")
    else:
        print(shotStack)
        print("targetMode ON")
        same_spot = 1
        x, y = shotStack.pop()
        print("pop is ok")
        while(same_spot == 1):
            check = check_hit(board, y, x)
            print("check is ok")
            shot_screen_A(check, y, x)
            same_spot = 0
            #check1 = check_hit(board, y-1, x)
            #check2 = check_hit(board, y+1, x)
            #check3 = check_hit(board, y, x-1)
            #check4 = check_hit(board, y, x+1)
            if(check == 1):
                board[y][x] = "H"
                score_a = score_a + 1
                if (y-1 >= 0): #and (check1 != 2)):
                    check1 = check_hit(board, y-1, x)
                    if (check1 != 2):
                        shotStack.append([x,y-1])
                        print("1st append ok")
                else:
                    continue
                if (y+1 <= 9):# and (check2 != 2)):
                    check2 = check_hit(board, y+1, x)
                    if( check2 != 2):
                        shotStack.append([x,y+1])
                        print("2nd append ok")
                else:
                    continue
                if (x-1 >= 0):# and (check3 != 2)):
                    check3 = check_hit(board, y, x-1)
                    if (check3 != 2):
                        shotStack.append([x-1,y])
                        print("3rd append ok")
                else:
                    continue
                if (x+1 <= 9):# and (check4 != 2)):
                    check4 = check_hit(board, y, x+1)
                    if (check4 != 2):
                        shotStack.append([x+1,y])
                        print("4th append ok")
                else:
                    break
            else:
                board[y][x] = "M"
                print("miss ok")
        if shotStack == []:
            targetMode = False
#----------------------Ai functions (above) ----------------------- 

#function that handles the human firing
def shot_human(board, y, x):
    global score_h
    check = check_hit(board,y,x)
    shot_screen_H(check,y,x)
    if(check == 1):
        hit_board[y][x] = "H"
        score_h = score_h + 1
    else:
        hit_board[y][x] = "M"

#display screen for when AI fires
def shot_screen_A(hit,y,x):
    gameDisplay.blit(background_image_ai, (0, 0))
    TextSurf, TextRect = text_objects_red("AI Turn:", largeText)
    TextRect.center = ((400),(100))
    gameDisplay.blit(TextSurf, TextRect)
    y= y + 65
    x=x+1
    pygame.draw.rect(gameDisplay, BLACK, (260, 180, 279, 36))
    pygame.draw.rect(gameDisplay, LBLUE, (265, 185, 269, 26))
    TextSurf, TextRect = text_objects("X-cord: " + str(x), smallText)
    TextRect.center = ((325),(200))
    gameDisplay.blit(TextSurf, TextRect)
    TextSurf, TextRect = text_objects("Y-cord: " + chr(y), smallText)
    TextRect.center = ((475),(200))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.draw.rect(gameDisplay, BLACK, (290, 230, 217, 36))
    pygame.draw.rect(gameDisplay, LBLUE, (295, 235, 207, 26))
    if hit == 1:
        TextSurf, TextRect = text_objects_red("Result: HIT!", smallText)
        TextRect.center = ((400),(250))
        gameDisplay.blit(TextSurf, TextRect)
    else:
        TextSurf, TextRect = text_objects_red("Result: MISSED", smallText)
        TextRect.center = ((400),(250))
        gameDisplay.blit(TextSurf, TextRect)

    gameDisplay.blit(hal, (350, 300))
    pygame.display.update()
    pygame.time.wait(1000)

#display screen function for when Human fires
def shot_screen_H(hit,y,x):
    gameDisplay.blit(background_image_h, (0, 0))
    TextSurf, TextRect = text_objects_red("HUMAN Turn:", largeText)
    TextRect.center = ((400),(100))
    gameDisplay.blit(TextSurf, TextRect)
    y= y + 65
    x= x+1
    pygame.draw.rect(gameDisplay, BLACK, (260, 180, 279, 36))
    pygame.draw.rect(gameDisplay, LBLUE, (265, 185, 269, 26))
    TextSurf, TextRect = text_objects("X-cord: " + str(x), smallText)
    TextRect.center = ((325),(200))
    gameDisplay.blit(TextSurf, TextRect)
    TextSurf, TextRect = text_objects("Y-cord: " + chr(y), smallText)
    TextRect.center = ((475),(200))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.draw.rect(gameDisplay, BLACK, (290, 230, 217, 36))
    pygame.draw.rect(gameDisplay, LBLUE, (295, 235, 207, 26))
    if hit == 1:
        TextSurf, TextRect = text_objects_red("Result: HIT!", smallText)
        TextRect.center = ((400),(250))
        gameDisplay.blit(TextSurf, TextRect)
    else:
        TextSurf, TextRect = text_objects_red("Result: MISSED", smallText)
        TextRect.center = ((400),(250))
        gameDisplay.blit(TextSurf, TextRect)
    gameDisplay.blit(player, (272, 272))
    pygame.display.update()
    pygame.time.wait(1000)

#functions that manipulates the color of the text
def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()

def text_objects_blue(text, font):
    textSurface = font.render(text, True, LBLUE)
    return textSurface, textSurface.get_rect()

def text_objects_orange(text, font):
    textSurface = font.render(text, True, (255,97,3))
    return textSurface, textSurface.get_rect()

def text_objects_red(text, font):
    textSurface = font.render(text, True, RED)
    return textSurface, textSurface.get_rect()

#display the title screen using pygame
def title():
    gameDisplay.blit(background_image, [0, 0])
    pygame.display.set_caption("Battleship")
    TextSurf, TextRect = text_objects("Battleship", largeText)
    TextRect.center = ((400),(150))
    gameDisplay.blit(TextSurf, TextRect)
    TextSurf, TextRect = text_objects("Click an Algorithm to Start", smallText)
    TextRect.center = ((400),(450))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.draw.rect(gameDisplay, BLACK, (310, 225, 180, 50))
    pygame.draw.rect(gameDisplay, LBLUE, (315, 230, 170, 40))
    TextSurf, TextRect = text_objects("Brute-Force", smallText)
    TextRect.center = ((400),(252))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.draw.rect(gameDisplay, BLACK, (310, 280, 180, 50))
    pygame.draw.rect(gameDisplay, LBLUE, (315, 285, 170, 40))
    TextSurf, TextRect = text_objects("Heuristic", smallText)
    TextRect.center = ((400),(307))
    gameDisplay.blit(TextSurf, TextRect)
    TextSurf, TextRect = text_objects("(Press ESC to Exit Game)", tinyText)
    TextRect.center = ((400),(470))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

#display screen for winner
def winner():
    gameDisplay.fill(BACKGROUND)
    
    global score_a
    global score_h
    if score_a == 17:
        gameDisplay.blit(background_image_lose, (0, 0))
        TextSurf, TextRect = text_objects("WINNER:", largeText)
        TextRect.center = ((400),(100))
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("AI", largeText)
        TextRect.center = ((400),(200))
        gameDisplay.blit(TextSurf, TextRect) 
        image = pygame.image.load(r'Hal.PNG')
        gameDisplay.blit(image, (350, 300))
    else:
        gameDisplay.blit(background_image_win, (0, 0))
        TextSurf, TextRect = text_objects("WINNER:", largeText)
        TextRect.center = ((400),(100))
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("HUMAN", largeText)
        TextRect.center = ((400),(200))
        gameDisplay.blit(TextSurf, TextRect) 
        image = pygame.image.load(r'player.png')
        gameDisplay.blit(image, (272, 272))
    pygame.display.update()

#call game_start() to start the game
game_start()
