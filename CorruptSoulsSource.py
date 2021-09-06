import pygame
import random
import time
from pygame.locals import *
pygame.init()
import FunctionsToUse

last_score = 0

clock = pygame.time.Clock()
screen = pygame.display.set_mode((700,700))
pygame.display.set_caption("Corrupt Souls v0.1")

class PointyStar:
    def __init__(self, speedx, speedy, xpos, ypos):
        self.speedx = speedx
        self.speedy = speedy
        self.ypos = ypos
        self.xpos = xpos
    def tick(self):
        self.ypos = self.ypos + self.speedy
        self.xpos = self.xpos + self.speedx

class Enemy:
    def __init__(self):
        self.health = random.randint(1,5)
        self.speed = random.uniform(0, 0.45)
        self.active = True
        self.xpos = random.randint(-310,310)
        self.ypos = random.randint(-310,310)
        self.xdirection = "none"
    def take_damage(self, damage_value):
        self.health = self.health - damage_value
        if self.health <= 0:
            self.active = False
    def tick(self):
        if random.randint(1,10000) == 2:
            self.speed = self.speed - 0.01
        if self.active == True:
            if self.xpos > 325:
                self.spos = self.xpos - self.speed
            if self.xpos < 325:
                self.xpos = self.xpos + self.speed
            if self.ypos > 325:
                self.ypos = self.ypos - self.speed
            if self.ypos < 325:
                self.ypos = self.ypos + self.speed
            elif self.xdirection != "none":
                if self.xdirection == "left":
                    self.xpos = self.xpos - self.speed
                if self.xdirection == "right":
                    self.xpos = self.xpos + self.speed
                if self.xpos >= 300 or self.xpos <= -300:
                    self.xdirection = "none"
            else:
                chance = random.randint(1,4)
                if chance == 2:
                    self.xdirection = "right"
                else:
                    self.xdirection = "left"
        if random.randint(1,10000) == 2:
            self.speed = self.speed + 0.01

backx = 5
backy = 5
up = False
down = False
right = False
left = False
started = False
score = 0
game_over = False
can_die = False

enemies = []
pointystars = []

for i in range(1, 5, 1):
    enemies.append(Enemy())

character = pygame.image.load("scrolling_test_character.png")
character = pygame.transform.scale(character, (50,50)).convert()

background = pygame.image.load("scrolling_image_background.png")
background = pygame.transform.scale(background, (690, 690)).convert()

enemy = pygame.image.load("scrolling_test_enemy.png")
enemy = pygame.transform.scale(enemy, (50,50)).convert()

pointystar = pygame.image.load("pointy_throable_object.png")
pointystar = pygame.transform.scale(pointystar, (25,25)).convert()

titlescreen = pygame.image.load("titlescreen.png")
titlescreen = pygame.transform.scale(titlescreen, (690, 690)).convert()

play_button = pygame.image.load("play_button.png")
play_button = pygame.transform.scale(play_button, (90,60)).convert()

game_over_screen = pygame.image.load("game_over_screen.png")
game_over_screen = pygame.transform.scale(game_over_screen, (690, 690))

icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

while True:
    clock.tick(500)
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                up = True
            if event.key == K_DOWN:
                down = True
            if event.key == K_RIGHT:
                right = True
            if event.key == K_LEFT:
                left = True
        if event.type == KEYUP:
            if event.key == K_UP:
                up = False
            if event.key == K_DOWN:
                down = False
            if event.key == K_RIGHT:
                right = False
            if event.key == K_LEFT:
                left = False
        if event.type == MOUSEBUTTONDOWN:
            mousepos = event.pos
            if FunctionsToUse.touching(mousepos[0], mousepos[1], 310, 610, 90, 60) == True and started == False:
                started = True
                can_die = False
            if game_over == True:
                game_over = False
                screen.fill(FunctionsToUse.BLUE)
                started = True
                backx = 5
                backy = 5
                score = 0
                enemies = []
                pointystars = []
    if started == True and game_over == False:
        if random.randint(1,300) == 2:
            can_die = True
        score = score + 0.001
        if len(enemies) > 25:
            v = 0
            for enemyhumanoid in enemies:
                if v >= 25:
                    enemies = []
                    for i in range(1,5,1):
                        enemies.append(Enemy())
                v = v + 1
        if random.randint(1,10000) == 2 and len(enemies) < 24:
                enemies.append(Enemy())
        if random.randint(1,1000) == 2:
            starxpos = random.randint(-510, 510)
            starypos = random.randint(-510, 510)
            if FunctionsToUse.touching(starxpos, starypos, 325, 325, 50, 50) == False:
                pointystars.append(PointyStar(random.uniform(0.01,0.35), random.uniform(0.01,0.35), starxpos, starypos))
        if up == True and backy < 319:
            backy = backy + 0.5
            down = False
            for enemyhumanoid in enemies:
                enemyhumanoid.ypos = enemyhumanoid.ypos + 0.5
            for enemyhumanoid in pointystars:
                enemyhumanoid.ypos = enemyhumanoid.ypos + 0.5
        if down == True and backy > -312:
            backy = backy - 0.5
            up = False
            for enemyhumanoid in enemies:
                enemyhumanoid.ypos = enemyhumanoid.ypos - 0.5
            for enemyhumanoid in pointystars:
                enemyhumanoid.ypos = enemyhumanoid.ypos - 0.5
        if right == True and backx > -312:
            backx = backx - 0.5
            left = False
            for enemyhumanoid in enemies:
                enemyhumanoid.xpos = enemyhumanoid.xpos - 0.5
            for enemyhumanoid in pointystars:
                enemyhumanoid.ypos = enemyhumanoid.xpos - 0.5
        if left == True and backx < 319:
            backx = backx + 0.5
            right = False
            for enemyhumanoid in enemies:
                enemyhumanoid.xpos = enemyhumanoid.xpos + 0.5
            for enemyhumanoid in pointystars:
                enemyhumanoid.ypos = enemyhumanoid.xpos + 0.5
        for enemyhumanoid in enemies:
            enemyhumanoid.tick()
            if FunctionsToUse.touching(325, 325, int(enemyhumanoid.xpos), int(enemyhumanoid.ypos), 50, 50) == True and can_die == True:
                print("touched enemy")
                pygame.display.update()
                time.sleep(2)
                enemies = []
                pointystars = []
                started = False
                last_score = score
                score = 0
                for i in range(1, 5, 1):
                    enemies.append(Enemy())
            for starobj in pointystars:
                if FunctionsToUse.touching(starobj.xpos, starobj.ypos, int(enemyhumanoid.xpos), int(enemyhumanoid.ypos), 50, 50) == True:
                    print("star touched enemy")
                    enemies.remove(enemyhumanoid)
                    pointystars.remove(starobj)
            screen.fill(FunctionsToUse.BLUE)
            screen.blit(background, (backx,backy))
            screen.blit(character, (325,325))
        for starobj in pointystars:
            screen.blit(pointystar, (starobj.xpos,starobj.ypos))
            starobj.tick()
            if FunctionsToUse.touching(325, 325, int(starobj.xpos), int(starobj.ypos), 25, 25) == True and can_die == True:
                print("touched star")
                pygame.display.update()
                time.sleep(2)
                enemies = []
                pointystars = []
                started = False
                last_score = score
                score = 0
                for i in range(1, 5, 1):
                    enemies.append(Enemy())
        for enemypos in enemies:
            screen.blit(enemy,(enemypos.xpos, enemypos.ypos))
    if started == False:
        screen.blit(titlescreen, (5,5))
        screen.blit(play_button, (310,610))
        FunctionsToUse.show_text(str(int(last_score)), 116, 667, FunctionsToUse.GREEN, 20, screen)
        pass
    if game_over == True:
        screen.fill(FunctionsToUse.BLACK)
        screen.blit(game_over_screen, (5,5))
        FunctionsToUse.show_text(str(int(score)), 320, 380, FunctionsToUse.BLACK, 65, screen)
        can_die = False
    pygame.display.update()