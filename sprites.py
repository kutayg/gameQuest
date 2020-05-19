#import libraries
import pygame as pg
from settings import *

#here is the Player class
class Player(pg.sprite.Sprite):
    #draws the player sprite and lets it initialize
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.hitpoints = 100
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    #checks if there's something in the player's way.  If there isn't, it makes the player move one tile.
    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx, dy):
            self.x += dx
            self.y += dy
        
    #prevents the player from moving through walls
    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False

    #repeating function that lets the module change the values
    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

#here is the Mob class
class Mob(pg.sprite.Sprite):
    #draws the mob sprite and lets it initialize
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
    
    #checking if the mob is on the same tile as the player. If it isn't, it makes the mob move toward the player.
    def update(self):
        if self.rect.x > self.game.player.rect.x:
            self.rect.x -= 1
        if self.rect.x < self.game.player.rect.x:
            self.rect.x += 1
        if self.rect.y > self.game.player.rect.y:
            self.rect.y -= 1
        if self.rect.y < self.game.player.rect.y:
            self.rect.y += 1

#here is the Wall class
class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(LIGHTGREY)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE