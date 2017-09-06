# 06.09.2017
import pygame


class Rectangle():
    """A class to represent a rectangle."""

    def __init__(self, ss_settings, screen):
        """Initialize the rectangle and set its starting position."""
        self.screen = screen
        self.ss_settings = ss_settings

        # Set the dimensions and properties of the rectangle.
        self.width, self.height = 100, 50
        self.rectangle_color = (0, 0, 0)
        self.screen_rect = screen.get_rect()

        # Build the rectangle's rect object and right it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.right = self.screen_rect.right - 10
        self.rect.top = self.screen_rect.top

        # Store a decimal value for the rectangle's center.
        self.y = float(self.rect.y)

    def rectangle_move_up(self):
        """Update the ball's position based on the movement flags."""
        self.y -= self.ss_settings.rectangle_speed_factor

    def rectangle_move_down(self):
        """Update the ball's position based on the movement flags."""
        self.y += self.ss_settings.rectangle_speed_factor

    def directions(self):
        """Directions"""
        if self.rect.top == self.screen_rect.top:
            return 0
        else:
            return False
        if self.rect.bottom == self.screen_rect.bottom:
            return 1
        else:
            return False

    def update(self):
        """Update the rectangle's position."""
        # Update the rectangle's center value, not the rect.
        if self.directions():
            direction = self.directions()
            if direction == 0:
                self.rectangle_move_down()
            if direction == 1:
                self.rectangle_move_up()
            print(direction)

        # Update rect object from self.y.
        self.rect.y = self.y

    def draw_rectangle(self):
        """Draw the rectangle at its current location."""
        self.screen.fill(self.rectangle_color, self.rect)
