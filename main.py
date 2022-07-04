import random,sys
import pygame as pg
from settings import *
from my_sprites import *

class Game():
    def __init__(self):
        # initializing all game elements
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
    
    def new(self):
        # starting a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player()
        p1 = Platform(0,HEIGHT-40, WIDTH, 40)
        self.all_sprites.add(p1)
        self.platforms.add(p1)
        p2 = Platform(WIDTH/2-40,HEIGHT*3/4, 100, 40)
        self.all_sprites.add(p2)
        self.platforms.add(p2)
        self.all_sprites.add(self.player)
        self.run()
    
    def run(self):
        # this will be our main game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    
    def update(self):
        # updating all elements after taking the events
        self.all_sprites.update()
        hits = pg.sprite.spritecollide(self.player, self.platforms, False)
        if hits:
            self.player.pos.y = hits[0].rect.top
            self.player.vel.y = 0   
            
            
    def draw(self):
        #drawing the updated elements
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pg.display.flip()
    
    def events(self):
        # check for all the game events
        for event in pg.event.get():
            # for closing the window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
                
    
    def show_start_screen(self):
        pass
    
    def show_go_screen(self):
        pass
    
    
g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()
    
pg.quit()


    
    