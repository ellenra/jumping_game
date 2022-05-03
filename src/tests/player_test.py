import unittest
from player import *

class TestPlatform(unittest.TestCase):
    def setUp(self):
        self.position = POSITION
        self.size = SIZE
        self.velocity = VECTOR_0
        self.acceleration = VECTOR_0

    def test_players_position(self):
        self.assertEqual(self.position, VECTOR((250, 530)))

    def test_players_size(self):
        self.assertEqual(self.size, (30, 30))

    def test_players_velocity(self):
        self.assertEqual(self.velocity, VECTOR(0, 0))

    def test_players_acceleration(self):
        self.assertEqual(self.acceleration, VECTOR(0, 0))