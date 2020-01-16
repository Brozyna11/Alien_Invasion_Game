import sys,pygame

def check_events(ship):
    """reaction for all events initiated by the user"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
                # Moving ship right
                ship.rect.centerx += 1
            if event.key == pygame.K_LEFT:
                ship.moving_left = True
                # Moving ship left
                ship.rect.centerx -= 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False


def update_screen(ai_settings,screen,ship):
    ''' Aktualization of all images on the screen and moving to updated screen'''
    # Refreshing of the screen during each iteration'''
    ''' Pygame method background color following RGB convention'''
    screen.fill(ai_settings.bg_color)
    """ Display ship on the screen"""
    
    ship.blitme()
    ''' Pygame method responsible for refreshing the screen'''
    pygame.display.flip()
    
