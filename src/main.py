import time
import sys
import pygame
from login.main_login import LogInView
from main_functions import *

pygame.init()

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
            score = font.render(str(PLAYER.score - 1), True, (PINK))
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
    texty = font.render(str(PLAYER.score - 1), True, PINK)
    SCREEN.blit(texty, (SCREEN_WIDTH / 2 + 30, 10))

    for entity in ALL_SPRITES:
        SCREEN.blit(entity.surf, entity.rect)
        entity.move()

    pygame.display.update()
    CLOCK.tick(60)
