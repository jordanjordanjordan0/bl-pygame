
import random

# Initializa game -tells computer that the following
# code should be interpretted as a game
pygame.init()

# step 1. Set up the display 
height = 1000
width = 1200


screen = pygame.display.set_mode((width, height))

# this will allow us to show the title of the game when a
# user opens our game
pygame.display.set_caption("Avoid the Falling Objects")

# Set frame rate
clock = pygame.time.Clock()
FPS = 60

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()






class player:
    def __init__(self):
        self.x = width // 2 # Start in the middle
        self.y = height - 60 # Near the bottom
        self.playerWidth = 50
        self.playerHeight = 50
        self.playerSpeed= 5 # How fast the player moves

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.playerSpeed
        if keys[pygame.K_RIGHT] and self.x < width - self.playerWidth:
            self.x += self.playerSpeed

    def draw(self):
        pygame.draw.rect(screen, (0,0, 255), (self.x, self.y, self.playerWidth, self.playerHeight))
