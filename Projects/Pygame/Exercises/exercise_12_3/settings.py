# 21.08.2017
class Settings():
    """A class to store all settings."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1440
        self.screen_height = 900
        self.bg_color = (0, 0, 0)

        # Rocket settings
        self.rocket_speed_factor = 1.5
