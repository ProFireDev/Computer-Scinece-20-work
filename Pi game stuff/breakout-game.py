import pygame
import random
import math
import sys

from pygame import time
from pygame import draw
from pygame import event
from pygame import display
from pygame.constants import K_LEFT, K_RIGHT, QUIT
from pygame import key


class Game():
    
    def __init__(self,WindowSize):

        self.Window = display.set_mode(WindowSize)
    
    def draw(self):
        pass

    def update(self):
        pass

################___missing some stuff here____###############################
# still broken, watch / read later

# there might be an erroe copying and pasting here
class Ball():

    colour = "red"
    radius = 15
    targetVelocity = 0.5 #change number for ball speed

#logic for the ball bouncing off the padel and moving around

    def __init__(self,game):

        self.Window = game.Window
        self.resetBall()
        self.maxLeft = self.radius
        self.maxRight = self.Window.get_width() - self.radius
        self.maxHight = 100 + self.radius

    def draw(self):
        draw.circle(self.Window,self.colour,(self.x,self.y),self.radius)

    def update(self,dt):
        deltaX = self.velX * dt
        deltaY =self.velY *dt

        self.X += deltaX

        if self.X < self.maxLeft:
            self.X = self.maxLeft + (self.maxLeft - self.X)
            self.velX *= -1
        
        if self.X < self.maxRight:
            self.X = self.maxRight + (self.maxRight - self.X)
            self.velX *= -1
        
        self.y +- deltaY
        
        if self.y < self.maxHight:
            self.y = 2*self.maxHight - self.y
            self.velY *= -1

        if self.y > 800:
            self.resetBall()


    def resetBall(self):
        self.x = 600
        self.y = 600

        angle = random.uniform(0.5,math.pi-0.5) # angle in radians not digrees - using math lib

        self.velX = self.targetVelocity * math.cos*angle
        self.velY = -self.targetVelocity * math.cos*angle
class paddle():

    def __init__(self,game):

        self.Window = game.Window

    def update(self,dt,keys):
        if keys[K_LEFT]:
            velocity = -0.8
        elif keys[K_RIGHT]:
             velocity = 0.8
        else:
             velocity = 0
            
        delta =  velocity*dt
        self.x += delta

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

#start of the game components being called

    dt = clock.tick(60) #frame rate counter
    keys = key.get_pressed()

    game.Window.fill("gray60")

    game.update(dt)
    game.draw()
    display.update()