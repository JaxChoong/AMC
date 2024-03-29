import pygame.font

# **********************************
# This file is mostly from source
# **********************************

class Button():

    def __init__(self, settings, screen, msg):
        #Initialize screen attributes
        self.screen = screen
        self.screen_rect = screen.get_rect()
    
        # set the dimensions and properties of the button.
        self.width, self.height = 80, 50
        self.button_color = (255,0,0)
        self.text_color = (0,0,255)
        self.font = pygame.font.SysFont(None, 48)

        # center button
        self.rect = pygame.Rect(0,0, self.width , self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery  +  30

        # The button message needs to be prepped only once.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        # put text on button
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen .blit(self.msg_image,self.msg_image_rect)