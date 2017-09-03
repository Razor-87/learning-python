# 01.09.2017
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

        # Random position
        self.x = randint(50, cat_settings.screen_width - 50)
        self.rect.x = self.x

    def ball_move(self):
        """Update the ball's position based on the movement flags."""
        self.rect.y += self.cat_settings.ball_speed

    def update(self):
        """Update the movement and position of the ball."""
        self.ball_move()

    def blitme(self):
        """Draw the ball at its current location."""
        self.screen.blit(self.image, self.rect)
