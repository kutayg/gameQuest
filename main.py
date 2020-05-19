# Sources: KidsCanCode - Game Development with Pygame video series Tile-based game - Part 1  Video link: https://youtu.be/3UxnelT9aCo
#Edited by Ethan Lee, Alex Paulen, Mr. Cozort, and Kutay Gokcen.
#Here is the main file, it contains the game class and sets up the tiles as well as movement.
#Imports
import pygame as pg
import sys
import math
import random
import string
from os import path
from settings import *
from sprites import *
 
#possible maps, spawns one randomly at play
posMap = ('map.txt', 'map1.txt')
 
#chooses a random map
mapVar = random.choice(posMap)
#Defines the class: Game 
class Game:
    #init the game
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        #sets clock
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        #calls load_data
        self.load_data()
    #loads the data by pointing to files on the pc, (map) and draws in lines.
    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map_data = []
        #mapVar makes it random and spawns map from map or map1
        with open(path.join(game_folder, mapVar)) as f:
            for line in f:
                self.map_data.append(line)
    #defines the code that is needed for changing map and map1.txt to sprites and walls.
    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.mob = Mob(self, 30, 30)
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                #If 1, goes to wall
                if tile == '1':
                    Wall(self, col, row)
                #If P, spawns player
                if tile == 'P':
                    self.player = Player(self, col, row)
                #If M, spawns Mob.
                if tile == 'M':
                    self.mob = Mob(self, col, row)
    #Defines the run fn for the game loop and draw pg
    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()
 
    def quit(self):
        pg.quit()
        sys.exit()
 
    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        #Checks for collisions for sprites
        hits = pg.sprite.spritecollide(self.player, self.mobs, False)
        if hits:
            print("ouch!")
            self.quit()
    #Draws the grid on the game window
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))
    #draw fn from pg, used to make the sprites appear and the bg appear
    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()
    #defines the events such as quit, and arrow key movement.
    def events(self):
        # catch all events here
        for event in pg.event.get():
            #If you click the x button, the game quits
            if event.type == pg.QUIT:
                self.quit()
            #Arrow keys corresponding to movement.
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_LEFT:
                    self.player.move(dx=-1)
                if event.key == pg.K_RIGHT:
                    self.player.move(dx=1)
                if event.key == pg.K_UP:
                    self.player.move(dy=-1)
                if event.key == pg.K_DOWN:
                    self.player.move(dy=1)
 
    def show_start_screen(self):
        pass
 
    def show_go_screen(self):
        pass
 
# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()