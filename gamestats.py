
class GameStats():
    """Tracks statistics for the game."""

    def __init__(self, settings):
        self.settings = settings
        self.reset_stats()

        # High score that should never be reset.

    def reset_stats(self):
        """Initialise statistics that can change during the game."""
        self.score = 0