import pygame
import sys
import random
from settings import Settings

settings = Settings()

def update_screen(screen, ebee,cars):
       screen.fill(settings.bg_color)
       ebee.blitme()
       cars.blitme()
       pygame.display.flip()

       
def check_events():
    #Respond to keypresses and mouse events.
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Checks if user quits the game
                    sys.exit()
                
               # elif event.type == pygame.KEYDOWN:
               #     if(event.key==pygame.K_LEFT):
                         
                
                # elif event.type == pygame.KEYUP:
                #     check_keyup_events(event,ship)

                # elif event.type == pygame.MOUSEBUTTONDOWN:
                #     mouse_x, mouse_y = pygame.mouse.get_pos()
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




