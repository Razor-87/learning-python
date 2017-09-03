# 03.09.2017
class Settings():
    """A class to store all settings."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (210, 210, 210)

        # Ball settings
        self.ball_speed = 1
        self.ball_out_limit = 3

        # Catcher settings
        self.catcher_speed = 2
