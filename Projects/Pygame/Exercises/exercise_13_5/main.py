# 01.09.2017
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
        gf.check_events(cat_settings, screen, catcher)
        catcher.update()
        ball.update()
        gf.detect_collisions(cat_settings, screen, catcher, ball)
        gf.update_screen(cat_settings, screen, ball, catcher)


run_game()
