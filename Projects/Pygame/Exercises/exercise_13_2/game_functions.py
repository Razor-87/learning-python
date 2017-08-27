# 25.08.2017
import sys

import pygame
from random import randint
from star import Star


def check_events(s_settings, screen):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(s_settings, screen, stars):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(s_settings.bg_color)
    # Redraw stars.
    stars.draw(screen)
    # Make the most recently drawn screen visible.
    pygame.display.flip()


def get_number_stars_x(s_settings, star_width):
    """Determine the number of stars that fit in a row."""
    available_space_x = s_settings.screen_width - star_width
    number_stars_x = int(available_space_x / (2 * star_width))
    return number_stars_x


def get_number_rows(s_settings, star_height):
    """Determine the number of rows of stars that fit on the screen."""
    available_space_y = s_settings.screen_height - star_height
    number_rows = int(available_space_y / star_height)
    return number_rows


def create_star(s_settings, screen, stars, star_number, row_number):
    """Create an stars and place it in the row."""
    star = Star(s_settings, screen)
    star_width = star.rect.width
    random = randint(-5, 5)
    star.x = star_width + random * star_width * star_number
    star.rect.x = star.x
    star.rect.y = star.rect.height + random * star.rect.height * row_number
    stars.add(star)


def create_grid(s_settings, screen, stars):
    """Create a full grid of stars."""
    # Create an star and find the number of stars in a row.
    star = Star(s_settings, screen)
    number_stars_x = get_number_stars_x(s_settings, star.rect.width)
    number_rows = get_number_rows(s_settings, star.rect.height)

    # Create the grid of stars.
    for row_number in range(number_rows):
        for star_number in range(number_stars_x):
            create_star(s_settings, screen, stars, star_number, row_number)
