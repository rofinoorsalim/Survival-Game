#Created by RofiGanteng
#Idea by RofiGanteng
#icon downloaded from flaticon.com

import pygame
import random
import math
import sys

from pygame import mixer
clock = pygame.time.Clock()
pygame.init()

#Screen window
screen = pygame.display.set_mode((800,600))
#tittle and icon
pygame.display.set_caption("SURVIVAL")
logo = pygame.image.load("icon.png")
pygame.display.set_icon(logo)


#background sound
mixer.music.load("background.wav")
mixer.music.play(-1)

#player
playerimg = pygame.image.load("casey.png")
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

#Item
weaponimg = pygame.image.load("apple.png")
weaponX = random.randint(10,650)
weaponY = random.randint(200,550)
weapon_state = "ready"

#play
playimg = pygame.image.load("play.png")
playX = 370
playY = 480

#Comet
cometimg = []
cometX = []
cometY = []
cometY_change = []
num_of_comet = 3
c_change = 1

for i in range(num_of_comet) :
    cometimg.append(pygame.image.load("comet.png"))
    cometX.append(random.randint(50,700))
    cometY.append(random.randint(-100,0))
    cometY_change.append(40)

#Game over text
over_font = pygame.font.Font("freesansbold.ttf", 64)
gameO = False

#Credit
credit_font = pygame.font.Font("freesansbold.ttf", 16)
creX = 600
creY = 15

#High score
high_value = 0
highX = 10
highY = 90

#Score
score_value = 0 
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 50

#Score
level_value = 1
levelX = 10
levelY = 10

#taken
takeX = 370
takeY = 480

def game_over_text() :
    over_text = over_font.render("GAME OVER",True, (255,0,0))
    screen.blit(over_text, (200, 250))

def taken(x,y) :
    taken = font.render("Item collected",True, (0,0,0))
    screen.blit(taken, (x, y))

def credit(x,y) :
    credit = credit_font.render("Created by RofiGanteng",True, (255,0,0))
    screen.blit(credit, (x, y))

def show_score(x,y) :
    score = font.render("Score : " +str(score_value),True, (255,99,71))
    screen.blit(score, (x, y))

def level(x,y) :
    level = font.render("LEVEL " +str(level_value),True, (255,0,0))
    screen.blit(level, (x, y))

def high(x,y) :
    high = font.render("Highscore : " +str(high_value),True, (255,99,71))
    screen.blit(high, (x, y))

def play(x,y) :
    screen.blit(playimg,(x,y))

def player(x,y) :
    screen.blit(playerimg,(x,y))

def comet(x,y,i) :
    screen.blit(cometimg[i],(x,y))

def item(x,y,) :
    screen.blit(weaponimg,(x,y))

def iscollision(playerX,playerY,weaponX,weaponY):
    distance = math.sqrt((math.pow(playerX-weaponX+15,2)) + (math.pow(playerY-weaponY+15,2)))
    if distance < 35  and weapon_state == "pressed":
        return True
    else :
        return False

#Game loop
running = True
while running : 
    #RGB
    screen.fill((34,139,34))

    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT :
                playerX_change = -6
            if event.key == pygame.K_RIGHT :
                playerX_change = 6
            if event.key == pygame.K_UP :
                playerY_change = -6
            if event.key == pygame.K_DOWN :
                playerY_change = 6
            if event.key == pygame.K_SPACE :
                distances = math.sqrt((math.pow(playerX-weaponX+15,2)) + (math.pow(playerY-weaponY+15,2)))
                if weapon_state == "ready" and distances < 35:
                    weapon_state = "pressed"
                    iscollision(playerX,playerY,weaponX,weaponY)
                    
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerX_change = 0
                playerY_change = 0


    #collision  
    collision = iscollision(playerX,playerY,weaponX,weaponY)
    if collision :
        collision_sound = mixer.Sound("point.wav")
        collision_sound.play()
        weapon_state = "ready"
        score_value += 1
        weaponX = random.randint(0,650)
        weaponY = random.randint(200,550)
    item(weaponX, weaponY)
    # taken(takeX,takeY)

    playerX += playerX_change
    playerY += playerY_change
    if playerX <= 0 :
        playerX = 0
    elif playerX >= 736 :
        playerX = 736
    elif playerY <= 0 :
        playerY = 0
    elif playerY >= 536 :
        playerY = 536

    for i in range(num_of_comet) :
        distances = math.sqrt((math.pow(cometX[i] - playerX,2)) + (math.pow(cometY[i] - playerY,2)))
        if distances < 27 :
            for j in range(num_of_comet)    :
                collision_sound = mixer.Sound("explosion.wav")
                collision_sound.play()
                gameO = True
                playerX = 370
                playerY = 480
                score_value = 0
                level_value = 1 
                break
        if cometY[i] <= 600 :
            comet(cometX[i], cometY[i], i)
            cometY_change[i] = 5
            
            if score_value >= 10 and score_value < 20:
                # levels_sound = mixer.Sound("level.wav")
                # levels_sound.play()
                level_value = 2
                cometY_change[i] += 2
            elif score_value >= 20  and score_value < 30:
                # level_sound.play()
                level_value = 3
                cometY_change[i] += 3
            elif score_value >= 30 and score_value < 40:
                # level_sound.play()
                level_value = 4
                cometY_change[i] += 4
            elif score_value >= 40 and score_value < 50 :
                # level_sound.play()
                level_value = 5
                cometY_change[i] += 5
            elif score_value >= 50 :
                # level_sound.play() 
                level_value = "max"
                cometY_change[i] += 6
            cometY[i] += cometY_change[i]

        if cometY[i] > 600 :
            cometX[i] = random.randint(50,700)
            cometY[i] = random.randint(-100,0)
            comet(cometX[i],cometY[i],i)

        if score_value > high_value :
            high_value = score_value
        
    player(playerX,playerY)
    credit(creX,creY)
    level(levelX,levelY)
    show_score(textX,textY)
    high(highX,highY)
    pygame.display.update()
    clock.tick(80)