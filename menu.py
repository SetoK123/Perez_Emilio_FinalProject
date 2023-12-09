# This file was created by: Emilio Perez

# Sources of code:
# https://www.geeksforgeeks.org/how-to-create-buttons-in-a-game-using-pygame/
# https://www.youtube.com/watch?v=G8MYGDf_9ho

# Title Vball defense training 
# Goals

import pygame
import os
import pygame
import button


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
audio_button = button.Button(225, 200, audio_img, 1)
keys_button = button.Button(246, 325, keys_img, 1)
back_button = button.Button(332, 450, back_img, 1)

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#game loop
run = True
while run:

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
      #draw the different options buttons
      if inst_button.draw(screen):
        print("Video Settings")
      if back_button.draw(screen):
        menu_state = "main"

#check if the options menu is open
    if menu_state == "setup":
      #draw the different options buttons
      inst_button.draw(screen)
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

  pygame.display.update()

pygame.quit()