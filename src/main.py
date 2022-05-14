import time
import sys
import random as rand
import pygame
from services.player import PLAYER, PLATFORMS, ALL_SPRITES, PINK, SCREEN_WIDTH
from services.platforms import Platform
from services.settings import SCREEN, LIGHTBLUE, CLOCK, SCREEN_HEIGHT
from login.main_login import LogInView
from main_functions import platform_collision, newplatforms

pygame.init()


for i in range(rand.randint(4, 5)):
    IS_TRUE = True
    new_platform = Platform()

    while IS_TRUE:
        new_platform = Platform()
        IS_TRUE = platform_collision(new_platform, PLATFORMS)

    PLATFORMS.add(new_platform)
    ALL_SPRITES.add(new_platform)

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
            font = pygame.font.SysFont("Adobe Myungjo Std Orta", 40)
            text_1 = font.render("Your Score : ", True, (PINK))
            SCREEN.blit(text_1, (round(SCREEN_WIDTH / 3), round(SCREEN_HEIGHT - 500)))
            score = font.render(str(PLAYER.score - 1), True, (PINK))
            SCREEN.blit(score, (round(SCREEN_WIDTH - 260), round(SCREEN_HEIGHT - 450)))
            text = font.render("BETTER LUCK NEXT TIME!", True, (PINK))
            SCREEN.blit(text, (round(SCREEN_WIDTH - 417), round(SCREEN_HEIGHT - 370)))
            pygame.display.update()
            time.sleep(3)
            pygame.quit()
            sys.exit()

    newplatforms()
    SCREEN.fill(LIGHTBLUE)

    FONT_2 = pygame.font.SysFont("Adobe Myungjo Std Orta", 38)
    SCORE_TEXT = FONT_2.render("Score :", True, PINK)
    SCREEN.blit(SCORE_TEXT, (round(SCREEN_WIDTH / 2 - 70), 10))

    SCORE_POINTS = FONT_2.render(str(PLAYER.score - 1), True, PINK)
    SCREEN.blit(SCORE_POINTS, (round(SCREEN_WIDTH / 2 + 30), 10))

    for entity in ALL_SPRITES:
        SCREEN.blit(entity.surf, entity.rect)
        entity.move()

    pygame.display.update()
    CLOCK.tick(60)
