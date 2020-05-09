'''
import pygame
from os import path
 
pygame.init()
pygame.display.set_mode()
 
def load_data():
    global game_folder
    game_folder = path.dirname(__file__)
    print("here's the game folder " + game_folder)
 
load_data()
main_menu_bkgrnd = pygame.image.load(game_folder + r"\Emate's Arc\Main Menu Items\Emate's Arc Main Menu Background.png")
main_menu_begin = pygame.transform.scale(pygame.image.load(game_folder + r"\Emate's Arc\Main Menu Items\Emate's Arc Main Begin Button.png").convert_alpha(), (900,650))
main_menu_quit = pygame.transform.scale(pygame.image.load(game_folder + r"\Emate's Arc\Main Menu Items\Emate's Arc Main Quit Button.png").convert_alpha(), (900,650))
main_menu_options = pygame.transform.scale(pygame.image.load(game_folder + r"\Emate's Arc\Main Menu Items\Emate's Arc Main Options Button.png").convert_alpha(), (900,650))
options_title = pygame.image.load(game_folder + r"\Emate's Arc\Options Screen Items\Emate's Arc Options Title.png").convert_alpha()
options_audio = pygame.image.load(game_folder + r"\Emate's Arc\Options Screen Items\Emate's Arc Audio Button.png").convert_alpha()
options_controls = pygame.image.load(game_folder + r"\Emate's Arc\Options Screen Items\Emate's Arc Controls Button.png").convert_alpha()
options_backarrow = pygame.image.load(game_folder + r"\Emate's Arc\Options Screen Items\Emate's Arc Back Button.png").convert_alpha()
options_add = pygame.transform.scale(pygame.image.load(game_folder + r"\Emate's Arc\Options Screen Items\Emate's Arc Add Button.png").convert_alpha(), (500,400))
options_subtract = pygame.transform.scale(pygame.image.load(game_folder + r"\Emate's Arc\Options Screen Items\Emate's Arc Subtract Button.png").convert_alpha(), (500,400))
options_offnotifier = pygame.image.load(game_folder + r"\Emate's Arc\Options Screen Items\Emate's Arc Off Notifier.png").convert_alpha()
options_onnotifier = pygame.image.load(game_folder + r"\Emate's Arc\Options Screen Items\Emate's Arc On Notifier.png").convert_alpha()
options_musictext = pygame.image.load(game_folder + r"\Emate's Arc\Options Screen Items\Emate's Arc Music Text.png").convert_alpha()
audio_title = pygame.image.load(game_folder + r"\Emate's Arc\Options Screen Items\Emate's Arc Audio Title.png").convert_alpha()
main_menu_music = (game_folder + r"\Emate's Arc\Main Menu Items\Main Menu Music.mp3")

'''