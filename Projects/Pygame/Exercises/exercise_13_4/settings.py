# 27.08.2017
class Settings():
    """A class to store all settings."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1100
        self.screen_height = 800
        self.bg_color = (200, 200, 200)

        # Raindrop settings.
        self.raindrop_speed_factor = 1
