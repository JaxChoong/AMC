
# **********************************
# This file is written by JAX
# **********************************

from pygame.sprite import Sprite
import pygame
import random
import gamefunctions as gf
class Cars(Sprite):
    
    # A class to manage cars.
    def __init__(self, screen,settings,lane):
        super(Cars,self).__init__()
        self.screen = screen
        self.image = self.randomizeCars()
        self.rect = self.image.get_rect()
        self.lane = gf.randomizeLanes()
        self.rect.centerx = lane
        self.rect.y = 0
        self.y = float(self.rect.y)
        self.speed_factor = random.uniform(settings.car_speed_minimum,settings.car_speed_maximum)

    def blitme(self):
        # Draw the car at its current position
        self.screen.blit(self.image, self.rect)

    def update(self, score,settings):
        # Move the cars down
        edge = self.check_edges(score,settings)
        if edge:
            self.rect.centery = 0
            self.y = 0
        elif not edge:
            self.y += self.speed_factor
            self.rect.centery = self.y

    def check_edges(self, score,settings):
        #Check if cars have reached bottom of the screen
        if self.rect.top >= 600:
            self.resetCars(score,settings)
        else:
            return False
        
    def randomizeCars(self):
        # Function to randomise cars' icons.
        car_number = random.randint(1,3)
        if car_number == 1:
            self.image = pygame.image.load('images/car1.png')
            self.image = pygame.transform.scale(self.image, (90, 100))
        elif car_number == 2:
            self.image = pygame.image.load('images/car2.png')
            self.image = pygame.transform.scale(self.image, (90, 100))
        elif car_number == 3:
            self.image = pygame.image.load('images/car3.png')
            self.image = pygame.transform.scale(self.image, (90, 100))
        return self.image

    def resetCars(self, score,settings):     # Rest cars back to the top of screen
        self.lane = gf.randomizeLanes()
        self.car_image = self.randomizeCars()
        self.rect.centery = 0
        self.rect.centerx = self.lane
        self.y = 0
        score.score += settings.score_scale
        self.speed_factor = random.uniform(settings.car_speed_minimum,settings.car_speed_maximum)