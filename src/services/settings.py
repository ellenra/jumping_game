import pygame
pygame.init()
pygame.time.Clock()


SCREEN_HEIGHT = 550
SCREEN_WIDTH = 500

CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

VECTOR = pygame.math.Vector2


PINK = (255, 153, 204)
YELLOW = (255, 255, 51)
LIGHTBLUE = (176, 224, 230)
DARKERBLUE = (123, 213, 213)
DARKESTBLUE = (86, 186, 206)

ACC = 0.5
FRIC = -0.12
