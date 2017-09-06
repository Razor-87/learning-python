# 06.09.2017
class Settings():
    """A class to store all settings."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1024
        self.screen_height = 768
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5

        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 10
        self.bullet_height = 3
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Rectangle settings
        self.rectangle_speed_factor = 0.5
