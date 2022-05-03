import random as rand
import time
import sys
import pygame
from player import PLAYER, PLATFORMS, ALL_SPRITES, PINK, SCREEN_WIDTH
from settings import SCREEN, LIGHTBLUE, CLOCK, SCREEN_HEIGHT
from platforms import Platform
from login.main_login import LogInView

pygame.init()

def platform_collision(platform, groupies):
    if pygame.sprite.spritecollideany(platform, groupies):
        return True
    for thing in groupies:
        if thing == platform:
            continue
        if (abs(platform.rect.top - thing.rect.bottom) < 50) and \
            (abs(platform.rect.bottom - thing.rect.top) < 50):
            return True
    return None


def newplatforms():
    while len(PLATFORMS) < 6:
        width = rand.randrange(50, 175)
        plat = Platform()
        true = True

        while true:
            plat = Platform()
            plat.rect.center = (rand.randrange(0, SCREEN_WIDTH - width),
                                 rand.randrange(-50, 0))
            true = platform_collision(plat, PLATFORMS)
        PLATFORMS.add(plat)
        ALL_SPRITES.add(plat)


for i in range(rand.randint(4, 5)):
    IS_TRUE = True
    new_platform = Platform()

    while IS_TRUE:
        new_platform = Platform()
        IS_TRUE = platform_collision(new_platform, PLATFORMS)

    PLATFORMS.add(new_platform)
    ALL_SPRITES.add(new_platform)


SCREEN.fill(LIGHTBLUE)
pygame.display.set_caption("Jump Until You Die")


while True:
    PLAYER.update()

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
            i.rect.y += abs(int(PLAYER.velocity.y))
            if i.rect.top >= SCREEN_HEIGHT:
                i.kill()

    if PLAYER.rect.top > SCREEN_HEIGHT:
        for i in ALL_SPRITES:
            i.kill()
            time.sleep(0.5)
            SCREEN.fill(LIGHTBLUE)
            font = pygame.font.SysFont("Adobe Myungjo Std Orta", 38)
            text_1 = font.render("Your Score : ", True, (PINK))
            SCREEN.blit(text_1, (SCREEN_WIDTH / 3, SCREEN_HEIGHT / 2 - 70))
            score = font.render(str(PLAYER.score), True, (PINK))
            SCREEN.blit(score,(SCREEN_WIDTH / 2 - 20, SCREEN_HEIGHT / 2 - 20))
            text = font.render("Better luck next time!", True, (PINK))
            SCREEN.blit(text, (SCREEN_WIDTH / 3.6, SCREEN_HEIGHT / 2 + 50))
            pygame.display.update()
            time.sleep(3)
            pygame.quit()
            sys.exit()

    newplatforms()
    SCREEN.fill(LIGHTBLUE)

    font = pygame.font.SysFont("Adobe Myungjo Std Orta", 38)
    texty = font.render("Score :", True, PINK)
    SCREEN.blit(texty, (SCREEN_WIDTH / 2 - 70, 10))

    font = pygame.font.SysFont("Adobe Myungjo Std Orta", 38)
    texty = font.render(str(PLAYER.score), True, PINK)
    SCREEN.blit(texty, (SCREEN_WIDTH / 2 + 30, 10))

    for entity in ALL_SPRITES:
        SCREEN.blit(entity.surf, entity.rect)
        entity.move()

    pygame.display.update()
    CLOCK.tick(60)
