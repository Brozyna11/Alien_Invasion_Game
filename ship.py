import pygame
# Creating Class for a Ship object
class Ship():
    # Initiating constructor
    def __init__(self,ai_settings,screen):
        """Initialization of the spaceship and position"""
        self.screen = screen
        # Seetings related to speed of the ship
        self.ai_settings = ai_settings
        # Loading of the spaceship and its rectangle
        self.image = pygame.image.load("spaceship.png")
        #  Scaling of the image
        self.image = pygame.transform.scale(self.image,(100,100))
        # Creating Rectangle
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Option indicating moving the ship
        self.moving_right = False
        self.moving_left = False

        # Setting initial position of the ship
        self.center = float(self.screen_rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
    def update(self):
        """
        Aktualization of the position of the ship
        """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center

    def blitme(self):
        """ Display ship in current position"""
        self.screen.blit(self.image,self.rect)
    

        
