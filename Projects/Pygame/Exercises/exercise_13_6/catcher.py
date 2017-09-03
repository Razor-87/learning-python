# 29.08.2017
import pygame


class Catcher():
    """A class to represent a catcher."""

    def __init__(self, cat_settings, screen):
        """Initialize the catcher and set its starting position."""
        self.screen = screen
        self.cat_settings = cat_settings

        # Load the catcher image and set its rect attribute
        self.image = pygame.image.load('images/catcher.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start catcher at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the catcher's center.
        self.center = float(self.rect.centerx)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the catcher's position based on the movement flags."""
        # Update the catcher's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.cat_settings.catcher_speed
        if self.moving_left and self.rect.left > 0:
            self.center -= self.cat_settings.catcher_speed

        # Update rect object from self.center.
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the catcher at its current location."""
        self.screen.blit(self.image, self.rect)
