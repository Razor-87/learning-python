# 28.08.2017
import pygame


class Ball():
    """A class to represent a ball."""

    def __init__(self, cat_settings, screen):
        """Initialize the ball and set its starting position."""
        self.screen = screen
        self.cat_settings = cat_settings

        # Load the ball image and set its rect attribute.
        self.image = pygame.image.load('images/ball.bmp')
        self.rect = self.image.get_rect()

        # Start new ball on the top screen.
        self.rect.y = self.rext.height

        # Store the ball's exact position.
        self.y = float(self.rect.y)

    def blitme(self):
        """Draw the ball at its current location."""
        self.screen.blit(self.image, self.rect)
