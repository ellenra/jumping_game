import random
import pygame
from settings import *


SCREEN_HEIGHT = 550
SCREEN_WIDTH = 500



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
                
PLATFORM = Platform()
PLATFORMS = pygame.sprite.Group()
PLATFORMS.add(PLATFORM)

PLATFORM.surf = pygame.Surface((SCREEN_WIDTH, 30))
PLATFORM.surf.fill(DARKERBLUE)
PLATFORM.rect = PLATFORM.surf.get_rect(center=(round(SCREEN_WIDTH/2), round(SCREEN_HEIGHT-10)))
PLATFORM.moving = False