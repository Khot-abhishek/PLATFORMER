# all game elements sprite classes 
from settings import *
import pygame as pg


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((30,40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(center = (WIDTH/2 ,HEIGHT/2))
        self.acc = pg.math.Vector2(0,0)
        self.vel = pg.math.Vector2(0,0)
        self.pos = pg.math.Vector2(WIDTH/2 ,HEIGHT/2)
        
        
    def update(self):
        self.acc = pg.math.Vector2(0,0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC
        
        #applying friction to player accelaraion      
        self.acc += self.vel * PLAYER_FRICTION 
        self.vel += self.acc
        self.pos += self.vel
        self.rect = self.pos     