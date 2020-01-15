import pygame
import sys

def run_game():
    ''' Initialize all pygame modules'''
    pygame.init()
    ''' Pygame method responsible for background display'''
    screen = pygame.display.set_mode((1200,800))
    ''' Pygame method responsible for caption'''
    pygame.display.set_caption("Alien Invasion")
    ''' Main loop of the game'''
    
    while True:
        ''' Awaiting action from the user (all actions from the user are events)'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        ''' Pygame method responsible for refreshing the screen'''
        pygame.display.flip()

run_game()