# 07.09.2017
import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from rectangle import Rectangle
import game_functions as gf


def run_game():
    # Initialize game, settings, and screen object.
    pygame.init()
    ss_settings = Settings()
    screen = pygame.display.set_mode(
        (ss_settings.screen_width, ss_settings.screen_height))
    pygame.display.set_caption("Sideways Shooter")

    # Make the Play button.
    play_button = Button(screen, "Play")

    # Create an instance to store game statistics.
    stats = GameStats(ss_settings)

    # Make a ship
    ship = Ship(ss_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()
    # Make a rectangle
    rectangle = Rectangle(ss_settings, screen)

    # Start the main loop for the game.
    while True:
        gf.check_events(ss_settings, screen, stats, play_button, ship,
                        bullets)

        if stats.game_active:
            ship.update()
            rectangle.update()
            gf.update_bullets(ss_settings, rectangle, bullets)

        gf.update_screen(ss_settings, screen, stats, ship, rectangle, bullets,
                         play_button)


run_game()
