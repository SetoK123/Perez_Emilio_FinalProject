
import pygame
import Testing
from Testing import screen



pygame.init()

court = pygame.image.load("image/Tcourt.png")
ball = pygame.image.load("image/filler.png")

def testing():
    screen.blit(ball,(0,0))
    
