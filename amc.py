import pygame
import gamefunctions as gf
from ebee import Ebee

#Setup pygame
pygame.init()
screen = pygame.display.set_mode((720,600))    #Set the screen size
pygame.display.set_caption("Average MMU Commute")
clock = pygame.time.Clock()
running = True      #Running state of the game.
ebee = Ebee(screen)

while running:
    gf.update_screen(screen , ebee)
    gf.check_events()
