import pygame

class Ship():
    """ Creating Class for a Ship object """
    def __init__(self,ai_settings,screen):
        # attributes of the ship object
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load("spaceship.png")
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.centerx = float(self.screen_rect.centerx)
        self.centery = float(self.screen_rect.bottom)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        # special method responsible for display object on the screen
        self.screen.blit(self.image,self.rect)

    def update(self):
        # special method controlling ship movement
        if self.moving_right and self.rect.right < self.screen_rect.right :
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor
        self.rect.centerx = self.centerx
        self.rect.bottom  = self.centery



        
