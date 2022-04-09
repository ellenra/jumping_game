
import unittest
from main import Player

class TestPlayer(unittest.Testcase):
    def setUp(self):
        self.player = Player()
    def player_size(self):
        self.assertEqual(self.grid.size(), (30, 30))

