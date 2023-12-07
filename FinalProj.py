# This file was created by: Emilio Perez

# Sources of code:
# https://www.geeksforgeeks.org/how-to-create-buttons-in-a-game-using-pygame/
# https://www.youtube.com/watch?v=G8MYGDf_9ho

# Title Vball defense training 
# Goals


from Settings import *
import pygame
import sys 
import os

# start_img = pg.image.load('start.png')

import pygame
import button

game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'image')
sounds_folder = os.path.join(game_folder, 'sounds')

#create display window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')



# Game variables
game_menu = True
game_menu_start = False

#load button images
start = pygame.image.load('image/start.png').convert_alpha()
setup = pygame.image.load('image/set_up.png').convert_alpha()
instruction = pygame.image.load('image/instructions.png').convert_alpha()
filler = pygame.image.load('image/filler.png').convert_alpha()

#create button instances
start_button = button.Button(300, 50, start, 0.8)
setup_button = button.Button(300, 200, setup, 0.8)
instruction_button = button.Button(300, 350, instruction, 0.8)
filler_screen = button.Button(300, 350, filler, 0.8)

#define fonts
font = pygame.font.SysFont("arialblack", 40)

#define colours
TEXT_COL = (255, 255, 255)

# define drawtext
def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))


#game loop
run = True
while run:
	draw_text("Press SPACE to pause", font, TEXT_COL, 160, 250)
	
	screen.fill((202, 228, 241))
	# Prints if button is clicked
if game_menu == 1:
	game_menu += 1
	if start_button.draw(screen) == True:
		game_menu = False
		game_menu_start = True


	
	if game_menu_start == True:
		filler_screen.draw(screen)
		
		
		
	if setup_button.draw(screen):
		print('EXIT')
		
		
	if instruction_button.draw(screen):
		print('instructions')
		

	# event handler
	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False




pygame.display.update()

pygame.quit()


#     # updates the frames of the game 
# pg.display.update() 




  