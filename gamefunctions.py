import pygame
import sys
from ebee import Ebee
from cars import Cars

def update_screen(screen, ebee,cars):
       pygame.display.flip()
       ebee.blitme()
       cars.blitme()

       
def check_events():
    #Respond to keypresses and mouse events.
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Checks if user quits the game
                    sys.exit()
                
                # elif event.type == pygame.KEYDOWN:
                #     check_keydown_events(event,screen)
                
                # elif event.type == pygame.KEYUP:
                #     check_keyup_events(event,ship)

                # elif event.type == pygame.MOUSEBUTTONDOWN:
                #     mouse_x, mouse_y = pygame.mouse.get_pos()
                #     check_play_button(ai_settings, screen, stats, sb,  play_button, ship, aliens, bullets, mouse_x, mouse_y)
                    



