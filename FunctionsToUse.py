import pygame
from pygame.event import pump
from pygame.locals import *

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)
PURPLE = (102, 0, 204)
BROWN = (139,69,19)
COLORS = [RED, GREEN, BLUE, WHITE, BLACK, PURPLE, BROWN]
GOLD = (255,215,0)
pygame.init()

#touching - checks for touch
def touching(obj1x,obj1y,obj2x,obj2y,obj2length, obj2width):
    if obj1x in range(obj2x, obj2x + obj2length - 1) and obj1y in range(obj2y, obj2y + obj2length - 1):
        return True
    if obj1x in range(obj2x, obj2x + obj2width - 1) and obj1y in range(obj2y, obj2y + obj2width + 1):
        return True
    else:
        return False

#show_text - displays pygame text
def show_text(msg, x, y, color, size, screen):
        fontobj= pygame.font.SysFont("freesans", size)
        msgobj = fontobj.render(msg,False,color)
        screen.blit(msgobj,(x, y))