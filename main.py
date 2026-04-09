import pygame
from sys import exit
import os

GAME_WIDTH = 512 
GAME_HEIGHT = 512

PLAYER_X = GAME_HEIGHT / 2
PLAYER_Y = GAME_WIDTH / 2

PLAYER_HEIGHT = 42
PLAYER_WIDTH = 48
PLAYER_DISTANCE = 5

# image
background_image = pygame.image.load(os.path.join("images", "background.png"))
player_image_right = pygame.image.load(os.path.join("images", "megaman-right.png"))
player_image_right = pygame.transform.scale(player_image_right, (PLAYER_WIDTH, PLAYER_HEIGHT))

pygame.init()
window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Starting to create games using python")
pygame.display.set_icon(player_image_right)
clock = pygame.time.Clock()

class Player(pygame.Rect):
    def __init__(self):
        super().__init__(PLAYER_X, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.image = player_image_right

# left(x), right(y), width, height
# player = pygame.Rect(150, 150, 50, 50)
player = Player()
print(player)


         

def draw(): 
    window.fill((20, 18, 167))
    window.blit(background_image, (0, 80))
    window.blit(player.image, (player))
    # pygame.draw.rect(window, (2, 239, 238), player)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
       
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player.y = max(player.y - PLAYER_DISTANCE, 0)

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player.y = min(player.y + PLAYER_DISTANCE, GAME_HEIGHT - player.height)

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.x = min(player.x + PLAYER_DISTANCE, GAME_WIDTH + player.width)

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.x = max(player.x - PLAYER_DISTANCE, 0)

        draw()
    pygame.display.update()
    clock.tick(60) #60 frams per second (fps)


 # if event.type == pygame.KEYDOWN:
        #     if event.key in (pygame.K_UP, pygame.K_w):
        #         player.y -= 5
        #     if event.key in (pygame.K_DOWN , pygame.K_s):
        #         player.y += 5
        #     if event.key in (pygame.K_RIGHT, pygame.K_d):
        #         player.x += 5
        #     if event.key in (pygame.K_LEFT, pygame.K_a):
        #         player.x -= 5 


   # player.y -= PLAYER_DISTANCE
            # if player.y < 0:
            #     player.y = 0
                # player.y += PLAYER_DISTANCE 

     # player.y += PLAYER_DISTANCE
            # if player.y + player.height > GAME_HEIGHT:
            #     player.y = GAME_HEIGHT - player.height
