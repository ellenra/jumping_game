import pygame
from settings import PINK, VECTOR, ACC, FRIC
from platforms import SCREEN_WIDTH, PLATFORMS, PLATFORM

POSITION = VECTOR((250, 530))
SIZE = (30, 30)
VECTOR_0 = VECTOR(0, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.jumping = False
        self.surf = pygame.Surface(SIZE)
        self.surf.fill(PINK)
        self.rect = self.surf.get_rect()

        self.position = POSITION
        self.velocity = VECTOR_0
        self.acceleration = VECTOR_0

    def move(self):
        self.acceleration = VECTOR(0, 0.4)
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_LEFT]:
            self.acceleration.x = -ACC

        if pressed_keys[pygame.K_RIGHT]:
            self.acceleration.x = ACC

        self.acceleration.x += self.velocity.x * FRIC
        self.velocity += self.acceleration
        self.position += self.velocity + 0.4 * self.acceleration

        if self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH

        self.rect.midbottom = self.position


    def jump(self):
        collisions = pygame.sprite.spritecollide(self, PLATFORMS, False)

        if collisions and not self.jumping:
            self.jumping = True
            self.velocity.y = -15

    def no_jump(self):
        if self.jumping:
            if self.velocity.y < -3:
                self.velocity.y = -3

    def update(self):
        collisions = pygame.sprite.spritecollide(self, PLATFORMS, False)
        if self.velocity.y > 0:
            if collisions:
                if self.position.y < collisions[0].rect.bottom:
                    self.position.y = collisions[0].rect.top +1
                    self.velocity.y = 0
                    self.jumping = False

PLAYER = Player()
ALL_SPRITES = pygame.sprite.Group()

ALL_SPRITES.add(PLATFORM,
                PLAYER)
