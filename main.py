# AS91896 internal
# Heeju Shim 2021


# Import libraries (if pygame is not found, print something)
try:
 import pygame
 import sys
 import json
 import pytext
 import requests
 import urllib
 import itertools
 import threading
 import time
except ModuleNotFoundError:
     print("Pygame not found, install it with pip install pygame")
     quit()

# Variables
fps = 60 # Maximum FPS the game will run on (default 60)
clock = pygame.time.Clock()
score = 0 # keep track of scores
amount = 0
chain = 0 # possible game mechanic?
initalised = False
header = "https://opentdb.com/api.php?amount{}".format(amount)



# Functions and classes
def online():
     try:
          urllib.urlopen('http://216.58.192.142', timeout = 1)
          return True
     except urllib.error.URLError as err:
          return False


def set_text(string, coordx, coordy, fontSize): #Function to set text

    font = pygame.font.Font('freesansbold.ttf', fontSize) 
    #(0, 0, 0) is black, to make black text
    text = font.render(string, True, (0, 0, 0)) 
    textRect = text.get_rect()
    textRect.center = (coordx, coordy) 
    return (text, textRect)


def init():
     # This is a function that checks integrity and loads
     # api data if the program detects the computer is online.
     #Else, it will function offline.
     pygame.init()
     pygame.font.init()
     screen = pygame.display.set_mode((1000,1000))
     screen.fill((0,0,0))
     initalised = False
     online()
     while initalised == False:
     # Draws text onto the screen
      pytext.draw("ver 0.1b", (15,26), color=(255,255,255))
      pytext.draw("pyquiz INIT...", (20,88), color=(255,255,255))
      pytext.draw("Main", (163,403), color=(255,255,255))
      pytext.draw("Network", (163,427), color=(255,255,255)
      


      
      












def main():
     while True:
      
      screen
      pygame.display.set_caption('pyQuiz running')

      pygame.display.flip()
      


      for event in pygame.event.get():
           if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

      print(pygame.mouse.get_pos())
      clock.tick(120)
# main Game
while True:
 pygame.init()
 pygame.font.init()
 screen = pygame.display.set_mode((1000,1000))
 if initalised == False:
      init()
      break
      


main()


