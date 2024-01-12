import pygame
import sys
import random
from settings import Settings
from time import sleep

settings = Settings()

def update_screen(screen, ebee,cars):
       screen.fill(settings.bg_color)
       ebee.blitme()
       cars.blitme()
       pygame.display.flip()

       
def check_events(ebee):
    #Respond to keypresses and mouse events.
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Checks if user quits the game
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                      if(event.key==pygame.K_LEFT):
                           ebee.moving_left=True
                      elif(event.key==pygame.K_RIGHT):
                           ebee.moving_right=True

                if event.type == pygame.KEYUP:
                      if(event.key == pygame.K_LEFT or event.key==pygame.K_RIGHT):
                           ebee.moving_left=False
                           ebee.moving_right=False
                            
                #elif event.type == pygame.MOUSEBUTTONDOWN:
                     #mouse_x, mouse_y = pygame.mouse.get_pos()
                #     check_play_button(ai_settings, screen, stats, sb,  play_button, ship, aliens, bullets, mouse_x, mouse_y)
                    

def randomizeLanes():
    # Function to randomise lanes for cars
    lane_number = random.randint(1,3)
    if lane_number == 1:
        lane = 50
    elif lane_number == 2:
        lane = 170
    elif lane_number == 3:
        lane = 300
    return lane

def check_ebee_cars_collisions(ebee,cars):
    collisions = pygame.sprite.collide_rect(ebee,cars)   #Check if the rects of the cars and ebee collided.
    if collisions:
        sleep(0.1)    #Turns of screen for SOMETIME
