import random
import time
import sys
import pygame
from player import *
from login import *
from tkinter import Tk

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


for i in range(random.randint(4, 5)):
    is_true = True
    new_platform = Platform()

    while is_true:
        new_platform = Platform()
        is_true = platform_collision(new_platform, PLATFORMS)

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
            font = pygame.font.SysFont("Adobe Myungjo Std Orta", 32)
            text = font.render("Better luck next time!", True, (PINK))
            SCREEN.blit(text, (SCREEN_WIDTH / 3.6, SCREEN_HEIGHT / 2))
            pygame.display.update()
            time.sleep(1.75)
            pygame.quit()
            sys.exit()

    newplatforms()
    SCREEN.fill(LIGHTBLUE)

    for entity in ALL_SPRITES:
        SCREEN.blit(entity.surf, entity.rect)
        entity.move()

    pygame.display.update()
    CLOCK.tick(60)

