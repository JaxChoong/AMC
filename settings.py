
# *****************************************
# This file is written by JAX and CALVIN
# *****************************************

# Manages game settings
#(JAX)
class Settings():
    def __init__(self):
        self.running = False    # Running state of the game
        self.game_over = False   # Detect if the game is over
        self.screen_width = 350
        self.screen_height = 600
        self.bg_color = (115,115,115)
        
        # Settings for cars
        self.score_scale = 50
        self.car_speed_minimum = 2.0
        self.car_speed_maximum = 3.0

        # Settings for ebee
        self.ebee_speed_factor = 2

    #(CALVIN)
    def reset_game(self):
        self.running = False
        self.game_over = False

    #(JAX)
    def initialize_dynamic_settings(self):
       # Initialize settings that change throughout the game.
        self.ebee_speed_factor = 2
        self.score_scale = 50
        self.car_speed_minimum = 2.0
        self.car_speed_maximum = 3.0
