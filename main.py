# AS91896 internal
# Heeju Shim 2021


# Import libraries (if pygame is not found, print something)

import pygame
import sys
import platform
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
import random


# Variables
fps = 60 # Maximum FPS the game will run on (default 60)
clock = pygame.time.Clock()
score = 0 # keep track of scores
amount = 0
db = 0
chain = 0 # possible game mechanic?
delay = 3
machine_info = platform.platform()
pyv = platform.python_version()
initalised = False
header = "https://opentdb.com/api.php?amount{}".format(amount)
white = (255,255,255)
clicked = False
black = (0,0,0)
defaultrounds = 10
difficulty = "Easy"
vans = []


font = pygame.font.SysFont(None,45)
smallText = pygame.font.SysFont(None,23)

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
    endpoint = "https://opentdb.com/api.php?amount=50&difficulty=easy&type=multiple"
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    hreq = urllib.request.Request(url=endpoint, headers=headers)
    ldata = urllib.request.urlopen(hreq).read()
    pdata = json.loads(ldata)
    return pdata

def mediumapi():
 endpoint = "https://opentdb.com/api.php?amount=50&difficulty=medium&type=multiple"
 headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
 hreq = urllib.request.Request(url=endpoint, headers=headers)
 ldata = urllib.request.urlopen(hreq).read()
 pdata = json.loads(ldata)
 return pdata
 
def hardapi():
 endpoint = "https://opentdb.com/api.php?amount=50&difficulty=hard&type=multiple"
 headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
 hreq = urllib.request.Request(url=endpoint, headers=headers)
 ldata = urllib.request.urlopen(hreq).read()
 pdata = json.loads(ldata)
 return pdata
# Class for buttons in the game
class button():
	#colours for button and text
	button_col = (225, 225, 225)
	hover_col = (225, 225, 225)
	click_col = (0,128,0)
	text_col = (0,0,0)
	width = 180
	height = 70

	def __init__(self, x, y, text):
		self.x = x
		self.y = y
		self.text = text

	def draw_button(self):

		global clicked
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#create pygame Rect object for the button
		button_rect = Rect(self.x, self.y, self.width, self.height)
		
		#check mouseover and clicked conditions
		if button_rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1:
				clicked = True
				pygame.draw.rect(screen, self.click_col, button_rect)
			elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
				clicked = False
				action = True
			else:
				pygame.draw.rect(screen, self.hover_col, button_rect)
		else:
			pygame.draw.rect(screen, self.button_col, button_rect)
		
		#add shading to button
		pygame.draw.line(screen, white, (self.x, self.y), (self.x + self.width, self.y), 2)
		pygame.draw.line(screen, white, (self.x, self.y), (self.x, self.y + self.height), 2)
		pygame.draw.line(screen, black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
		pygame.draw.line(screen, black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

		#add text to button
		text_img = font.render(self.text, True, self.text_col)
		text_len = text_img.get_width()
		screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
		return action

# Declare all (global) button spawns

#For the menu
play = button(255, 350, "Play")
Options = button(255, 450, "Options")
Exit = button(255, 550, "Quit")
#---------------------------------------
#For the options
back = button(0,50,"Back")
reinit = button(124,254,"Refresh")
diff = button(124,354, "Difficulty")


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
      draw_text(machine_info, smallText, (0,0,0),screen,0,50)
      draw_text("PLEASE WAIT", font, (0,0,0),screen,0,300)
      draw_text("Build composed 15/6/2021", font, (0,0,0),screen,0,640)
      


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
      pygame.event.pump()
      screen.fill((255,255,255))
      draw_text("ver 0.1b", font, (0,0,0),screen,0,0)
      draw_text(machine_info, smallText, (0,0,0),screen,0,30)
      draw_text("Python Version: {}".format(pyv), smallText, (0,0,0),screen,0,50)
      draw_text("Quiz-py", font, (0,128,0),screen,296,260)
      if play.draw_button():
           in_menu = False
           game()
      if Options.draw_button():
           in_menu = False
           options()
      if Exit.draw_button():
	      quit()
      pygame.display.update()

      

 


def game():
     global difficulty
     if difficulty == "Easy":
          eata = open("quizeasy.json", "r")
          data = json.load(eata)
     elif difficulty == "Medium":
          mata = open("quizmedium.json", "r")
          data = json.load(mata)
     elif difficulty == "Hard":
          hata = open("quizhard.json", "r")
          data = json.load(hata)
     # Splice data from JSON upstream, to get questiown, correct answers and incorrect
     while True:
          
          
          global db
          if db == 0:


              results = data['results']
              ranq = random.choice(results)
              rq = ranq['question']
              ra = ranq['correct_answer']
              ri = ranq['incorrect_answers']

              vans.extend(ri)
              vans.append(ra)
     # Local button data (to use in this function only)
              random.shuffle(vans)
              pygame.time.delay(12)
              db = db + 1
            

     
          
          screen.fill((255,255,255))
          btn1 = button(89, 430, vans[0])
          btn2 = button(89, 560, vans[1])
          btn3 = button(465,433,vans[2])
          btn4 = button(516, 557, vans[3])

          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    print("attempted to leave")
               elif event.type == pygame.MOUSEBUTTONUP:
                    print(pygame.mouse.get_pos())

     
          if btn1.draw_button():

               if vans[0] == ra:

                    print("lawl")
                    db = True
               else:
                    print("bawl")
                    db = True
          if btn2.draw_button():
               if vans[1] == ra:
                    print("lawl")
                    db = True
               else:
                    print("bawl")
                    db = True
          if btn3.draw_button():
               if vans[2] == ra:
                    print("lawl")
                    db = True
               else:
                    print("bawl")
                    db = True
          if btn4.draw_button():
               if vans[3] == ra:
                    print("lawl")
                    db = True
               else:
                    print("bawl")
                    db = True
      
          pygame.display.update()
          mainClock.tick(60)
 



def options():
     global difficulty
     options = True
     while options:
          pygame.event.pump()
          screen.fill((255,255,255))
          draw_text("ver 0.1b", font, (0,0,0),screen,0,0)
          draw_text(machine_info, smallText, (0,0,0),screen,0,30)
          draw_text("Python Version:{}".format(pyv), smallText,(0,0,0), screen,0,50)
     
          if back.draw_button():
               options = False
               main_menu()
          if reinit.draw_button():
               print("LOL!")
          if diff.draw_button():
               if difficulty == "Easy":
                    difficulty = "Medium"
               elif difficulty == "Medium":
                    difficulty = "Hard"
               elif difficulty == "Hard":
                    difficulty = "Easy"
          pygame.display.update()


     

initialise()
