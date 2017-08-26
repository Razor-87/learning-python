# 26.08.2017
import pygame
from pygame.sprite import Group

from settings import Settings
import game_functions as gf


def run_game():
    # Initialize game, settings, and screen object.
    pygame.init()
    r_settings = Settings()
    screen = pygame.display.set_mode(
        (r_settings.screen_width, r_settings.screen_height))
    pygame.display.set_caption("Raindrops")

    # Make a group of raindrops.
    raindrops = Group()

    # Create the grid of raindrops.
    gf.create_grid(r_settings, screen, raindrops)

    # Start the main loop for the game.
    while True:
        gf.check_events(r_settings, screen)
        gf.update_raindrops(r_settings, raindrops)
        gf.update_screen(r_settings, screen, raindrops)


run_game()
