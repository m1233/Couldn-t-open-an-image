# Pygame template - skeleton for future projects
import pygame as pg
import random
from game_options import *
from sprites import *

class Game:
    def __init__(self):
        pg.init()   
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("BRUH")
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        self.SPAWNENEMIES = 1
        self.my_event = pg.event.Event(self.SPAWNENEMIES)
        pg.event.post(self.my_event)
        pg.time.set_timer(self.SPAWNENEMIES, 3000)

        self.spawnpoint1 = 20, -80
        self.spawnpoint2 = 140, -80
        self.spawnpoint3 = 260, -80
        self.spawnpoint4 = 380, -80
        self.spawnpoint5 = 500, -80
        self.spawnpoints = (self.spawnpoint1,self.spawnpoint2,self.spawnpoint3,self.spawnpoint4,self.spawnpoint5)

        self.all_sprites = pg.sprite.Group()
        self.blocks = pg.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.blocks)
        g.run()
        

    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

            if event.type == self.SPAWNENEMIES:
                num = random.randint(0,len(self.spawnpoints))
                print(num)
                for i in range(5):
                    if num != i:
                        print(i)
                        self.block = Block(self.spawnpoints[i])
                        self.blocks.add(self.block)
                        self.all_sprites.add(self.blocks)    


        dead_blocks = pg.sprite.spritecollide(self.player, self.blocks, True)

        # if dead_blocks:
        #     self.running = False

    def draw(self):
        self.screen.fill(MY_RED)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

g = Game()
while g.running:
    g.new()

pg.quit()
