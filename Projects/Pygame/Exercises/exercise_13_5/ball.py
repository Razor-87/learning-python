# 29.08.2017
import pygame
from random import randint


class Ball():
    """A class to represent a ball."""

    def __init__(self, cat_settings, screen):
        """Initialize the ball and set its starting position."""
        self.screen = screen
        self.cat_settings = cat_settings

        # Load the ball image and set its rect attribute
        self.image = pygame.image.load('images/ball.bmp')
        self.rect = self.image.get_rect()

        # Start new ball on the top screen
        self.screen_rect = screen.get_rect()
        self.rect.y = self.screen_rect.top

        # Store the ball's exact position
        # self.y = float(self.rect.y)

        # Random position
        self.x = randint(0, cat_settings.screen_width)
        # self.x = float(random)
        self.rect.x = self.x

    # def update(self):
    #     """Update the catcher's position based on the movement flags."""
    #     # Update the catcher's center value, not the rect.

    #     # Update rect object from self.center.
    #     self.rect.centerx = self.center

    def blitme(self):
        """Draw the ball at its current location."""
        self.screen.blit(self.image, self.rect)
