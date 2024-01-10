import pygame
import gamefunctions as gf
from ebee import Ebee
from settings import Settings

#Setup pygame

game_settings = Settings()
pygame.init()
screen = pygame.display.set_mode((game_settings.screen_height,game_settings.screen_width))    #Set the screen size
pygame.display.set_caption("Average MMU Commute")
clock = pygame.time.Clock()
running = True      #Running state of the game.
ebee = Ebee(screen)

while running:
    gf.update_screen(screen , ebee)
    gf.check_events()
