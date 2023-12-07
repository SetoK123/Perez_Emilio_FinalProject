import pygame
import button

pygame.init()

#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

#game variables


#define fonts
font = pygame.font.SysFont("arialblack", 40)

#define colours
TEXT_COL = (255, 255, 255)


def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#game loop
run = True
while run:

  screen.fill((52, 78, 91))

  draw_text("Press SPACE to pause", font, TEXT_COL, 160, 250)

   #event handler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False



  #event handler
  

  pygame.display.update()

pygame.quit()