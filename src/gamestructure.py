import random
import time
import sys
import pygame


pygame.init()


SCREEN_HEIGHT = 550
SCREEN_WIDTH = 500


VECTOR = pygame.math.Vector2


PINK = (255, 153, 204)
YELLOW = (255, 255, 51)
LIGHTBLUE = (176, 224, 230)
DARKERBLUE = (123, 213, 213)
DARKESTBLUE = (86, 186, 206)



ACC = 0.5
FRIC = -0.12



CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
SCREEN.fill(LIGHTBLUE)


pygame.display.set_caption("Jump Until You Die")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.jumping = False
        self.surf = pygame.Surface((30, 30))
        self.surf.fill(PINK)
        self.rect = self.surf.get_rect()

        self.position = VECTOR((250, 530))
        self.velocity = VECTOR(0, 0)
        self.acceleration = VECTOR(0, 0)

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


class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((7.5, 7.5))
        self.surf.fill(YELLOW)
        self.rect = self.surf.get_rect(center=(random.randint(0, SCREEN_WIDTH - 50),
                                               random.randint(0, SCREEN_HEIGHT - 50)))
        self.speed = 0
        self.moving = True

    def move(self):
        if self.moving is True:
            self.rect.move_ip(self.speed, 0)

    def update(self):
        coincollision = pygame.sprite.spritecollide(self, COINS, False)
        for coi in COINS:
            if coincollision:
                change_color(coi)

def change_color(coi):
    coi.surf.fill(LIGHTBLUE)


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

def platform_collision(platform, groupies):
    if pygame.sprite.spritecollideany(platform, groupies):
        return True

    for thing in groupies:
        if thing == platform:
            continue
        if (abs(platform.rect.top - thing.rect.bottom) < 50) and \
            (abs(platform.rect.bottom - thing.rect.top) < 50):
            return True

def coin_collision(coin, groupies):
    if pygame.sprite.spritecollideany(coin, groupies):
        return True
    for i in groupies:
        if i == PLATFORM:
            continue
        if (abs(PLATFORM.rect.top - i.rect.bottom) < 50) and \
            (abs(PLATFORM.rect.bottom - i.rect.top) < 50):
            return True

def newplatforms():
    while len(PLATFORMS) < 6:
        width = random.randrange(50, 175)
        plat = Platform()
        is_true = True

        while is_true:
            plat = Platform()
            plat.rect.center = (random.randrange(0, SCREEN_WIDTH - width),
                                random.randrange(-50, 0))
            is_true = platform_collision(plat, PLATFORMS)
        PLATFORMS.add(plat)
        ALL_SPRITES.add(plat)

def newcoins():
    while len(COINS) < 3:
        coin = Coins()
        is_true = True

        while is_true:
            coin = Coins()
            coin.rect.center = (random.randrange(0, SCREEN_WIDTH - 10),
                                random.randrange(-50, 0))
            is_true = coin_collision(coin, COINS)
        COINS.add(coin)
        ALL_SPRITES.add(coin)


PLATFORM = Platform()
PLAYER = Player()
COIN = Coins()

PLATFORM.surf = pygame.Surface((SCREEN_WIDTH, 30))
PLATFORM.surf.fill(DARKERBLUE)
PLATFORM.rect = PLATFORM.surf.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT-10))
PLATFORM.moving = False



ALL_SPRITES = pygame.sprite.Group()
PLATFORMS = pygame.sprite.Group()
COINS = pygame.sprite.Group()

ALL_SPRITES.add(PLATFORM,
                PLAYER,
                COIN)
PLATFORMS.add(PLATFORM)
COINS.add(COIN)


for i in range(random.randint(4, 5)):
    is_true = True
    new_platform = Platform()
    new_coins = Coins()

    while is_true:
        new_platform = Platform()
        new_coins = Coins()
        is_true = platform_collision(new_platform, PLATFORMS)

    PLATFORMS.add(new_platform)
    ALL_SPRITES.add(new_platform)
    ALL_SPRITES.add(new_coins)
    COINS.add(new_coins)


while True:
    PLAYER.update()
    COIN.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.key == pygame.K_UP:
                PLAYER.jump()



    if PLAYER.rect.top <= SCREEN_HEIGHT / 2.5:
        PLAYER.position.y += abs(PLAYER.velocity.y)
        for i in PLATFORMS:
            i.rect.y += abs(PLAYER.velocity.y)
            if i.rect.top >= SCREEN_HEIGHT:
                i.kill()



    if PLAYER.rect.top > SCREEN_HEIGHT:
        for i in ALL_SPRITES:
            i.kill()
            time.sleep(0.5)
            SCREEN.fill(LIGHTBLUE)
            font = pygame.font.SysFont("Adobe Myungjo Std Orta", 32)
            text = font.render("Better luck next time!", True, (PINK))
            SCREEN.blit(text, (SCREEN_WIDTH / 3.6, SCREEN_HEIGHT / 2))
            pygame.display.update()
            time.sleep(1.75)
            pygame.quit()
            sys.exit()

    newplatforms()
    newcoins()
    SCREEN.fill(LIGHTBLUE)

    for entity in ALL_SPRITES:
        SCREEN.blit(entity.surf, entity.rect)
        entity.move()

    pygame.display.update()
    CLOCK.tick(60)
