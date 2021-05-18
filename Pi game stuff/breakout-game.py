from pygame import Rect, display, draw, event, init, key, rect, time
from pygame.constants import K_LEFT, K_RIGHT, QUIT
#^ it should just be covered by *
#ignore warnings in editor, they are wrong, just added thease in to get rid of them, cuz they are annoying -
# make an issue on the github for the error lesnse about it 

#from pygame import *
import random
import math
import sys

class Game():

    def __init__(self,WindowSize):
        self.Window = display.set_mode(WindowSize)

        self.Ball = Ball(self)
        self.Paddle = Paddle(self)

        self.Bricks = []
        for x in range(10,1210,100):
            for y in range(110,460,50):
                self.Bricks.append(Brick(self,x,y))

    def bounce(self,Object):

        if Object.x <= self.Ball.x <= Object.x + Object.length:
            self.Ball.velY *= -1
        elif Object.y <= self.Ball.y <= Object.y + Object.width:
            self.Ball.velX *= -1
        else:
            vx = math.copysign(self.Ball.velY,-self.Ball.velX)
            vy = math.copysign(self.Ball.velX,-self.Ball.velY)
            self.Ball.velX = vx
            self.Ball.velY = vy

    def draw(self):
        self.Ball.draw()
        self.Paddle.draw()
        for brick in self.Bricks:
            brick.draw()

    def update(self,dt,keys):
        self.Ball.update(dt)
        self.Paddle.update(dt,keys)

        if self.Ball.rect.colliderect(self.Paddle.rect):
            self.bounce(self.Paddle)

        for brick in self.Bricks:
            if self.Ball.rect.colliderect(brick.rect):
                self.bounce(brick)
                self.Bricks.remove(brick)
                break

class Ball():

    colour = "red"
    radius = 15
    targetVelocity = 0.5

    def __init__(self,game):
        self.Window = game.Window
        self.resetBall()
        self.maxLeft = self.radius
        self.maxRight = self.Window.get_width() - self.radius
        self.maxUp = 100 + self.radius

    def draw(self):
        draw.circle(self.Window,self.colour,(self.x,self.y),self.radius)

    def update(self,dt):
        deltax = self.velX * dt
        deltay = self.velY * dt

        self.x += deltax

        if self.x < self.maxLeft:
            self.x = 2*self.maxLeft - self.x
            self.velX *= -1

        if self.x > self.maxRight:
            self.x = 2*self.maxRight - self.x
            self.velX *= -1

        self.y += deltay

        if self.y < self.maxUp:
            self.y = 2*self.maxUp - self.y
            self.velY *= -1

        if self.y > 800:
            self.resetBall()

        self.rect.update(self.x - self.radius,self.y-self.radius,self.radius*2,self.radius*2)

    def resetBall(self):
        self.x = 600
        self.y = 600
        
        angle = random.uniform(0.5,math.pi-0.5)

        self.velX = self.targetVelocity * math.cos(angle)
        self.velY = -self.targetVelocity * math.sin(angle)

        self.rect = rect(self.x - self.radius,self.y-self.radius,self.radius*2,self.radius*2)

class Paddle():

    colour = "blue"
    length = 120
    width = 30
    speed = 0.8

    def __init__(self,game):

        self.Window = game.Window
        self.x = 540
        self.y = 700

        self.maxLeft = 0
        self.maxRight = self.Window.get_width() - self.length
        
        self.rect = Rect(self.x,self.y,self.length,self.width)
        
    def draw(self):
        draw.rect(self.Window, self.colour, self.rect)

    def update(self,dt,keys):
        if keys[K_LEFT]:
            velocity = -self.speed
        elif keys[K_RIGHT]:
            velocity = self.speed
        else:
            velocity = 0

        delta = velocity*dt
        self.x += delta

        if self.x < self.maxLeft:
            self.x = self.maxLeft
        elif self.x > self.maxRight:
            self.x = self.maxRight
        
        self.rect.update(self.x,self.y,self.length,self.width)

class Brick():

    length = 80
    width = 40

    def __init__(self,game,x,y):

        self.x = x
        self.y = y
        colours = ("green","yellow","pink","orange","purple","cyan")
        self.Window = game.Window
        self.colour = random.choice(colours)
        self.rect = Rect(x,y,self.length,self.width)
        
    def draw(self):
        draw.rect(self.Window, self.colour, self.rect)
        
if init()[1] != 0:
    print("Error initializing PyGame")

boardSize = (1200,800)
game = Game(boardSize)
clock = time.Clock()

#start of the game components being called

while True:
    for evnt in event.get():

        if evnt.type == QUIT:
            quit()
        sys.exit() # moved back a tab and error warning went away -- check in on this
        #code is unreachable, is also incorrect (for now), ignore it
            # i dont belive that this has properly been implamented yet

    dt = clock.tick(60)
    
    keys = key.get_pressed()
    
    game.Window.fill("Gray60")

    game.update(dt,keys)
    game.draw()
    display.update()   
