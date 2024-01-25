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
import highest_score as hs
import sound as sfx


# ******************************************
# This file is written by JAX
# (CALVIN and ERIC type a few lines only)
# ******************************************

settings = Settings()
pygame.init()
screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))    #Set the screen size
pygame.display.set_caption("Average MMU Commute")
clock = pygame.time.Clock()
ebee = Ebee(screen)
lane = gf.randomizeLanes()
existing_lanes = []
play_button = Button(settings, screen, "Play")
mouse_x, mouse_y = pygame.mouse.get_pos()
score = Score(settings, screen)
carsGroup = Group()
gf.create_cars(screen,existing_lanes,carsGroup)


while True:
    gf.check_events(ebee, play_button,settings, screen, score, carsGroup, mouse_x, mouse_y,existing_lanes)
    if settings.running:
        ebee.movementUpdate()
        carsGroup.update(score,settings)
        gf.check_ebee_cars_collisions(ebee,carsGroup,settings)   #Check for collisions between ebee and car 
        gf.scale_game_difficulty(settings,score,screen,existing_lanes,carsGroup)    # Scales up game diff depending on score

    #testing (Calvin)
    else:
        settings.game_over = True


    gf.update_screen(settings, screen, score, play_button, ebee, carsGroup)
    # lb.update_score_list(settings, score)

    #testing (Calvin)
    if settings.game_over:
        hs.update_score_list(settings, score)