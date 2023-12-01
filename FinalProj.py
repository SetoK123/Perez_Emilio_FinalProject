# This file was created by: Emilio Perez

# Sources of code:
# https://www.geeksforgeeks.org/how-to-create-buttons-in-a-game-using-pygame/
# https://www.youtube.com/watch?v=G8MYGDf_9ho

# Title Vball defense training 
# Goals


from Settings import *
import pygame as pg 
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



#load button images
start = pygame.image.load('Perez_Emilio_FinalProject/image/start.png').convert_alpha()
setup = pygame.image.load('Perez_Emilio_FinalProject/image/set_up.png').convert_alpha()
instruction = pygame.image.load('Perez_Emilio_FinalProject/image/instructions.png').convert_alpha()
filler = pygame.image.load('Perez_Emilio_FinalProject/image/filler.png').convert_alpha()

#create button instances
start_button = button.Button(300, 50, start, 0.8)
setup_button = button.Button(300, 200, setup, 0.8)
instruction_button = button.Button(300, 350, instruction, 0.8)
filler_screen = button.Button(300, 350, filler, 0.8)

#game loop
run = True
while run:

	screen.fill((202, 228, 241))
# Prints if button is clicked
	if start_button.draw(screen) == True:
		print('START')
		
	else:
		pass
		
		
	if setup_button.draw(screen):
		print('EXIT')
		
		
	if instruction_button.draw(screen):
		print('instructions')
		

	#event handler
	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()

#     # updates the frames of the game 
# pg.display.update() 




  