import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.width,ai_settings.height))
    space_ship = Ship(ai_settings,screen)
    pygame.display.set_caption("Alien Invasion_2.0")

    while True:
        gf.check_events(space_ship)
        space_ship.update()
        gf.update_screen(ai_settings,screen,space_ship)
        
        

run_game()