"""Ship class for controlling the player's spaceship."""
import pygame
from pygame.sprite import Sprite
from movement import ShipMover


class Ship(Sprite):
    """Represents the player's ship in the game."""

    def __init__(self, ai_game):
        """Initialize the ship and its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load("Human_ship.bmp")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.mover = ShipMover(self.settings, self.screen_rect, self.rect)

    def update(self, *args, **kwargs):
        """Update the ship’s position using the ShipMover."""
        self.mover.update_position()

    def blit_me(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.mover.x = float(self.rect.x)
