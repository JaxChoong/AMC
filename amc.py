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
import gamefunctions as gf
from ebee import Ebee
from cars import Cars
from settings import Settings
from LeaderBoard import Score

#Setup pygame (Jax)

game_settings = Settings()
pygame.init()
screen = pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))    #Set the screen size
pygame.display.set_caption("Average MMU Commute")
clock = pygame.time.Clock()
running = True      #Running state of the game.
ebee = Ebee(screen)
lane = gf.randomizeLanes()
cars = Cars(screen, lane)
score = Score()


while running:
    gf.check_events(ebee)
    ebee.movementUpdate()
    cars.update(score)
    gf.check_ebee_cars_collisions(ebee,cars)   #Check for collisions between ebee and cars
    gf.update_screen(screen , ebee, cars)
