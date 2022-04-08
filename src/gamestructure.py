import random
import time
import sys
import pygame


pygame.init()


SCREEN_HEIGHT = 550
SCREEN_WIDTH = 500


vector = pygame.math.Vector2


PINK = (255, 153, 204)
YELLOW = (255, 255, 51)
LIGHTBLUE = (176, 224, 230)
DARKERBLUE = (123, 213, 213)
DARKESTBLUE = (86, 186, 206)



ACC = 0.5
FRIC = -0.12



clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(LIGHTBLUE)


pygame.display.set_caption("Jump Until You Die")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.jumping = False
        self.surf = pygame.Surface((30, 30))
        self.surf.fill(PINK)
        self.rect = self.surf.get_rect()

        self.position = vector((250, 530))
        self.velocity = vector(0, 0)
        self.acceleration = vector(0, 0)

    def move(self):
        self.acceleration = vector(0, 0.4)
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
        collisions = pygame.sprite.spritecollide(self, platforms, False)

        if collisions and not self.jumping:
            self.jumping = True
            self.velocity.y = -15


    def no_jump(self):
        if self.jumping:
            if self.velocity.y < -3:
                self.velocity.y = -3



    def update(self):
        collisions = pygame.sprite.spritecollide(self, platforms, False)
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
        self.rect = self.surf.get_rect(center = (random.randint(0, SCREEN_WIDTH - 50),
                                                random.randint(0, SCREEN_HEIGHT - 50)))
        self.speed = 0
        self.moving = True

    def move(self):
        if self.moving is True:
            self.rect.move_ip(self.speed, 0)

    def update(self):
        coincollision = pygame.sprite.spritecollide(self, coins, False)
        for coi in coins:
            if coincollision:
                change_color(coi)

def change_color(coi):
    coi.surf.fill(LIGHTBLUE)


class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super(Platform, self).__init__()
        self.surf = pygame.Surface((random.randint(50, 175), 13))
        self.surf.fill(DARKESTBLUE)
        self.rect = self.surf.get_rect(center = (random.randint(0, SCREEN_WIDTH - 50),
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
    else:
        for thing in groupies:
            if thing == platform:
                continue
            if (abs(platform.rect.top - thing.rect.bottom) < 50) and \
                (abs(platform.rect.bottom - thing.rect.top) < 50):
                return True
        C = False

def coin_collision(coin, groupies):
    if pygame.sprite.spritecollideany(coin, groupies):
        return True
    else:
        for i in groupies:
            if i == platform:
                continue
            if (abs(platform.rect.top - i.rect.bottom) < 50) and \
                (abs(platform.rect.bottom - i.rect.top) < 50):
                return True

def newplatforms():
    while len(platforms) < 6:
        width = random.randrange(50, 175)
        p = Platform()
        C = True

        while C:
            p = Platform()
            p.rect.center = (random.randrange(0, SCREEN_WIDTH - width),
                             random.randrange(-50, 0))
            C = platform_collision(p, platforms)
        platforms.add(p)
        all_sprites.add(p)

def newcoins():
    while len(coins) < 3:
        p = Platform()
        C = True

        while C:
            p = Coins()
            p.rect.center = (random.randrange(0, SCREEN_WIDTH - 10),
                             random.randrange(-50, 0))
            C = coin_collision(p, platforms)
        coins.add(p)
        all_sprites.add(p)


platform = Platform()
player = Player()
coin = Coins()

platform.surf = pygame.Surface((SCREEN_WIDTH, 30))
platform.surf.fill(DARKERBLUE)
platform.rect = platform.surf.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT-10))
platform.moving = False



all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
coins = pygame.sprite.Group()

all_sprites.add(platform,
                player,
                coin)
platforms.add(platform)
coins.add(coin)


for i in range(random.randint(4, 5)):
    C = True
    new_platform = Platform()
    new_coins = Coins()

    while C:
        new_platform = Platform()
        new_coins = Coins()
        C = platform_collision(new_platform, platforms)

    platforms.add(new_platform)
    all_sprites.add(new_platform)
    all_sprites.add(new_coins)
    coins.add(new_coins)


while True:
    player.update()
    coin.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.key == pygame.K_UP:
                player.jump()



    if player.rect.top <= SCREEN_HEIGHT / 2.5:
        player.position.y += abs(player.velocity.y)
        for i in platforms:
            i.rect.y += abs(player.velocity.y)
            if i.rect.top >= SCREEN_HEIGHT:
                i.kill()



    if player.rect.top > SCREEN_HEIGHT:
        for i in all_sprites:
            i.kill()
            time.sleep(0.5)
            screen.fill(LIGHTBLUE)
            font = pygame.font.SysFont("Adobe Myungjo Std Orta", 32)
            text = font.render("Better luck next time!", True, (PINK))
            screen.blit(text, (SCREEN_WIDTH / 3.6, SCREEN_HEIGHT / 2))
            pygame.display.update()
            time.sleep(1.75)
            pygame.quit()
            sys.exit()

    newplatforms()
    newcoins()
    screen.fill(LIGHTBLUE)

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
        entity.move()

    pygame.display.update()
    clock.tick(60)




