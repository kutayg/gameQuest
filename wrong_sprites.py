# Sprite classes for platform game
# © 2019 KidsCanCode LLC / All rights reserved.
# Import libraries, import directly from Sprite
import pygame as pg
from pygame.sprite import Sprite
from settings import *
vec = pg.math.Vector2

# this is the player class
class Player(Sprite):
    # include game parameter to pass game class as argument in main.
    # initializes player, gives it dimensions
    def __init__(self, game):
        Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((30, 40))
        # makes player purple
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.hitpoints = 100
    def myMethod(self):
        pass
    # player's shape continuously extends until it jumps, then the player resets.
    def jump(self):
        # allows player to jump
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        self.game.screen.fill(AQUA)
        # if the player hits a platform, it ricochets and comes back down (cannot go through platform)
        if hits: 
            self.vel.y = -15
    def update(self):
        self.acc = vec(0, 0.5)
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_d]:
            self.acc.x = PLAYER_ACC
        # w key does not do anything
        if keys[pg.K_w]:
            pass
            # self.acc.y = -PLAYER_ACC
        if keys[pg.K_s]:
            self.acc.y = PLAYER_ACC
        # Space key makes player jump, not the w key
        if keys[pg.K_SPACE]:
            self.jump()

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # self.acc.y += self.vel.y * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        if self.pos.y < 0:
            self.pos.y = HEIGHT
        if self.pos.y > HEIGHT:
            self.pos.y = 0

        self.rect.midbottom = self.pos
# this is the platform class
class Platform(Sprite):
    # initializes the dimensions for each platform
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        # makes all platforms orange
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y