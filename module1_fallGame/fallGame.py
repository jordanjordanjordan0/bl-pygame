import pygame
import random

# Initalize game -tells computer that the following
# code should be interpretted as a game
pygame.init()
 
# Step 1. set up display
height = 600
width = 800

# this is reusable code that represents our game screen
screen = pygame.display.set_mode((width, height))

# this will allow us to show the title of the game when a
# user opens our game
pygame.display.set_caption("Avoid the Falling Objects")

# Set frame rate
clock = pygame,time.clock() # games run on frames
FPS = 60 # Game updates 60 times per second

#. Step 2. Create player object
# Object - a data type that allows us to
# pass in unique data, including
# functions and other objects

class Player:
    def __init__(self):
        self.x = width // 2 # Start in the middle
        self.y = height - 60 # Near the bottom
        self.playerwidth = 50
        self.playerheight = 50
        self.playerspeed = 5 # How fast the player moves

    def move(self, keys):
        if keys[pygame.k_LEFT] and self.x > 0:
            self.x -= self.playerspeed
        if keys[pygame.K_RIGHT] and self.x < width - self.playerWidth:
            self.x += self.playerSpeed  
    
    def draw(self):
        pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, selfplayerWidth, self.playHeight))

