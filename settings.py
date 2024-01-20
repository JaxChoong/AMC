# Manages game settings
class Settings():
    def __init__(self):
        self.running = False    # Running state of the game
        self.game_over = False   # Detect if the game is over
        self.screen_width = 350
        self.screen_height = 600
        self.bg_color = (30,30,30)
        

        # Settings for cars
        self.car_speed_factor = 0.3
        self.score_scale = 50

        # Settings for ebee
        self.ebee_speed_factor = 0.3

    #def initialize_dynamic_settings(self):
    #    """Initialize settings that change throughout the game."""
    #    self.ebee_speed_factor = 0.3
    #    self.cars_speed_factor = 0.3
    #    self.score_scale = 50
