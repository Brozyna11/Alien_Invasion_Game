class Settings():
    """ Class contaning all general settings of all objects from which different objects """
    def __init__(self):
        # Screen Settings
        self.width = 1700
        self.height = 900
        self.bg_color = (0,0,0)
        # Ship settings
        self.ship_speed_factor = 5

        # Bullet settings
        self.bullet_speed_factor = 2
        self.bullet_width = 10
        self.bullet_height = 10
        self.bullet_color =255,60,60
        self.bullets_allowed = 6
