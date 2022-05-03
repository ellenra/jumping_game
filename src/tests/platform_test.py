import unittest
from platforms import *

class TestPlatform(unittest.TestCase):
    def setUp(self):
        self.speed = SPEED
        self.surface = SURFACE

    def test_speed(self):
        x = self.speed
        self.assertTrue(-2<=x<=2)

    def test_surface_lenght(self):
        x = self.surface
        self.assertTrue(50<=x<=175)
