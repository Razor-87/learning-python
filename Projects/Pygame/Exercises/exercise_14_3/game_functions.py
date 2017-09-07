# 07.09.2017
import sys

import pygame
from bullet import Bullet


def check_keydown_events(event, ss_settings, screen, ship, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_UP:
        ship.moving_top = True
    elif event.key == pygame.K_DOWN:
        ship.moving_bottom = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ss_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_UP:
        ship.moving_top = False
    elif event.key == pygame.K_DOWN:
        ship.moving_bottom = False


def check_events(ss_settings, screen, stats, play_button, ship, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ss_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ss_settings, stats, play_button, bullets,
                              mouse_x, mouse_y)


def check_play_button(ss_settings, stats, play_button, bullets, mouse_x,
                      mouse_y):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game settings.
        ss_settings.initialize_dynamic_settings()

        # Start game
        start_game(stats, bullets)


def start_game(stats, bullets):
    """Start game."""
    # Reset the game statistics.
    stats.reset_stats()
    stats.game_active = True

    # Empty the list of rectangle and bullets.
    bullets.empty()


def fire_bullet(ss_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ss_settings.bullets_allowed:
        new_bullet = Bullet(ss_settings, screen, ship)
        bullets.add(new_bullet)


def bullet_check_hit(ss_settings, rectangle, bullets):
    """if ball rect crosses rectangle rect return True."""
    for bullet in bullets.sprites():
        if bullet.rect.colliderect(rectangle.rect):
            bullets.remove(bullet)


def detect_miss(ss_settings):
    """Detect miss."""
    ss_settings.bullet_miss_limit -= 1


def update_bullets(ss_settings, rectangle, bullets):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()

    # Check bullet hit
    bullet_check_hit(ss_settings, rectangle, bullets)

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.right >= ss_settings.screen_width:
            bullets.remove(bullet)
            detect_miss(ss_settings)


def check_screen_edges(ss_settings, rectangle):
    """Respond appropriately if any rectangle have reached an edge."""
    if rectangle.check_edges():
        change_rectangle_direction(ss_settings, rectangle)
        # Speed up game.
        ss_settings.increase_speed()


def change_rectangle_direction(ss_settings, rectangle):
    """Drop the entire fleet and change the fleet's direction."""
    rectangle.rect.y += ss_settings.rectangle_speed_factor
    ss_settings.rectangle_direction *= -1


def game_over_check(ss_settings, stats):
    """Check game over"""
    if ss_settings.bullet_miss_limit == 0:
        stats.game_active = False


def update_screen(ss_settings, screen, stats, ship, rectangle, bullets,
                  play_button):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ss_settings.bg_color)
    # Redraw all bullets behind ship.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    check_screen_edges(ss_settings, rectangle)
    rectangle.draw_rectangle()
    game_over_check(ss_settings, stats)

    # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()

    # Make the most recently drawn screen visible.
    pygame.display.flip()
