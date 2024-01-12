from pygame.sprite import Sprite
import pygame
from settings import Settings 
import random

settings = Settings()

class Cars(Sprite):
    

    # A class to manage cars.
    def __init__(self, screen,lane, car_number):
        super(Cars,self).__init__()
        self.screen = screen
        car_image = self.randomiseCars()
        self.rect = self.image.get_rect()

        self.rect = self.image.get_rect()
        self.rect.centerx = lane
        self.rect.y = 0
        self.y = float(self.rect.y)
        self.speed_factor = settings.car_speed_factor

    def blitme(self):
        """Draw the car at its current position"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        # Move the cars down
        self.y += settings.car_speed_factor
        self.rect.y = self.y

    def check_edges(self):
        if self.rect.top == 600:
            return True
        
    def randomiseCars(self):
        # Function to randomise cars' icons.
        car_number = random.randint(1,3)
        if car_number == 1:
            self.image = pygame.image.load('images/car1.png')
            self.image = pygame.transform.scale(self.image, (90, 100))
        elif car_number == 2:
            self.image = pygame.image.load('images/car2.png')
            self.image = pygame.transform.scale(self.image, (150, 100))
        elif car_number == 3:
            self.image = pygame.image.load('images/car3.png')
            self.image = pygame.transform.scale(self.image, (150, 100))