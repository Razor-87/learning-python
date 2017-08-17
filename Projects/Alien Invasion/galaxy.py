# 17.08.2017
import pygame


class Galaxy():

    def __init__(self, screen):
        """Initialize the galaxy"""
        self.screen = screen
        self.image = pygame.image.load('images/galaxy.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
            """Draw the ship at its current location."""
            self.screen.blit(self.image, self.rect)
