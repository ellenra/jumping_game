import unittest
import sys

sys.path.append('./src/platforms.py')

from platforms import Platform

class TestLogIn(unittest.Testcase):
    def setUp(self):
        self.platform = Platform()
    def test_platform_movement(self):
        self.platform.speed = 2
        self.platform.rect.left = 600
        self.assertEqual(self.platform.rect.right, 0)

