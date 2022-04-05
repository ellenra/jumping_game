(en saa pygamea toimimaan tällä koneella ja poetryä toisella joten testien teko ei onnistunut vielä)

import unittest
from gamestructure import Player

class TestPlayer(unittest.Testcase):
    def setUp(self):
        self.player = Player()
    def player_size(self):
        self.assertEqual(self.grid.size(), (30, 30))

