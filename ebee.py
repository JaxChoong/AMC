import pygame

# Class that manages behaviours of the ebee.
class Ebee():
    def __init__(self,screen):
        self.screen = screen
        
        #Load ebee and get its rect.
        self.image = pygame.image.load('images\ebee.png')     #import the ebee image
        self.image = pygame.transform.scale(self.image, (60, 100))      #resize ebee image
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start ebee at the bottom of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for ebee center
        self.center = float(self.rect.centerx)

    def blitme(self):
        # Draw ebee at its current location
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        # Center ebee on the screen.
        self.center = self.screen_rect.centerx
    
    #Movement for (Ebee) 
    def Ebee_movement(self):
<<<<<<< HEAD
        x=1
=======
        
        

>>>>>>> f32eed5132bf45679afe17deec919fcd605d53a3
