import unittest
from services.player import *


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.position = POSITION
        self.size = SIZE
        self.velocity = VECTOR_0
        self.acceleration = VECTOR_0
        self.jumping = False
        self.surf = pygame.Surface(SIZE)
        self.surf.fill(PINK)
        self.rect = self.surf.get_rect()
        self.score = 0

    def test_players_position(self):
        self.assertEqual(self.position, VECTOR((250, 530)))

    def test_players_size(self):
        self.assertEqual(self.size, (30, 30))

    def test_players_velocity(self):
        self.assertEqual(self.velocity, VECTOR(0, 0))

    def test_players_acceleration(self):
        self.assertEqual(self.acceleration, VECTOR(0, 0))
    
    def test_jumping(self):
        collisions = pygame.sprite.spritecollide(self, PLATFORMS, False)
        Player.jump(self)
        if collisions and not self.jumping:
            self.assertEqual(self.jumping, True)
            
    def test_prevent_jump(self):
        Player.no_jump(self)
        self.jumping = True
        if self.jumping:
            if self.velocity.y < -3:
                self.assertEqual(self.velocity.y, -3)   
                
    def test_position_when_moving(self):
        self.position.x = 510
        Player.move(self)
        self.assertEqual(self.position.x, 0)
        
    def test_position_when_moving_2(self):
        self.position.x = -10
        Player.move(self)
        self.assertEqual(self.position.x, 500)
        
    def test_score_when_does_not_hit_platform(self):
        self.velocity.y = -1
        Player.update(self)
        self.assertEqual(self.score, 0)
