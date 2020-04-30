import pygame
from pygame.sprite import Sprite
import os
import final_models
 
pygame.init()
pygame.display.set_mode()
 
 
WIDTH = 1000
HEIGHT = 800
 
music = pygame.mixer.music.load(models.main_menu_music)
 
running = True
x = 2
screenSelect = 0
optionSelect = 0
all_sprites = pygame.sprite.Group()
 
musicvolume = 1
sfxvolume = 5
 
BLACK = (0,0,0)
 
def hitboxclick(x1, x2, y1, y2):
    if x1 < mousepos[0] < x2 and y1 < mousepos[1] < y2 and mouseclick[0]:
        return True
    else:
        return False
 
pygame.mixer.music.play(-1)
 
while running:
    pygame.mixer.music.set_volume(musicvolume)
    mousepos = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    mouseclick = pygame.mouse.get_pressed()
    display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
    # MAIN MENU SCREEN #
    if screenSelect == 0:
        all_sprites.draw(display_surface)
        display_surface.fill(BLACK)
        display_surface.blit(models.main_menu_bkgrnd, (20, 0))
        display_surface.blit(models.main_menu_begin, (50, 0))
        display_surface.blit(models.main_menu_options, (50, 150))
        display_surface.blit(models.main_menu_quit, (50, 300))
        if hitboxclick(345, 655, 570, 680):
            running = False
        elif hitboxclick(345, 655, 420, 530):
            screenSelect = 1
    # OPTIONS SCREEN #
    if screenSelect == 1:
        display_surface.fill(BLACK)
        if optionSelect == 0:
            display_surface.blit(models.options_title, (0,-325))
            display_surface.blit(models.options_audio, (-320, -100))
            display_surface.blit(models.options_backarrow, (-425, -300))
            if hitboxclick(5, 310, 210, 305):
                optionSelect = 1
            if hitboxclick(0, 100, 0, 95):
                screenSelect = 0
    # AUDIO SCREEN #
        elif optionSelect == 1:
            display_surface.blit(models.options_backarrow, (-425, -300))
            display_surface.blit(models.audio_title, (0,-325))
            display_surface.blit(models.options_add, (0, 0))
            display_surface.blit(models.options_subtract, (-75, 0))
            display_surface.blit(models.options_musictext, (-400, -175))
            if hitboxclick(0, 100, 0, 95):
                optionSelect = 0
            if hitboxclick(230, 465, -20, 220):
                musicvolume += .2
            elif hitboxclick(155, 195, 200, 210):
                musicvolume -= .2
 
    if keys[pygame.K_o]:
        print(mousepos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
 
    pygame.display.update()