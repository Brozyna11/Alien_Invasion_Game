import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize all pygame modules
    pygame.init()
    # Creation of the object ai_settings as an example of the class Settings()
    ai_settings = Settings()
    # Pygame method responsible for background display resolution
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    # Pygame method responsible for caption
    pygame.display.set_caption("Alien Invasion")
    # Creating Ship object
    ship = Ship(ai_settings,screen)
    ''' Main loop of the game'''
    while True:
        ''' Awaiting action from the user (all actions from the user are events)'''
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship)
run_game()