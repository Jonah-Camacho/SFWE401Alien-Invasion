import pygame.font

class Credit:
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 600,150
        self.credit_color = (255, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None,150)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)
    def _prep_msg(self, msg):

        self.msg_image = self.font.render(msg, True, self.text_color, self.credit_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    

    def draw_credit(self):
        self.screen.fill(self.credit_color,  self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)