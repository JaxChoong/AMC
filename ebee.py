
# **********************************
# This file is written by JAX
# **********************************

import pygame
from settings import Settings
from pygame.sprite import Sprite

settings=Settings()

# Class that manages behaviours of the ebee.
# eric wrote this yes
class Ebee(Sprite):
    def __init__(self,screen):
        self.screen = screen
        
        #Load ebee and get its rect.
        self.image = pygame.image.load('images\ebee.png')     #import the ebee image
        self.image = pygame.transform.scale(self.image, (40, 90))      #resize ebee image
        self.imageright = pygame.image.load('images\ebeeright.png')     #right ebee image
        self.imageright = pygame.transform.scale(self.imageright, (50, 90))   #resize right ebee
        self.imageleft = pygame.image.load('images\ebeeleft.png')     #left ebee image
        self.imageleft = pygame.transform.scale(self.imageleft, (50, 90))    #resize left ebee
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
        #Commented out so that it runs faster

        if(self.moving_right==True):
            self.screen.blit(self.imageright, self.rect)
        elif(self.moving_left==True):
            self.screen.blit(self.imageleft, self.rect)
        else:
            
        # # Draw ebee at its current location
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

        