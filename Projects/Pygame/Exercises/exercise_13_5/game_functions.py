# 29.08.2017
import sys

import pygame
# from ball import Ball
# from catcher import Catcher


def check_keydown_events(event, cat_settings, screen, catcher):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        catcher.moving_right = True
    elif event.key == pygame.K_LEFT:
        catcher.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, catcher):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        catcher.moving_right = False
    elif event.key == pygame.K_LEFT:
        catcher.moving_left = False


def check_events(cat_settings, screen, catcher):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, cat_settings, screen, catcher)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, catcher)


def update_screen(cat_settings, screen, catcher, ball):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop
    screen.fill(cat_settings.bg_color)

    # Draw catcher and ball
    catcher.blitme()
    ball.blitme()

    # Make the most recently drawn screen visible
    pygame.display.flip()
