# all game elements sprite classes 
from settings import *
import pygame as pg


class Player(pg.sprite.Sprite):
    def __init__(self,Game):
        super().__init__()
        self.Game = Game
        self.image = pg.Surface((30,40))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect(center = (WIDTH/2 ,HEIGHT/2))
        self.acc = pg.math.Vector2(0,0)
        self.vel = pg.math.Vector2(0,0)
        self.pos = pg.math.Vector2(WIDTH/2 ,HEIGHT/2)
        
    def jump(self):
        #jump only if we are standing on a platform
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.Game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -PLAYER_JUMP
        
    def update(self):
        self.acc = pg.math.Vector2(0,PLAYER_GRAVITY)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC
        
        #kepping the player in the screen
        if self.rect.left > WIDTH:
            self.pos.x = -10
        if self.rect.right < 0:
            self.pos.x = WIDTH + 10
        
        #applying friction to player accelaraion      
        self.acc.x += self.vel.x * PLAYER_FRICTION 
        self.vel += self.acc    # increasing velocity according to accelaration
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos     
        

class Platform(pg.sprite.Sprite):
    def __init__(self,x,y,w,h):
        super().__init__()
        self.image = pg.Surface((w,h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(topleft=(x,y))
   