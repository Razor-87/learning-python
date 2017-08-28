# 28.08.2017
import pygame

from ball import Ball
from catcher import Catcher
from settings import Settings
import game_functions as gf


def run_game():
    # Initialize game, settings, and screen object.
    pygame.init()
    cat_settings = Settings()
    screen = pygame.display.set_mode(
        (cat_settings.screen_width, cat_settings.screen_height))
    pygame.display.set_caption("Catcher")

    # Create a ball and catcher.
    ball = Ball(cat_settings, screen)
    catcher = Catcher(cat_settings, screen)

    # Start the main loop for the game.
    while True:
        gf.check_events(cat_settings, screen)
        gf.update_ball(cat_settings, screen, ball)
        gf.update_catcher(cat_settings, screen, catcher)
        gf.update_screen(cat_settings, screen, ball, catcher)


run_game()
