import pygame
import random
import math
import sys

from pygame import time
from pygame import event
from pygame import display
from pygame.constants import QUIT


class Game():
    
    def __init__(self,WindowSize):

        self.Window = display.set_mode(WindowSize)
    
    def draw(self):
        pass

    def update(self):
        pass

# there might be an erroe copying and pasting here
class Ball():

    def __init__(self,game):

        self.Window = game.Window

    def update(self):
        pass

    def resetBall(self):
        pass

class paddle():

    def __init__(self,game):

        self.Window = game.Window

    def update(self):
        pass

class Brick():

    def __init__(self,game):

        self.Window = game.Window

    def draw(self):
        pass

if pygame.init() [1] != 0:
    print('error initializing Pygame')

boardSize = (1200,800)
game = Game(boardSize)
clock = time.Clock()

while True:

    for evnt in event.get():

        if evnt.type == QUIT:
            #quit()
            sys.exit()



    dt = clock.tick(60) #frame rate counter

    game.Window.fill("gray60")

    #update

    #draw

    display.update()