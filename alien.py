import pygame 
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class representing single alien in the alien fleet"""
    def __init__(self,ai_settings,screen):
        """Initialization of the alien object and its inital position"""
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load("alienship.png")
        self.image = pygame.transform.scale(self.image,(80,80))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x=float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image,self.rect)
