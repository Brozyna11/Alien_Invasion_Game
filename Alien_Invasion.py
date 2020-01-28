# importing necessary modules to run the game
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien


def run_game():
    """ Main function of the game"""
    # Initialization of the pygame module
    pygame.init()
    # Creation of the object settings as an example of class Settings which contains all general parameters of the game objects
    ai_settings = Settings()
    # Saving displayed screen in the variable screen as a return value from pygame.display method
    screen = pygame.display.set_mode((ai_settings.width,ai_settings.height))
    # creating project which will inherit from already created classes in the prepared modules
    space_ship = Ship(ai_settings,screen)
    alien_ship = Alien(ai_settings,screen)
    pygame.display.set_caption("Alien Invasion_2.0")
    # Creation of the object bullets as an example of class Group() which is a container class to hold and manage multiple Sprite objects
    bullets = Group()
    aliens = Group()
    # calling special function from game_functions module in order to create whole fleet of alien_ships
    gf.create_fleet(ai_settings,screen,space_ship,aliens)

    # Main lopp of the game
    while True:
        gf.check_events(ai_settings,screen,space_ship,bullets)
        space_ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,space_ship,aliens,bullets)
# calling main function to run the game       
run_game()