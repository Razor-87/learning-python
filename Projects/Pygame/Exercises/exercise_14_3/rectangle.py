# 07.09.2017
import pygame


class Rectangle():
    """A class to represent a rectangle."""

    def __init__(self, ss_settings, screen):
        """Initialize the rectangle and set its starting position."""
        self.screen = screen
        self.ss_settings = ss_settings

        # Set the dimensions and properties of the rectangle.
        self.width, self.height = 20, 40
        self.rectangle_color = (50, 50, 50)
        self.screen_rect = screen.get_rect()

        # Build the rectangle's rect object and right it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.right = self.screen_rect.right
        self.rect.top = self.screen_rect.top + 5

        # Store a decimal value for the rectangle's center.
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if rectangle is at edges of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.top == screen_rect.top:
            return True
        elif self.rect.bottom == self.screen_rect.bottom:
            return True

    def update(self):
        """Update the rectangle's position."""
        # Update the rectangle's center value, not the rect.
        self.y += (self.ss_settings.rectangle_speed_factor *
                   self.ss_settings.rectangle_direction)

        # Update rect object from self.y.
        self.rect.y = self.y

    def draw_rectangle(self):
        """Draw the rectangle at its current location."""
        self.screen.fill(self.rectangle_color, self.rect)
