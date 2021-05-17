import pygame
import random
import math
import sys
 # that amazing moment when you somehow manage to break everything for no reason at all
 # but then you realizse that its just your own pure stupidity why its not working
 ## fix later - installed a temp fix, but game currently will not rn
 #check back on #2 to review code around Ln 19 and 100
from pygame import time
from pygame import draw
from pygame import event
from pygame import display
from pygame.constants import K_LEFT, K_RIGHT, K_x, QUIT
from pygame import key


class Game():
    
    def __init__(self,WindowSize):

        self.Window = display.set_mode(WindowSize)
    
    def draw(self):
        pass

    def update(self):
        pass

    def bounce(self,Object):

        if Object.x <= Object.x + Object.length:
            self.Ball.velY *= -1
        elif Object.y <= self.Ball.y <= Object.y + Object.width:


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
        self.x =540
        self.y = 540
        #self.maxRight =
        #self.rect.update(self.x,self.y,self.length,self.width)
    def update(self,dt,keys):
        if keys[K_LEFT]:
            velocity = -0.8
        elif keys[K_RIGHT]:
             velocity = 0.8
        else:
             velocity = 0
            
        delta =  velocity*dt
        self.x += delta
        #self.rect.update(self.x,self.y,self.length,self.width)
class Brick():


# fix bounce function aswell as add in collide rect from pi game here
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


    # fix ball pos locking - very broken

    # add in smoother movements -- its no where near close to being "smooth"




    # it should be working now, but its not 🤔 i am confused now -- somethning to do
    # with the missing windows class - it runs sometimes, but not
