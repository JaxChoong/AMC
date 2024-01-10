# *********************************************************
# Program: YOUR_FILENAME.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: TL13
# Year: 2023/24 Trimester 1
# Names: ERIC_CHIN_YAN_HONG | CHONG_MENG_HANG | MEMBER_NAME_3
# IDs: 1221107092 | 1221105899 | MEMBER_ID_3
# Emails: 1221107092@student.mmu.edu.my | 1221105899@student.mmu.edu.my | MEMBER_EMAIL_3
# Phones: 0168262342 | 0168711296 | MEMBER_PHONE_3
# ********************************************************* 
import pygame
import gamefunctions as gf
from ebee import Ebee
from settings import Settings

#Setup pygame (Jax)

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
