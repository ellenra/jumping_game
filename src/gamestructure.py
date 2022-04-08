import pygame, random, sys, time

pygame.init()

 

screen_height = 550
screen_width = 500


vector = pygame.math.Vector2


pink = (255, 153, 204)
yellow = (255, 255, 51)
lightblue = (176, 224, 230)
darkerblue = (123, 213, 213)
darkestblue = (86, 186, 206)



ACC = 0.5
FRIC = -0.12



clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill(lightblue)


pygame.display.set_caption("Jump Until You Die")


class Player(pygame.sprite.Sprite):
    def __init__(self, x = 0, y = 0):
        super(Player, self).__init__() 
        self.jumping = False
        self.surf = pygame.Surface((30, 30))
        self.surf.fill(pink)
        self.rect = self.surf.get_rect()

        self.position = vector((250, 530))
        self.velocity = vector(0,0)
        self.acceleration = vector(0,0)

    def move(self):
        self.acceleration = vector(0, 0.4)
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_LEFT]:
            self.acceleration.x = -ACC

        if pressed_keys[pygame.K_RIGHT]:
            self.acceleration.x = ACC
                
        self.acceleration.x += self.velocity.x * FRIC
        self.velocity += self.acceleration
        self.position += self.velocity + 0.4 * self.acceleration

        if self.position.x > screen_width:
            self.position.x = 0
        if self.position.x < 0:

            self.position.x = screen_width            

        self.rect.midbottom = self.position

    def jump(self): 
        collisions = pygame.sprite.spritecollide(self, platforms, False)

        if collisions and not self.jumping:
           self.jumping = True
           self.velocity.y = -15

 

    def no_jump(self):
        if self.jumping:
            if self.velocity.y < -3:
                self.velocity.y = -3

 

    def update(self):
        collisions = pygame.sprite.spritecollide(self, platforms, False)
        if self.velocity.y > 0:        
            if collisions:
                if self.position.y < collisions[0].rect.bottom:
                    self.position.y = collisions[0].rect.top +1
                    self.velocity.y = 0
                    self.jumping = False


class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super(Coins, self).__init__()
        self.surf = pygame.Surface((7.5, 7.5))
        self.surf.fill(yellow)
        self.rect = self.surf.get_rect(center = (random.randint(0, screen_width - 50),

                                                 random.randint(0, screen_height - 50))) 
        self.speed = 0
        self.moving = True

    def move(self):
        if self.moving == True:
            self.rect.move_ip(self.speed, 0)

            

    def update(self):
        coincollision = pygame.sprite.spritecollide(self, coins, False)
        for i in coins:
            if coincollision:
                change_color(i)

def change_color(i):
    i.surf.fill(lightblue)
    pygame.display.update


class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super(Platform, self).__init__()
        self.surf = pygame.Surface((random.randint(50, 175), 13))
        self.surf.fill(darkestblue)
        self.rect = self.surf.get_rect(center = (random.randint(0, screen_width - 50),

                                                 random.randint(0, screen_height - 50)))
        self.speed = random.randint(-2, 2)
        self.moving = True

    def move(self):
        if self.moving == True:  
            self.rect.move_ip(self.speed, 0)

            if self.speed > 0 and self.rect.left > screen_width:
                self.rect.right = 0

            if self.speed < 0 and self.rect.right < 0:
                self.rect.left = screen_width

def platform_collision(platform, groupies):
    if pygame.sprite.spritecollideany(platform, groupies):
        return True
    else:
        for i in groupies:
            if i == platform:
                continue
            if (abs(platform.rect.top - i.rect.bottom) < 50) and (abs(platform.rect.bottom - i.rect.top) < 50):
                return True
        C = False

def coin_collision(coin, groupies):
    if pygame.sprite.spritecollideany(coin, groupies):
        return True
    else:
        for i in groupies:
            if i == platform:
                continue
            if (abs(platform.rect.top - i.rect.bottom) < 50) and (abs(platform.rect.bottom - i.rect.top) < 50):
                return True
        C = False
 

def newplatforms():
    while len(platforms) < 6:
        width = random.randrange(50, 175)
        p  = Platform()      
        C = True

        while C:
             p = Platform()
             p.rect.center = (random.randrange(0, screen_width - width),
                              random.randrange(-50, 0))
             C = platform_collision(p, platforms)
        platforms.add(p)
        all_sprites.add(p)

def newcoins():
    while len(coins) < 3:
        p  = Platform()      
        C = True

        while C:
             p = Coins()
             p.rect.center = (random.randrange(0, screen_width - 10),

                              random.randrange(-50, 0))
             C = coin_collision(p, platforms)
        coins.add(p)
        all_sprites.add(p)


platform = Platform()
player = Player()
coin = Coins()

platform.surf = pygame.Surface((screen_width, 30))
platform.surf.fill(darkerblue)
platform.rect = platform.surf.get_rect(center = (screen_width / 2, screen_height - 10))
platform.moving = False 



all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
coins = pygame.sprite.Group()



all_sprites.add(platform, 

                player,

                coin)
platforms.add(platform)
coins.add(coin)

 

for i in range(random.randint(4, 5)):
    C = True
    new_platform = Platform()
    new_coins = Coins()

    while C:
        new_platform = Platform()
        new_coins = Coins()
        C = platform_collision(new_platform, platforms)

    platforms.add(new_platform)
    all_sprites.add(new_platform)
    all_sprites.add(new_coins)
    coins.add(new_coins)

 

while True:
    player.update()
    coin.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.key == pygame.K_UP:
                player.jump()



    if player.rect.top <= screen_height / 2.5:
        player.position.y += abs(player.velocity.y)
        for i in platforms:
            i.rect.y += abs(player.velocity.y)
            if i.rect.top >= screen_height:
                i.kill()



    if player.rect.top > screen_height:
        for i in all_sprites:
            i.kill()
            time.sleep(0.5)
            screen.fill(lightblue)
            font = pygame.font.SysFont("Adobe Myungjo Std Orta", 32)
            text = font.render("Better luck next time!", True, (pink))
            screen.blit(text, (screen_width / 3.6, screen_height / 2))
            pygame.display.update()
            time.sleep(1.75)
            pygame.quit()
            sys.exit()

    newplatforms()
    newcoins()
    screen.fill(lightblue)

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
        entity.move()

    pygame.display.update()
    clock.tick(60)
    
    
    
    
    
    
    
    
    
    
    