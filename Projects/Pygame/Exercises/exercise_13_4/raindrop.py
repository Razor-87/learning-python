# 27.08.2017
import pygame
from pygame.sprite import Sprite


class Raindrop(Sprite):
    """A class to represent a single raindrop in the grid."""

    def __init__(self, r_settings, screen):
        """Initialize the raindrop and set its starting position."""
        super().__init__()
        self.screen = screen
        self.r_settings = r_settings

        # Load the raindrop image and set its rect attribute.
        self.image = pygame.image.load('images/raindrop.bmp')
        self.rect = self.image.get_rect()

        # Start each new raindrop near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the raindrop's exact position.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the raindrop at its current location."""
        self.screen.blit(self.image, self.rect)

    def check_bottom(self):
        """Return True if raindrop is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True
