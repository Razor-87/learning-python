# 21.08.2017
import pygame

from settings import Settings
import game_functions as gf


def run_game():
    # Initialize game, settings, and screen object.
    pygame.init()
    r_settings = Settings()
    screen = pygame.display.set_mode(
        (r_settings.screen_width, r_settings.screen_height))
    pygame.display.set_caption("Keys")

    # Start the main loop for the game.
    while True:
        gf.check_events()
        gf.update_screen(r_settings, screen)


run_game()
