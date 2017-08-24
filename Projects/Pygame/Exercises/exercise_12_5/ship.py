# 24.08.2017
import pygame


class Ship():

    def __init__(self, ss_settings, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.ss_settings = ss_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the center left of the screen.
        self.rect.x = self.screen_rect.left
        self.rect.y = self.screen_rect.centery

        # Store a decimal value for the ship's center.
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_top = False
        self.moving_bottom = False

    def update(self):
        """Update the ship's position based on the movement flags."""
        # Update the ship's center value, not the rect.
        if self.moving_top and self.rect.top > self.screen_rect.top:
            self.y -= self.ss_settings.ship_speed_factor
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.ss_settings.ship_speed_factor

        # Update rect object from self.y.
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
