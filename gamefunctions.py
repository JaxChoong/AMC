
# ***********************************************
# This file is written by JAX, CALVIN AND ERIC
# ***********************************************

import pygame
import sys
import random
from cars import Cars
import highest_score as hs
import sound as sfx

oriroadbg=pygame.image.load("images/roadnice.png")
resizedbg=pygame.transform.scale(oriroadbg, (350,600))
dupbg=pygame.transform.scale(oriroadbg, (350,600))
posY_bg=0
posY_dupbg=-600
scrollspeed=0.7

#(JAX)
def update_screen(settings, screen, score, play_button, ebee, carsGroup):
    global posY_bg
    global posY_dupbg
    # Update the screen every time th game loops
    screen.fill(settings.bg_color)
    if(settings.running):#ERIC ADDED SCROLLING BACKGROUND AND IT IS MAKING EVERYTHING SLOW NEEDS TO FIX
      posY_bg += scrollspeed
      screen.blit(resizedbg,(0,posY_bg))
      posY_dupbg += scrollspeed
      screen.blit(dupbg,(0,posY_dupbg))
    if(posY_bg>=600):
      posY_bg = -600
    if(posY_dupbg>=600):
       posY_dupbg = -600
    else:
      screen.blit(resizedbg,(0,posY_bg))
      screen.blit(dupbg,(0,posY_dupbg))
    ebee.blitme()
    carsGroup.draw(screen)
    score.prep_score(settings, screen)
    score.show_score(screen)

    #(CALVIN)
    if not settings.running:
        #play button
        play_button.draw_button()
        # lb.update_score_list(settings, score)

    #(ERIC)
    if settings.game_over:
        #  Initialize gameover screen
        show_game_over(settings,screen)
        #(CALVIN)
        hs.update_score_list(settings, score)
        hs.show_previous_highest_score(settings, screen)
    # Draws / shows newest screen.
    pygame.display.update()

#(ERIC)
def check_events(ebee, play_button,settings, screen, score, carsGroup, mouse_x, mouse_y,existing_lanes):
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
                
                #(CALVIN)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    check_play_button(settings, screen, score, play_button, ebee, carsGroup, mouse_x, mouse_y,existing_lanes)
                
                     
                
                
#(JAX AND CALVIN) 
def check_play_button(settings, screen, score, play_button, ebee, carsGroup, mouse_x, mouse_y,existing_lanes):
    # Start a new game when the player clicks Play.
    if play_button.rect.collidepoint(mouse_x,mouse_y):
        button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
        create_cars(screen,existing_lanes,carsGroup)
        if button_clicked and not settings.running:
            # Reset the game settings
            #(CALVIN)
            if settings.game_over == True:
                settings.reset_game()

                #resets score
                score.reset_score()

                #Resets cars
                carsGroup.empty()
                settings.game_over = False
                settings.initialize_dynamic_settings()
                create_cars(screen,existing_lanes,carsGroup)
            settings.running = True

            # Reset the scoreboard images.
            score.prep_score(settings, screen)

#(JAX)
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

#(JAX)
def check_ebee_cars_collisions(ebee,carsGroup,settings):
    collisions = pygame.sprite.spritecollide(ebee,carsGroup,False)   #Check if the rects of the cars and ebee collided.
    if collisions:
        sfx.explosionSfx.play() #this line was ERIC
        settings.car_speed_factor=0
        #show_game_over(ebee,settings, screen)
        settings.running = False
        settings.game_over = True

#(ERIC)
def show_game_over(settings, screen):
    #  Font settings for "Game Over"  text
     text_color = (255,0,0)
     font = pygame.font.SysFont(None,54)
     showgameover = font.render("Game Over", True, text_color, settings.bg_color)
     dest=(75,250)
     screen.blit(showgameover,dest)

# These lines are written by JAX
def create_cars(screen, existing_lanes, carsGroup):
    #clears existing lanes
    existing_lanes.clear()

    # Create a singular car with a unique lane
    new_lane = randomizeLanes()
    while new_lane in existing_lanes:
        new_lane = randomizeLanes()  # Keep generating a new lane until it's unique

    car = Cars(screen, new_lane)
    carsGroup.add(car)
    existing_lanes.append(new_lane)


def scale_game_difficulty(settings,score,screen,existing_lanes,carsGroup):   #Function to scale up difficulty
    current_score = score.score
    if current_score == 300:
        sfx.carpassingSfx.play()
        if len(carsGroup)<2:
            create_cars(screen, existing_lanes, carsGroup)
            settings.score_scale += 50
    elif current_score == 1000:
        if len(carsGroup)<3:
            create_cars(screen, existing_lanes, carsGroup)
            settings.score_scale += 100
    elif current_score == 5000:
        if len(carsGroup)<4:
            create_cars(screen, existing_lanes, carsGroup)
            settings.score_scale += 200
            settings.ebee_speed_factor = 0.5