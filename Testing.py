# This file was created by: Emilio Perez

# Sources of code:
# https://www.geeksforgeeks.org/how-to-create-buttons-in-a-game-using-pygame/
# https://www.youtube.com/watch?v=G8MYGDf_9ho

# Goals 12/9/23-
# find out how to mkae ball disapear at 1500 then make new img that is downball that apears when ball 
# disapears to create the illusion that the ball is moving.

# Title Vball defense training 
# Goals

import pygame
import os
import pygame
import button
import random
from random import randint


pygame.init()

#create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

#game variables
game_open = False
menu_state = "main"


#define fonts
font = pygame.font.SysFont("arialblack", 40)

#define colours
TEXT_COL = (255, 255, 255)
transparent = (0, 0, 0, 0)

#load button images
start_img = pygame.image.load("image/start.png").convert_alpha()
setup_img = pygame.image.load("image/set_up.png").convert_alpha()
quit_img = pygame.image.load("image/quit.png").convert_alpha()
inst_img = pygame.image.load('image/instructions.png').convert_alpha()
audio_img = pygame.image.load('images/button_audio.png').convert_alpha()
keys_img = pygame.image.load('images/button_keys.png').convert_alpha()
back_img = pygame.image.load('image/back.png').convert_alpha()


#create button instances
start_button = button.Button(380, 100, start_img, 1)
setup_button = button.Button(380, 240, setup_img, 1)
quit_button = button.Button(380, 520, quit_img, 1)
inst_button = button.Button(380, 380, inst_img, 1)
keys_button = button.Button(246, 325, keys_img, 1)
back_button = button.Button(332, 450, back_img, 1)

class Ball(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load("image/ball.png").convert_alpha()
        self.rect = self.image.get_rect(center=position)


def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#images
court = pygame.image.load("image/Tcourt.png")
ball = pygame.image.load("image/ball.png")
ball1 = Ball((0,0))
ball2 = Ball((0,0))

change_timer = pygame.time.get_ticks()
# 3 seconds
change_interval = 3000 

# list of where the ball can go
set = [[200,0], [470,0], [800,0]]
# Picks one of the locations
ball_set = set[randint(0, 2)]
spikes = [[200,400], [470,500], [800,400]]
downball = spikes[randint(0, 2)]

# Make ball2 apear and disapear 
show_ball2 = False
ball0 = screen.blit(ball, ball_set)

def testing():
    global show_ball2

    screen.blit(court,(0,0))
    screen.blit(ball, ball_set)

    # if show_ball2 == True:
    #       ball2 == True

    
    # if elapsed_time < change_interval / 2:
    #   print("works")
    # show_ball2 = True
 
      
      
      
      
    

    
    # screen.blit(ball, downball)
    
  

    






#gets the current time of game
current_time = pygame.time.get_ticks()
#game loop
run = True
clock = pygame.time.Clock()
while run:

  current_time = pygame.time.get_ticks()
  elapsed_time = current_time - change_timer
  print(change_timer)

  screen.fill((202, 228, 241))

#check if game is paused
  if game_open == True:
    #check menu state
    if menu_state == "main":
      #draw pause screen buttons
      if start_button.draw(screen):
        menu_state = "start"
      if setup_button.draw(screen):
        menu_state = "setup"
      if inst_button.draw(screen):
        menu_state = "inst"
      if quit_button.draw(screen):
        run = False
         
# check for start menu state
    if menu_state == "start":
      #calls the game
      testing()
      
      
      # for change_interval in range (1400,1500):
        
      
      # check if it's time to change the ball's position
      # if its been 3 seconds reset ball and ball2 position
      if current_time - change_timer >= change_interval:
            ball_set = set[randint(0, 2)]
            downball = spikes[randint(0, 2)]
            show_ball2 = False
            # screen.blit(ball2, downball)
            change_timer = current_time


      while  change_timer < 1/current_time:
        print("works")
      show_ball2 = True
     
      
      # if current_time - change_timer >= change_interval:
      #   show_ball2 = False

      if back_button.draw(screen):
        menu_state = "main"
      

#check if the options menu is open
    if menu_state == "setup":
      #draw the different options buttons
      if inst_button.draw(screen):
        print("Video Settings")
      if back_button.draw(screen):
        menu_state = "main"

      # check for instruction menu state
    if menu_state == "inst":
      #draw the different options buttons
      if inst_button.draw(screen):
        print("Video Settings")
      if back_button.draw(screen):
        menu_state = "main"

  else:
    draw_text("Press SPACE to start", font, TEXT_COL, 160, 250)




 

    
  

        

  #event handler
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        game_open = True
    if event.type == pygame.QUIT:
      run = False

  pygame.display.flip()
  clock.tick(60)


pygame.quit()