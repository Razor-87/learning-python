# 07.09.2017
class Settings():
    """A class to store all settings."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Bullet settings
        self.bullet_width = 10
        self.bullet_height = 3
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        self.bullet_miss_limit = 3

        # How quickly the game speeds up
        self.speedup_scale = 1.05
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.1
        self.bullet_speed_factor = 2
        self.rectangle_speed_factor = 0.1

        # rectangle_direction of 1 represents bottom; -1 repressents top
        self.rectangle_direction = 1

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.rectangle_speed_factor *= self.speedup_scale
