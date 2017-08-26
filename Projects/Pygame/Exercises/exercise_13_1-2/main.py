# 25.08.2017
import pygame
from pygame.sprite import Group

from settings import Settings
import game_functions as gf


def run_game():
    # Initialize game, settings, and screen object.
    pygame.init()
    s_settings = Settings()
    screen = pygame.display.set_mode(
        (s_settings.screen_width, s_settings.screen_height))
    pygame.display.set_caption("Stars")

    # Make a group of stars.
    stars = Group()

    # Create the grid of stars.
    gf.create_grid(s_settings, screen, stars)

    # Start the main loop for the game.
    while True:
        gf.check_events(s_settings, screen)
        gf.update_screen(s_settings, screen, stars)


run_game()
