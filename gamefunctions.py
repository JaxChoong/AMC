
# ***********************************************
# This file is written by JAX, CALVIN AND ERIC
# ***********************************************

import pygame
import sys
import random
from cars import Cars
import highest_score as hs
import sound as sfx

# initialise scrolling background
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
    # Update the screen every time the game loops
    screen.fill(settings.bg_color)
    if(settings.running):#ERIC ADDED SCROLLING BACKGROUND
      posY_bg += scrollspeed
      screen.blit(resizedbg,(0,posY_bg))
      posY_dupbg += scrollspeed
      screen.blit(dupbg,(0,posY_dupbg))
    if(posY_bg>=600):
      posY_bg = -600
    if(posY_dupbg>=600):
       posY_dupbg = -600
    # redraws everything on screen
    else:
      screen.blit(resizedbg,(0,posY_bg))
      screen.blit(dupbg,(0,posY_dupbg))
    ebee.blitme()
    carsGroup.draw(screen)
    score.prep_score(settings, screen)
    score.show_score(screen)

    #(CALVIN)
    if not settings.running:
        # Draw play button on the screen when game is not running
        play_button.draw_button()

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
                           ebee.moving_left=True           # Ebee move left flag
                      elif(event.key==pygame.K_RIGHT):
                           ebee.moving_right=True          # Ebee move right flag

                if event.type == pygame.KEYUP:
                      if(event.key == pygame.K_LEFT or event.key==pygame.K_RIGHT):
                           ebee.moving_left=False
                           ebee.moving_right=False
                
                #(CALVIN)
                elif event.type == pygame.MOUSEBUTTONDOWN:     # Check if user clicks the play button
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    check_play_button(settings, screen, score, play_button, ebee, carsGroup, mouse_x, mouse_y,existing_lanes)
                
                     
                
                
#(JAX AND CALVIN) 
def check_play_button(settings, screen, score, play_button, ebee, carsGroup, mouse_x, mouse_y,existing_lanes):
    # Start a new game when the player clicks Play.
    if play_button.rect.collidepoint(mouse_x,mouse_y):
        button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
        create_cars(screen,settings,existing_lanes,carsGroup)   # Creates first car once the game is started

        if button_clicked and not settings.running:
            # Reset the game settings
            #(CALVIN)
            if settings.game_over == True:
                settings.reset_game()

                #resets score
                score.reset_score()

                #Resets cars
                carsGroup.empty()       # Clears cars from screen
                settings.game_over = False
                settings.initialize_dynamic_settings()
                create_cars(screen,settings,existing_lanes,carsGroup)   # Creates a new car again
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
        lane = 180
    elif lane_number == 3:
        lane = 300
    return lane

#(JAX)
def check_ebee_cars_collisions(ebee,carsGroup,settings):
    collisions = pygame.sprite.spritecollide(ebee,carsGroup,False)   #Check if the rects of the cars and ebee collided.
    if collisions:
        sfx.explosionSfx.play() #this line was ERIC
        settings.car_speed_factor=0
        settings.running = False      # stop game if collided
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
def create_cars(screen, settings,existing_lanes, carsGroup):

    new_lane = randomizeLanes()
    while new_lane in existing_lanes:   # check if new lane is occupied by another car
        new_lane = randomizeLanes()  # Keep generating a new lane 

    car = Cars(screen,settings)
    carsGroup.add(car)           # Actually add cars in 
    existing_lanes.append(new_lane)

def get_existing_lanes(carsGroup):       # check what lanes are occupied currently
    existing_lanes = []
    for car in carsGroup:
        existing_lanes.append(car.rect.centerx)
    return existing_lanes

def scale_game_difficulty(settings,score,screen,existing_lanes,carsGroup):   #Function to scale up difficulty
    current_score = score.score
    if current_score == 300 and len(carsGroup)<2:
        sfx.carpassingSfx.play()
        create_cars(screen,settings, existing_lanes, carsGroup)     # Add car to group
        settings.score_scale += 50               # Scale up score for each car that is dodged
        settings.car_speed_minimum = 2.5
        settings.car_speed_maximum = 3.5
    elif current_score == 1000 and len(carsGroup)<3:
        sfx.carpassingSfx.play()
        settings.score_scale += 100              # Scale up score for each car that is dodged
        settings.ebee_speed_factor = 3           # Increase movement speed for ebee cuz why not
        settings.car_speed_minimum = 3.0
        settings.car_speed_maximum = 4.0

        # the min and max car speeds are the parameter for random() to run with