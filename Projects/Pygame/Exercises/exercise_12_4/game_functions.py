# 21.08.2017
import sys

import pygame


def check_events():
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            print(event.key)


def update_screen(r_settings, screen):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(r_settings.bg_color)

    # Make the most recently drawn screen visible.
    pygame.display.flip()
