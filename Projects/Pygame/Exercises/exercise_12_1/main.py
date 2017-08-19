# 18.08.2017
import sys

import pygame


class Settings():
    """A class to store all settings for Galaxy."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1440
        self.screen_height = 900
        self.bg_color = (0, 0, 255)


def check_events():
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)

    # Make the most recently drawn screen visible.
    pygame.display.flip()


def run_game():
    # Initialize game, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Blue screen")

    # Start the main loop for the game.
    while True:
        check_events()
        update_screen(ai_settings, screen)


run_game()
