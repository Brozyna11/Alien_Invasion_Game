import sys
import pygame


def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
        ship.update()
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
        ship.update()
    if event.key == pygame.K_UP:
        ship.moving_up = True
        ship.update()
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
        ship.update()

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            print(event.key)
            check_keydown_events(event,ship)
        if event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def update_screen(settings,screen,ship):
    screen.fill(settings.bg_color)
    ship.blitme()
    pygame.display.flip()
    
