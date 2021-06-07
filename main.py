# AS91896 internal
# Heeju Shim 2021


# Import libraries (if pygame is not found, print something)

import pygame
import sys
import json
import os
import os.path
from pygame import surface
import pytext
import requests
import urllib.request
import itertools
import threading
import time

# Variables
fps = 60 # Maximum FPS the game will run on (default 60)
clock = pygame.time.Clock()
score = 0 # keep track of scores
amount = 0
chain = 0 # possible game mechanic?
initalised = False
header = "https://opentdb.com/api.php?amount{}".format(amount)

font = pygame.font.SysFont(None,45)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Functions for handling API calls.
# This runs if the user chooses to refresh the quiz bank
# or on first run. 
# Obviously requires internet, so the program will quit if it is not detected.
def easyapi():
    endpoint = "https://opentdb.com/api.php?amount=50&difficulty=easy"
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    hreq = urllib.request.Request(url=endpoint, headers=headers)
    ldata = urllib.request.urlopen(hreq).read()
    pdata = json.loads(ldata)
    return pdata

def mediumapi():
 endpoint = "https://opentdb.com/api.php?amount=50&difficulty=medium"
 headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
 hreq = urllib.request.Request(url=endpoint, headers=headers)
 ldata = urllib.request.urlopen(hreq).read()
 pdata = json.loads(ldata)
 return pdata
 
def hardapi():
 endpoint = "https://opentdb.com/api.php?amount=50&difficulty=hard"
 headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
 hreq = urllib.request.Request(url=endpoint, headers=headers)
 ldata = urllib.request.urlopen(hreq).read()
 pdata = json.loads(ldata)
 return pdata


mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((700, 700),0,32)

def initialise():
 initalised = True
 while initalised:
      pygame.event.pump()
      screen.fill((255,255,255))
      draw_text("ver 0.1b", font, (0,0,0),screen,0,0)
      draw_text("PLEASE WAIT", font, (0,0,0),screen,0,300)
      draw_text("Build composed 6/7/2021", font, (0,0,0),screen,0,640)
      pygame.display.update()
      easy = os.path.exists("quizeasy.json")
      medium = os.path.exists("quizmedium.json")
      hard = os.path.exists("quizhard.json")
      
      if not easy:
           easyv = easyapi()
           e = open("quizeasy.json", "x")
           e.close()
           with open("quizeasy.json", "w") as easy:
                easy.write(json.dumps(easyv))
                e.close()
      if not medium:
           mediumv = mediumapi()
           e = open("quizmedium.json", "x")
           e.close()
           with open("quizmedium.json", "w") as easy:
                easy.write(json.dumps(mediumv))
                e.close()
      if not hard:
           hardv = hardapi()
           e = open("quizhard.json", "x")
           e.close()
           with open("quizhard.json", "w") as hard:
                hard.write(json.dumps(hardv))
                e.close()
      pygame.time.delay(2000)
      break
 main_menu()
     
 pygame.display.update()
 mainClock.tick(60)


                
                




def main_menu():
 in_menu =True
 
 while in_menu:
       for event in pygame.event.get():
            if event.type==QUIT:
                 pygame.quit()
            screen.fill((0,0,0))
       draw_text("test", font, (0,0,0),screen,0,0)
       pygame.display.update()
       mainClock.tick(60)


 


def game():
     pass

initialise()
