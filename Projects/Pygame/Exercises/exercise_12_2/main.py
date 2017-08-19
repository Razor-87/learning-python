# 19.08.2017
import pygame

import game_functions as gf


class Settings():
    """A class to store all settings for Galaxy."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1440
        self.screen_height = 900
        self.bg_color = (0, 0, 0)


class Galaxy():

    def __init__(self, screen):
        """Initialize the galaxy"""
        self.screen = screen
        self.image = pygame.image.load('images/galaxy.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.center = self.screen_rect.center

    def blitme(self):
            """Draw the ship at its current location."""
            self.screen.blit(self.image, self.rect)


def run_game():
    # Initialize game, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Galaxy")

    # Make a galaxy
    galaxy = Galaxy(screen)

    # Start the main loop for the game.
    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, galaxy)


run_game()
