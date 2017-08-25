# 25.08.2017
import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """A class to represent a single star in the grid."""

    def __init__(self, s_settings, screen):
        """Initialize the star and set its starting position."""
        super().__init__()
        self.screen = screen
        self.s_settings = s_settings

        # Load the star image and set its rect attribute.
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()

        # Start each new star near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the star's exact position.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the star at its current location."""
        self.screen.blit(self.image, self.rect)
