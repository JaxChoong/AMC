import pygame

class Score():
    def __init__(self, settings, screen):
        """Initialize scorekeeping attributes."""
        self.score = 0
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings

        # Font settings for scoring information
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,54)

        #initiallize the attribute to be used in leaderboard
        self.added_to_leaderboard = False

        #Prepare the initial score images.
        self.prep_score(settings, screen)
        # self.prep_high_score()

    def reset_score(self):
        self.score = 0
        #same thing but this is for when the game resets
        self.added_to_leaderboard = False

    def prep_score(self, settings, screen):
        """Turn the score into a rendered image."""
        rounded_score = int(round(self.score,-1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, settings.bg_color)

        #Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = self.screen_rect.centerx
        self.score_rect.top = 20

    def show_score(self, screen):
        """Draw scores and levels to screen."""
        self.screen.blit(self.score_image, self.score_rect)
        # self.screen.blit(self.high_score_image,self.high_score_rect)
        # self.screen.blit(self.level_image, self.level_rect)

