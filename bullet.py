import pygame
from pygame.sprite import Sprite
import game_functions

class Bullet_Straight(Sprite):
    """Class designed for bullets management"""
    # Class Sprite is a simple parent class for visible game objects
    # Bullet class inherit from superclass Sprite

    def __init__(self,ai_settings,screen,space_ship):
        """ Creating of the bullet object in the initial position"""
        # The super() builtin returns a object (temporary object of the superclass) that allows us to access methods of the base class.
        super(Bullet_Straight,self).__init__()
        self.screen = screen

        # Creation of the rectangle in the point (0,0) and defining the correct position by using special pygame.Rect method
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = space_ship.rect.centerx
        self.rect.top = space_ship.rect.top

        # Position of the bullet determined as float number

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    
    def update(self):
        """ Method related to moving the bullet on the screen"""
        # Aktualization of the bullet Y position
        self.y -= self.speed_factor
        # Aktualization of the bullet Y coordinate
        self.rect.y = self.y


    def draw_bullet(self):
        """Display Bullet"""
        pygame.draw.rect(self.screen,self.color,self.rect)



class Bullet_Left(Sprite):
    """Class designed for bullets management"""
    # Class Sprite is a simple parent class for visible game objects
    # Bullet class inherit from superclass Sprite

    def __init__(self,ai_settings,screen,space_ship):
        """ Creating of the bullet object in the initial position"""
        # The super() builtin returns a object (temporary object of the superclass) that allows us to access methods of the base class.
        super(Bullet_Left,self).__init__()
        self.screen = screen

        # Creation of the rectangle in the point (0,0) and defining the correct position by using special pygame.Rect method
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = space_ship.rect.centerx
        self.rect.center = space_ship.rect.center

        # Position of the bullet determined as float number

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    
    def update(self):
        """ Method related to moving the bullet on the screen"""
        # Aktualization of the bullet Y position
        self.y -= self.speed_factor
        self.x -= self.speed_factor
        # Aktualization of the bullet Y coordinate
        self.rect.y = self.y
        self.rect.x = self.x


    def draw_bullet(self):
        """Display Bullet"""
        pygame.draw.rect(self.screen,self.color,self.rect)



class Bullet_Right(Sprite):
    """Class designed for bullets management"""
    # Class Sprite is a simple parent class for visible game objects
    # Bullet class inherit from superclass Sprite

    def __init__(self,ai_settings,screen,space_ship):
        """ Creating of the bullet object in the initial position"""
        # The super() builtin returns a object (temporary object of the superclass) that allows us to access methods of the base class.
        super(Bullet_Right,self).__init__()
        self.screen = screen

        # Creation of the rectangle in the point (0,0) and defining the correct position by using special pygame.Rect method
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = space_ship.rect.centerx
        self.rect.center = space_ship.rect.center

        # Position of the bullet determined as float number

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    
    def update(self):
        """ Method related to moving the bullet on the screen"""
        # Aktualization of the bullet Y position
        self.y -= self.speed_factor
        self.x += self.speed_factor
        # Aktualization of the bullet Y coordinate
        self.rect.y = self.y
        self.rect.x = self.x


    def draw_bullet(self):
        """Display Bullet"""
        pygame.draw.rect(self.screen,self.color,self.rect)






