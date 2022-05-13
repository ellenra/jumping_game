import unittest
from services.settings import *
from login.login_settings import *

class TestSettings(unittest.TestCase):
    def setUp(self):
        self.height = SCREEN_HEIGHT
        self.width = SCREEN_WIDTH
        self.pink = PINK
        self.lightblue = LIGHTBLUE
        self.darkerblue = DARKERBLUE
        self.darkestblue = DARKESTBLUE
        self.acceleration = ACC
        self.fric = FRIC

    def test_height(self):
        self.assertEqual(self.height, 550)

    def test_width(self):
        self.assertEqual(self.width, 500)

    def test_pink(self):
        self.assertEqual(self.pink, (255, 153, 204))

    def test_lightblue(self):
        self.assertEqual(self.lightblue, (176, 224, 230))

    def test_darkerblue(self):
        self.assertEqual(self.darkerblue, (123, 213, 213))

    def test_darkestblue(self):
        self.assertEqual(self.darkestblue, (86, 186, 206))

    def test_acceleration(self):
        self.assertEqual(self.acceleration, 0.5)

    def test_fric(self):
        self.assertEqual(self.fric, -0.12)
        
class TestLogInSettings(unittest.TestCase):
    def setUp(self):
        self.window = window
        self.geometry = GEOMETRY
    
    def test_geometry_is_right(self):
        self.assertEqual(self.geometry, "400x200")
