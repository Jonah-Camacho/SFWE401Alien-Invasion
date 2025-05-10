# movement.py

class ShipMover:
    def __init__(self, settings, screen_rect, rect):
        self.settings = settings
        self.screen_rect = screen_rect
        self.rect = rect
        self.x = float(rect.x)
        self.moving_right = False
        self.moving_left = False

    def update_position(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x
