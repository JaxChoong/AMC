
# **********************************
# This file is written by JAX
# **********************************

import pygame
from settings import Settings
from pygame.sprite import Sprite

settings=Settings()

# Class that manages behaviours of the ebee.
class Ebee(Sprite):
    def __init__(self,screen):
        self.screen = screen
        
        #Load ebee and get its rect.
        self.image = pygame.image.load('images\ebee.png')     #import the ebee image
        self.image = pygame.transform.scale(self.image, (40, 90))      #resize ebee image
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start ebee at the bottom of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for ebee center
        self.center = float(self.rect.centerx)

        #Init movement flag
        self.moving_right=False
        self.moving_left=False

    def blitme(self):
        # Draw ebee at its current location
        self.screen.blit(self.image, self.rect)

    def center_ebee(self):
        # Center ebee on the screen.
        self.center = self.screen_rect.centerx

    def movementUpdate(self):      # Eric wrote this part
        #Ebee movement(left and right)
        self.rect.centerx=self.center
        if(self.moving_right==True and self.rect.right < 350):
            self.center+=settings.ebee_speed_factor
        elif(self.moving_left==True and self.rect.left > 0):
            self.center-=settings.ebee_speed_factor
        