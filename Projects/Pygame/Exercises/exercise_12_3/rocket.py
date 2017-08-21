# 21.08.2017
import pygame


class Rocket():

    def __init__(self, r_settings, screen):
        """Initialize the rocket and set its starting position."""
        self.screen = screen
        self.r_settings = r_settings

        # Load the rocket image and get its rect.
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new rocket at the center of the screen.
        self.rect.center = self.screen_rect.center

        # Store a decimal value for the rocket's center.
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False

    def update(self):
        """Update the rocket's position based on the movement flags."""
        # Update the rocket's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.r_settings.rocket_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.r_settings.rocket_speed_factor
        if self.moving_top and self.rect.top > self.screen_rect.top:
            self.centery -= self.r_settings.rocket_speed_factor
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.r_settings.rocket_speed_factor

        # Update rect object from self.center.
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """Draw the rocket at its current location."""
        self.screen.blit(self.image, self.rect)
