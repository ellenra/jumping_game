import random
import pygame


SCREEN_HEIGHT = 550
SCREEN_WIDTH = 500

DARKESTBLUE = (86, 186, 206)


class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super(Platform, self).__init__()
        self.surf = pygame.Surface((random.randint(50, 175), 13))
        self.surf.fill(DARKESTBLUE)
        self.rect = self.surf.get_rect(center=(random.randint(0, SCREEN_WIDTH - 50),
                                               random.randint(0, SCREEN_HEIGHT - 50)))
        self.speed = random.randint(-2, 2)
        self.moving = True

    def move(self):
        if self.moving is True:
            self.rect.move_ip(self.speed, 0)

            if self.speed > 0 and self.rect.left > SCREEN_WIDTH:
                self.rect.right = 0

            if self.speed < 0 and self.rect.right < 0:
                self.rect.left = SCREEN_WIDTH