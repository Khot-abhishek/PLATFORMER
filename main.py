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
        self.player = Player(self)
        self.all_sprites.add(self.player)
        
        #creating the platforms
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        
        # start running the game
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
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0   
        
        #scrolling the platform when the player reaches the top 1/4 of screen
        if self.player.rect.top <= HEIGHT / 4:
                self.player.pos.y += abs(self.player.vel.y)
                for plat in self.platforms:
                    plat.rect.y += abs(self.player.vel.y)
                    #deleting every platform that is outside the screen
                    if plat.rect.top > HEIGHT:
                        plat.kill()
        
        #creating new platforms to spawn as the old ones gets deleted
        while len(self.platforms) < 6:
            width = random.randrange(25,100)
            x = random.randrange(0, WIDTH-width)
            y = random.randrange(-40, -10)
            p = Platform(x,y,width,20)
            self.all_sprites.add(p)
            self.platforms.add(p)
            
    def draw(self):
        #drawing the updated elements
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
         # *after* drawing everything, flip the display
        pg.display.flip()
    
    def events(self):
        # check for all the game events
        for event in pg.event.get():
            # for closing the window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
                
    
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


    
    