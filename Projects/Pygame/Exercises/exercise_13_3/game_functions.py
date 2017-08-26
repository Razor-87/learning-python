# 26.08.2017
import sys

import pygame
from raindrop import Raindrop


def check_events(r_settings, screen):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(r_settings, screen, raindrops):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(r_settings.bg_color)
    # Redraw raindrops.
    raindrops.draw(screen)
    # Make the most recently drawn screen visible.
    pygame.display.flip()


def get_number_raindrops_x(r_settings, raindrop_width):
    """Determine the number of raindrops that fit in a row."""
    available_space_x = r_settings.screen_width - raindrop_width
    number_raindrops_x = int(available_space_x / (2 * raindrop_width))
    return number_raindrops_x


def get_number_rows(r_settings, raindrop_height):
    """Determine the number of rows of raindrops that fit on the screen."""
    available_space_y = r_settings.screen_height - raindrop_height
    number_rows = int(available_space_y / (2 * raindrop_height))
    return number_rows


def create_raindrop(r_settings, screen, raindrops, raindrop_number,
                    row_number):
    """Create an raindrops and place it in the row."""
    raindrop = Raindrop(r_settings, screen)
    raindrop_width = raindrop.rect.width
    raindrop.x = raindrop_width + 2 * raindrop_width * raindrop_number
    raindrop.rect.x = raindrop.x
    raindrop.rect.y = (raindrop.rect.height + 2 * raindrop.rect.height *
                       row_number)
    raindrops.add(raindrop)


def create_grid(r_settings, screen, raindrops):
    """Create a full grid of raindrops."""
    # Create an raindrop and find the number of raindrops in a row.
    raindrop = Raindrop(r_settings, screen)
    number_raindrops_x = get_number_raindrops_x(r_settings,
                                                raindrop.rect.width)
    number_rows = get_number_rows(r_settings, raindrop.rect.height)
    # Create the grid of raindrops.
    for row_number in range(number_rows):
        for raindrop_number in range(number_raindrops_x):
            create_raindrop(r_settings, screen, raindrops,
                            raindrop_number, row_number)


def check_grid_bottom(r_settings, raindrops):
    """Respond appropriately if any raindrops have reached an edge."""
    for raindrop in raindrops.sprites():
        if raindrop.check_bottom():
            raindrops.remove(raindrop)
            break


def grid_raindrops_move(r_settings, raindrops):
    """Drop the entire fleet and change the fleet's direction."""
    for raindrop in raindrops.sprites():
        raindrop.rect.y += (1 +
                            (raindrop.rect.height / r_settings.screen_height))


def update_raindrops(r_settings, raindrops):
    """Update the positions of all raindrops in the grid."""
    grid_raindrops_move(r_settings, raindrops)
    check_grid_bottom(r_settings, raindrops)
    raindrops.update()
