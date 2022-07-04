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
        self.player = Player()
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


    
    