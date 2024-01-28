from pygame.sprite import Sprite
import pygame
import random
import gamefunctions as gf


# Jax wrote this whole thing :D
class Cars(Sprite):
    # Class to control cars
    def __init__(self, screen, settings):
        super(Cars, self).__init__()
        self.screen = screen
        self.image = self.randomize_cars()     # Randomise the images for cars
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.y = float(self.rect.y)
        self.speed_factor = random.uniform(settings.car_speed_minimum, settings.car_speed_maximum)   # randomise car speed

    def blitme(self):
        self.screen.blit(self.image, self.rect)    # Draw car on screen

    def update(self, score, settings,carsGroup):
        edge = self.check_edges()
        if edge:
            # check if cars hit the bottom,if so then reset to top(along with image and speed)
            self.reset_cars(score, settings,carsGroup)    
        else:
            # If not at the edge, then keep movig it down
            self.y += self.speed_factor
            self.rect.centery = self.y

    def check_edges(self):
        if self.rect.top >= 600:   # 600 is the bottom of the screen
            return True
        else:
            return False

    def randomize_cars(self):
        # randomise car images
        car_number = random.randint(1, 3)
        if car_number == 1:
            image = pygame.image.load('images/car1.png')
        elif car_number == 2:
            image = pygame.image.load('images/car2.png')
        elif car_number == 3:
            image = pygame.image.load('images/car3.png')
        return pygame.transform.scale(image, (90, 100))

    def reset_cars(self, score, settings, carsGroup):
        # Function to reset cars to the top of the screen if they hit bottom
        existing_lanes = gf.get_existing_lanes(carsGroup)   #check what lanes are occupied
        new_lane = gf.randomizeLanes()
        while new_lane in existing_lanes:
            new_lane = gf.randomizeLanes()
        self.rect.centery = 0
        self.rect.centerx = new_lane    # reset cars in their new lanes
        self.y = 0
        score.score += settings.score_scale      # increment score once cars reach bottom
        self.speed_factor = random.uniform(settings.car_speed_minimum, settings.car_speed_maximum)  #randomise new car speed