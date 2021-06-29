# Heeju Shim (12KNW) 2021
# AS91896 internal
# This program is a multi 


# Import libraries (if pygame is not found, print something)
import sys
import platform
import json
import os
import os.path
from pygame import surface
import requests
import urllib.request
import textwrap
import itertools
import threading
import time
import random
try:
    from pygame.locals import *
    import pygame
except ModuleNotFoundError:
    print("Hey you haven't installed pygame or none was found")
    print("Check if you're using the correct interperter")
    print("If you dont have pygame use")
    print("pip install pygame on your terminal to install it")
    time.sleep(4)
    quit(1)
# Variables
fps = 60  # Maximum FPS the game will run on (default 60)
clock = pygame.time.Clock()
score = 0  # keep track of scores
db = 0 # debounce value
chain = 0  # possible game mechanic?
delay = 3
machine_info = platform.platform() #gets Machine Values
pyv = platform.python_version() # gets Python version
initalised = False # Uninit value
white = (255, 255, 255) # white color value
clicked = False #checked if clicked!!!
black = (0, 0, 0) # black
defaultrounds = 10 #default rounds
currentround = 0 # current round
defaultmax = 30 # max rounds
correctv = 0 # correct value!!
incorrectv = 0 # incorrect value !!!
difficulty = "Easy" # default difficulty
vans = [] # Viable answer list 

pygame.init()
font = pygame.font.SysFont(None, 23)
bigText = pygame.font.SysFont(None, 45)

# Text functions
# draw_text for drawing text
# pygame has no draw text method so a function is used

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# Functions for handling API calls.
# This runs if the user chooses to refresh the quiz bank
# or on first run.
# Obviously requires internet
# If no internet connection detected, switch to offline bank
def easyapi():
     try:
          endpoint = "https://opentdb.com/api.php?amount=50&difficulty=easy&type=multiple"
          headers = {
          "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0"
          }
          hreq = urllib.request.Request(url=endpoint, headers=headers)
          ldata = urllib.request.urlopen(hreq).read()
          pdata = json.loads(ldata)
          return pdata
          # Offline error handler
     except urllib.error.URLError: 
         with open ('offline/quizeasy.json') as e: #open our offline bank to read
             pdata = json.load(e)
             return pdata

         

# Medium json file lookup
def mediumapi():
     try:
          endpoint = "https://opentdb.com/api.php?amount=50&difficulty=medium&type=multiple"
          headers = {
          "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0"
          }
          hreq = urllib.request.Request(url=endpoint, headers=headers)
          ldata = urllib.request.urlopen(hreq).read()
          pdata = json.loads(ldata)
          return pdata
    # If error handled (from being offline) do this
     except urllib.error.URLError: 
         with open ('offline/quizmedium.json') as e:
             pdata = json.load(e)
             return pdata
# Hard json file lookup
def hardapi():
     try:
          endpoint = "https://opentdb.com/api.php?amount=50&difficulty=hard&type=multiple"
          headers = {
          "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0"
          }
          hreq = urllib.request.Request(url=endpoint, headers=headers)
          ldata = urllib.request.urlopen(hreq).read()
          pdata = json.loads(ldata)
          return pdata
     except urllib.error.URLError:  #Offline handler
         with open ('offline/quizhard.json') as e:
             pdata = json.load(e)
             return pdata
# Class for buttons in the game
class button:
    # colours for button and text
    button_col = (225, 225, 225)
    hover_col = (225, 225, 225)
    click_col = (0, 128, 0)
    text_col = (0, 0, 0)
    width = 180
    height = 70


    def __init__(self, x, y, text):
        # Set x,y values, and gets text
        self.x = x
        self.y = y
        self.text = text

    def draw_button(self): # Button for drawing the button onto the screen

        global clicked
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # create pygame Rect object for the button
        button_rect = Rect(self.x, self.y, self.width, self.height)

        # check mouseover and clicked conditions
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

        # add shading to button
        pygame.draw.line(
            screen, white, (self.x, self.y), (self.x + self.width, self.y), 2
        )
        pygame.draw.line(
            screen, white, (self.x, self.y), (self.x, self.y + self.height), 2
        )
        pygame.draw.line(
            screen,
            white,
            (self.x, self.y + self.height),
            (self.x + self.width, self.y + self.height),
            2,
        )
        pygame.draw.line(
            screen,
            white,
            (self.x + self.width, self.y),
            (self.x + self.width, self.y + self.height),
            2,
        )

        # add text to button
        text_img = font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        screen.blit(
            text_img, (self.x + int(self.width / 2) -
                       int(text_len / 2), self.y + 25)
        )
        return action


# Declare all (global) button spawns

# For the menu
play = button(470, 350, "Play")
Options = button(470, 450, "Options")
Exit = button(470, 550, "Quit")
# ---------------------------------------
# For the options
back = button(0, 50, "Back")
reinit = button(124, 254, "Refresh")
diff = button(124, 354, "Difficulty")
rect = pygame.Rect(100, 100, 300, 300)

mainClock = pygame.time.Clock() # For FPS usage

pygame.init()
screen = pygame.display.set_mode((1200, 700), 0, 32)


# Initialise screen
# Handles all logical data handling before the game

def initialise():
    initalised = True
    while initalised:
        pygame.event.pump()
        screen.fill(
            (255, 255, 255)
        )  # Splice data from JSON upstream, to get questiown, correct answers and incorrect
        draw_text("ver 0.2f", font, (0, 0, 0), screen, 0, 0)
        draw_text(machine_info, font, (0, 0, 0), screen, 0, 50)
        draw_text("PLEASE WAIT", bigText, (0, 0, 0), screen, 0, 300)
        draw_text("Build composed 20/6/2021",
                  bigText, (0, 0, 0), screen, 0, 640)

        pygame.display.update()
        # Values checking if the files for the quiz file exists
        easy = os.path.exists("data/quizeasy.json")
        medium = os.path.exists("data/quizmedium.json")
        hard = os.path.exists("data/quizhard.json")

        if not easy:
            easyv = easyapi()
            e = open("data/quizeasy.json", "x")
            e.close()
            with open("data/quizeasy.json", "w") as easy:
                easy.write(json.dumps(easyv))
                e.close()
        if not medium:
            mediumv = mediumapi()
            e = open("data/quizmedium.json", "x")
            e.close()
            with open("data/quizmedium.json", "w") as easy:
                easy.write(json.dumps(mediumv))
                e.close()
        if not hard:
            hardv = hardapi()
            e = open("data/quizhard.json", "x")
            e.close()
            with open("data/quizhard.json", "w") as hard:
                hard.write(json.dumps(hardv))
                e.close()
        pygame.time.delay(2000)
        break
    main_menu()

    pygame.display.update()
    mainClock.tick(60)

# Function sets every value required by the quiz
# to 0.
# Prevents developer oversight 
# as well as cheating :)
def quizinit():
    global db, currentround, correctv, incorrectv
    if db > 0:
        db = 0
    if currentround > 0:
        currentround = 0
    if correctv > 0:
        correctv = 0
    if incorrectv > 0:
        incorrectv = 0


# Function for the main menu.
# Uses a loop until broken.
def main_menu():

    in_menu = True
    # Plays music from the assets folder
    pygame.mixer.music.load("assets/title.mp3")
    pygame.mixer.music.play()
    while in_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                print(pygame.mouse.get_pos())
        #Fills screen with white
        screen.fill((255, 255, 255))
        # Draws version information in case bug testing is required
        draw_text("ver 0.2f", font, (0, 0, 0), screen, 0, 0)
        draw_text(machine_info, font, (0, 0, 0), screen, 0, 30)
        draw_text("Python Version: {}".format(pyv),
                  font, (0, 0, 0), screen, 0, 50)
        draw_text("EVENT MODE![Evaluation Release]",
                  font, (0, 0, 0), screen, 0, 70)
        draw_text("Quiz-py", bigText, (0, 128, 0), screen, 470, 270)
        # All button handlers.
        if play.draw_button():
            in_menu = False
            # Breaks menu loop, inits quiz and plays quiz.
            quizinit()
            game()
        if Options.draw_button():
            in_menu = False
            # Same concept but options.
            options()
        if Exit.draw_button():
            # Quits the game
            quit()
        pygame.display.update()

# Function for the game
def game():
    global difficulty, db, currentround, defaultmax
    # Loads all of the json files required
    # Different difficulties have seperate files
    if difficulty == "Easy":
        eata = open("data/quizeasy.json", "r")
        data = json.load(eata)
    elif difficulty == "Medium":
        mata = open("data/quizmedium.json", "r")
        data = json.load(mata)
    elif difficulty == "Hard":
        hata = open("data/quizhard.json", "r")
        data = json.load(hata)

    in_game = True
    # Main game loop
    while in_game == True:

        if db == 0:
            # Checks if the quiz is meant to be over
            # then breaks loop and goes to results function.
            print("true man")
            if currentround > defaultmax:
                in_game = False
                results()

            results = data["results"]
            ranq = random.choice(results)
            rq = ranq["question"]
            for r in (("&quot;", " "), ("&#039;", " ")):
                rq = rq.replace(*r)
            rqe = textwrap.fill(rq, 30)
            ra = ranq["correct_answer"]
            ri = ranq["incorrect_answers"]
            # Vans (viable answers)
            # Is a list containing all correct and
            # incorrect answers.
            vans.extend(ri) # Extends values to list (preventing duplicates)
            vans.append(ra) #Append values to list
            random.shuffle(vans) # Shuffles this
            pygame.time.delay(12) # Prevents bugs from testing, delays game by 12ms
            db = db + 1 # Debouce value goes to 1 , prevents chaos

        if currentround > defaultmax:
            # Same check in db
            in_game = False
            results()
            print("results")
        else:
            pass
        # Fills screen. Blits buttons to screen.
        screen.fill((255, 255, 255))
        btn1 = button(89, 430, vans[0])
        btn2 = button(89, 560, vans[1])
        btn3 = button(924, 430, vans[2])
        btn4 = button(924, 560, vans[3])

        # Quit handlers and gets mouse position (print used for debugging)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("attempted to leave")
            elif event.type == pygame.MOUSEBUTTONUP:
                #print(pygame.mouse.get_pos())
                pass
        # Blits text to top corners displaying
        # difficulty and progress (how much to go, correct)
        #(, incorrect, etc.)
        draw_text(
            "Difficulty: {}".format(
                difficulty), font, (0, 128, 0), screen, 20, 14
        )
        draw_text(
            "Question {} out of {}".format(currentround, defaultmax),
            font,
            (0, 0, 0),
            screen,
            20,
            29,
        )
        draw_text("Correct: {}".format(correctv),
                  font, (0, 0, 0), screen, 1053, 14)
        draw_text("Incorrect: {}".format(incorrectv),
                  font, (0, 0, 0), screen, 1053, 29)
        draw_text("CHAIN: x{}".format(chain), font,
                  (0, 0, 0), screen, 419, 399)

        draw_text(rq, font, (0, 0, 0), screen, 227, 239)
        # Button handlers.
        if btn1.draw_button():
            # Each button has 0-3 positions in random
            # question list.
            # THis checks if the button in vans list positon 0
            # is correct. If correct it runs correct function.
            # Else it doesnt and just does incorrect
            # Should be self explanatory for the rest of the buttons
            if vans[0] == ra:

                correct()
            else:
                incorrect()
        if btn2.draw_button():
            if vans[1] == ra:
                correct()
            else:
                incorrect()
        if btn3.draw_button():
            if vans[2] == ra:
                correct()
            else:
                incorrect()
        if btn4.draw_button():
            if vans[3] == ra:
                correct()
            else:
                incorrect()
        # Update display (or else nothing happens lol)
        # Ticks the clock to 60 (the FPS) for performance reasons
        pygame.display.update()
        mainClock.tick(60)


# Options function
# User can refresh the banks (doesnt work if youre
# offline) and change difficulties.
def options():
    global difficulty
    options = True
    while options:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                print(pygame.mouse.get_pos())

        screen.fill((255, 255, 255))
        # Fill screen, debug info. Same thing.
        draw_text("ver 0.2f", font, (0, 0, 0), screen, 0, 0)
        draw_text(machine_info, font, (0, 0, 0), screen, 0, 30)
        draw_text("Python Version:{}".format(pyv),
                  font, (0, 0, 0), screen, 0, 50)
        # Draws information on what each button does
        draw_text(
            "Reloads the JSON quiz store. This will reset and randomise a batch of new questions.",
            font,
            (0, 0, 0),
            screen,
            419,
            287,
        )
        draw_text(
            "Current Difficulty: {}".format(difficulty),
            font,
            (0, 0, 0),
            screen,
            419,
            399,
        )
        # Button handlers
        if back.draw_button():
            options = False
            # breaks loop goes to main menu
            main_menu()
        if reinit.draw_button():
            options = False
            # Removes all files from data folder.
            # Goes back to initalise function, and then to
            # main menu.
            os.remove("data/quizeasy.json")
            os.remove("data/quizmedium.json")
            os.remove("data/quizhard.json")
            initialise()
        if diff.draw_button():
            # Change difficulty value
            if difficulty == "Easy":
                difficulty = "Medium"
            elif difficulty == "Medium":
                difficulty = "Hard"
            elif difficulty == "Hard":
                difficulty = "Easy"
        pygame.display.update()


# Functions for Game Over, Correct and Incorrect
def results():
    # The game is over!
    global difficulty, correctv, incorrectv, db 
    # Play a little music to signify game over
    pygame.mixer.music.load("assets/results.mp3")
    pygame.mixer.music.play(loops=-1, start=0.0, fade_ms=0)
    resultsv = True
    # Main results loop
    while resultsv == True:
        screen.fill((255, 255, 255))
        # Quit and mouse button handler, Same purpose.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONUP:
               # print(pygame.mouse.get_pos())
               pass

        # Button class handlers
        play_again = button(141, 578, "Play Again")
        title = button(1001, 578, "Return to Title")
        change_difficulty = button(601, 578, "Difficulty")
        # Draws stuff on the top left corner
        # Like the game function but in reverse
        draw_text(
            "Difficulty: {}".format(
                difficulty), font, (0, 128, 0), screen, 20, 14
        )
        draw_text("GAME OVER", font, (0, 0, 0), screen, 20, 29)
        draw_text("Results:", font, (0, 0, 0), screen, 318, 201)
        draw_text("Correct: {}".format(correctv),
                  font, (0, 128, 0), screen, 318, 301)
        draw_text(
            "Incorrect: {}".format(
                incorrectv), font, (255, 0, 0), screen, 318, 401
        )

        # Gives user a rank
        # Based on the amount of correct questions
        if correctv <= 5:
            draw_text("Your rank is: F", font, (0, 0, 0), screen, 318, 501)
        elif correctv <= 10:
            draw_text("Your rank is: E", font, (0, 0, 0), screen, 318, 501)
        elif correctv <= 15:
            draw_text("Your rank is: C", font, (0, 0, 0), screen, 318, 501)
        elif correctv <= 20:
            draw_text("Your rank is: B", font, (0, 0, 0), screen, 318, 501)
        elif correctv <= 24:
            draw_text("Your rank is: A", font, (0, 0, 0), screen, 318, 501)
        elif correctv <= 27:
            draw_text("Your rank is: AA", font, (0, 0, 0), screen, 318, 501)
        elif correctv <= 29:
            draw_text("Your rank is: AAA", font, (0, 0, 0), screen, 318, 501)
        elif correctv > 30:
            draw_text("Your rank is: S", font, (0, 0, 0), screen, 318, 501)

        if play_again.draw_button():  # If user wants to play again
            resultsv = False
            # Reinitialises values and goes to quiz
            quizinit()
            game()
        if title.draw_button():  # If user wants to go back to the title screen
            resultsv = False
            # Immediately returns to main screen
            main_menu()

        # Mrs Bharani suggested this, changes difficulty
        if change_difficulty.draw_button():
            if difficulty == "Easy":
                difficulty = "Medium"
            elif difficulty == "Medium":
                difficulty = "Hard"
            elif difficulty == "Hard":
                difficulty = "Easy"
        #Updates display
        pygame.display.update()


def correct():
    global db, currentround, defaultmax, chain, correctv
    # Plays a jingle
    pygame.mixer.music.load("assets/correct.mp3")
    pygame.mixer.music.play()
    # Increments the current round 
    # the correct and the
    # CHAIN values
    currentround = currentround + 1
    correctv = correctv + 1
    if currentround >= defaultmax:
        results()
    else:
        # Clears the viable answer list 
        vans.clear()
        # results.pop(ranq)
        db = db - 1 # Sets debounce value to 0 so list updates
    if chain <= 0 or chain > 0:
        chain = chain + 1
        # Increments chain value
        # Chain will break if user gets incorrect answer


def incorrect():
    global db, currentround, chain, defaultmax, incorrectv
    # Plays a little jingle
    pygame.mixer.music.load("assets/wrong.mp3")
    pygame.mixer.music.play()
    # Increments incorrect and currentround values
    incorrectv = incorrectv + 1
    currentround = currentround + 1
    if currentround >= defaultmax:
        # CHecks if the game is meant to be over
        results()
    else:
        # Clears the viable answers list, same agenda
        vans.clear()
        db = db - 1 # Sets debounce to 0 to update list
    if chain > 0:
        chain = 0
        # Breaks chain


# Since I don't need an main
# while loop I can just do this
initialise()
