"""Handles ship image loading and rectangle setup."""

import pygame


class ShipImage:
    """Handles the image and rect for the Ship."""

    def __init__(self, image_path, screen_rect):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.midbottom = screen_rect.midbottom

    def get_rect(self):
        return self.rect

    def get_image(self):
        return self.image
