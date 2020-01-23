import sys
import pygame
from bullet import Bullet_Straight,Bullet_Left,Bullet_Right
from alien import Alien



def check_keydown_events(event,ai_settings,screen, space_ship, bullets):
    if event.key == pygame.K_RIGHT:
        space_ship.moving_right = True
        space_ship.update()
    if event.key == pygame.K_LEFT:
        space_ship.moving_left = True
        space_ship.update()
    if event.key == pygame.K_UP:
        space_ship.moving_up = True
        space_ship.update()
    if event.key == pygame.K_DOWN:
        space_ship.moving_down = True 
        space_ship.update()
    if event.key == pygame.K_w:
        fire_bullet_straight(ai_settings,screen,space_ship,bullets)
    if event.key == pygame.K_d:
        fire_bullet_right(ai_settings,screen,space_ship,bullets)
    if event.key == pygame.K_a:
        fire_bullet_left(ai_settings,screen,space_ship,bullets)
    if event.key == pygame.K_ESCAPE:
        sys.exit()

def check_keyup_events(event, space_ship):
    if event.key == pygame.K_RIGHT:
        space_ship.moving_right = False
    if event.key == pygame.K_LEFT:
        space_ship.moving_left = False
    if event.key == pygame.K_UP:
        space_ship.moving_up = False
    if event.key == pygame.K_DOWN:
        space_ship.moving_down = False


def check_events(ai_settings,screen,space_ship,bullets):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,space_ship,bullets)
        if event.type == pygame.KEYUP:
            check_keyup_events(event,space_ship)


def update_screen(ai_settings,screen,space_ship,aliens,bullets):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    space_ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()
    

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        elif bullet.rect.left >= 1700:
            bullets.remove(bullet)
        elif bullet.rect.right <= 0:
            bullets.remove(bullet)

def fire_bullet_straight(ai_settings,screen,space_ship,bullets):
        if len(bullets) < ai_settings.bullets_allowed:
            # Creation of the new bullet and adding it to the group of bullets
            new_bullet = Bullet_Straight(ai_settings,screen,space_ship)
            bullets.add(new_bullet)

def fire_bullet_right(ai_settings,screen,space_ship,bullets):
        if len(bullets) < ai_settings.bullets_allowed:
            # Creation of the new bullet and adding it to the group of bullets
            new_bullet = Bullet_Right(ai_settings,screen,space_ship)
            bullets.add(new_bullet)

def fire_bullet_left(ai_settings,screen,space_ship,bullets):
        if len(bullets) < ai_settings.bullets_allowed:
            # Creation of the new bullet and adding it to the group of bullets
            new_bullet = Bullet_Left(ai_settings,screen,space_ship)
            bullets.add(new_bullet)

def get_number_aliens_x(ai_settings,alien_width):
    available_space_x = ai_settings.width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width 
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings,screen,space_ship,aliens):
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,space_ship.rect.height,alien.rect.height)

    for row_number in range(number_rows):

        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)

def get_number_rows(ai_settings,ship_height,alien_height):
    available_space_y = (ai_settings.height - (3* alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

        




