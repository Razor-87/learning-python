# 31.08.2017
class Settings():
    """A class to store all settings."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1024
        self.screen_height = 768
        self.bg_color = (255, 255, 255)

        # Ball settings
        self.ball_speed = 1.2

        # Catcher settings
        self.catcher_speed = 1.1
