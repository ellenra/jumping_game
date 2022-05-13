import unittest
from services.platforms import *
from main_functions import *

class TestPlatform(unittest.TestCase):
    def setUp(self):
        self.speed = SPEED
        self.surface = SURFACE
        self.moving = True
        self.surf = pygame.Surface((random.randint(50, 175), 13)) 
        self.surf.fill(DARKESTBLUE) 
        self.rect = self.surf.get_rect(center=(random.randint(0, SCREEN_WIDTH - 50), 
                                               random.randint(0, SCREEN_HEIGHT - 50)))

    def test_speed(self):
        x = self.speed
        self.assertTrue(-2<=x<=2)

    def test_surface_lenght(self):
        x = self.surface
        self.assertTrue(50<=x<=175)
        
    def test_moving(self):
        self.moving = True
        self.speed = 1
        self.rect.left = 550
        Platform.move(self)
        self.assertEqual(self.rect.right, 0)
        
    def test_moving_2(self):
        self.moving = True
        self.speed = -1
        self.rect.right = -500
        Platform.move(self)
        self.assertEqual(self.rect.left, 500)
        
    def test_creating_new_platforms(self):
        len(PLATFORMS) == 5
        newplatforms()
        self.assertEqual(len(PLATFORMS), 6)
        
