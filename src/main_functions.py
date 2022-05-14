import random as rand
import pygame
from services.player import PLATFORMS, ALL_SPRITES, SCREEN_WIDTH
from services.platforms import Platform
from services.settings import SCREEN, LIGHTBLUE
SCREEN.fill(LIGHTBLUE)
pygame.display.set_caption("Jump Until You Die")

def platform_collision(platform, groupies):
    """Käsittelee liikkuvien objektien törmäyksiä.

    Args:
        platform: Liikkuva taso.
        groupies: Tasoon törmäävä objekti.

    Returns:
        True jos törmäys, muuten None.
    """
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
    """Funktio, joka on vastuussa uusien tasojen luomisesta.
    """
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
