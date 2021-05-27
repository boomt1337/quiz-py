# AS91896 internal
# Heeju Shim 2021


# Import libraries (if pygame is not found, print something)
try:
 import pygame
 import sys
 import json
except ModuleNotFoundError:
     print("Pygame not found, install it with pip install pygame")

# Variables
fps = 60 # Maximum FPS the game will run on (default 60)
res = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
score = 0 # keep track of scores


while True:
    pygame.display.init()
    background = pygame.Surface(res.get_size())
    background.fill((250,250,250))
    pygame.display.flip()



