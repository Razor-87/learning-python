# 21.08.2017
import sys

import pygame


def check_keydown_events(event, rocket):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = True
    elif event.key == pygame.K_UP:
        rocket.moving_top = True
    elif event.key == pygame.K_DOWN:
        rocket.moving_bottom = True


def check_keyup_events(event, rocket):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = False
    elif event.key == pygame.K_UP:
        rocket.moving_top = False
    elif event.key == pygame.K_DOWN:
        rocket.moving_bottom = False


def check_events(rocket):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, rocket)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rocket)


def update_screen(r_settings, screen, rocket):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(r_settings.bg_color)
    rocket.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()
