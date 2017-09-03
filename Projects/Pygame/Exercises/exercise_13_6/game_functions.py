# 03.09.2017
import sys

import pygame
from random import randint


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


def ball_check_bottom(cat_settings, screen, ball):
    """Ball up if ball is at bottom of screen."""
    screen_rect = ball.screen.get_rect()
    if ball.rect.y >= screen_rect.bottom:
        ball_up(cat_settings, screen, ball)
        cat_settings.ball_out_limit -= 1


def ball_check_catcher(cat_settings, screen, catcher, ball):
    """if ball rect crosses catcher rect return True."""
    if ball.rect.left < catcher.rect.left:
        return False
    if ball.rect.right > catcher.rect.right:
        return False
    if ball.rect.y < catcher.rect.top:
        return False
    else:
        return True


def ball_up(cat_settings, screen, ball):
    """Move ball up."""
    ball.rect.y = ball.screen_rect.top
    ball.x = randint(50, ball.cat_settings.screen_width - 50)
    ball.rect.x = ball.x


def detect_collisions(cat_settings, screen, catcher, ball):
    """Detect collisions."""
    ball_check_bottom(cat_settings, screen, ball)
    if ball_check_catcher(cat_settings, screen, catcher, ball):
        ball_up(cat_settings, screen, ball)


def game_over_check(cat_settings):
    """Check game over"""
    if cat_settings.ball_out_limit > 0:
        return True
    else:
        return False


def update_screen(cat_settings, screen, catcher, ball):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop
    screen.fill(cat_settings.bg_color)
    # Draw catcher and ball
    catcher.blitme()
    ball.blitme()
    # Make the most recently drawn screen visible
    pygame.display.flip()
