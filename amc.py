# *********************************************************
# Program: amc.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: TL13
# Year: 2023/24 Trimester 1
# Names: ERIC_CHIN_YAN_HONG | CHONG_MENG_HANG | CHOONG JIA XUEN
# IDs: 1221107092 | 1221105899 | 1221106177
# Emails: 1221107092@student.mmu.edu.my | 1221105899@student.mmu.edu.my | 1221106177@student.mmu.edu.my
# Phones: 0168262342 | 0168711296 | 0136573888
# ********************************************************* 
import pygame
from pygame.sprite import Group
import gamefunctions as gf
from ebee import Ebee
from cars import Cars   
from settings import Settings
from gamescore import Score
from playbutton import Button

#Setup pygame (Jax)

game_settings = Settings()
pygame.init()
screen = pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))    #Set the screen size
pygame.display.set_caption("Average MMU Commute")
clock = pygame.time.Clock()
ebee = Ebee(screen)
lane = gf.randomizeLanes()
play_button = Button(game_settings, screen, "Play")

score = Score(game_settings, screen)
carsGroup = Group()
gf.create_cars(screen,lane,carsGroup)


while True:
    gf.check_events(ebee, play_button, screen, score, carsGroup)
    if game_settings.running:
        ebee.movementUpdate()
        carsGroup.update(score)
        gf.check_ebee_cars_collisions(ebee,carsGroup,game_settings)   #Check for collisions between ebee and car 
        gf.scale_game_difficulty(game_settings,score,screen,lane,carsGroup)    # Scales up game diff depending on score
    gf.update_screen(game_settings, screen, score, play_button, ebee, carsGroup)
