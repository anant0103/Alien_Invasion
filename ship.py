import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self,ai_settings,screen):
        #inherits ship from sprites
        super(Ship,self).__init__()

        self.screen=screen
        self.ai_settings=ai_settings

        #load ship image
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.screen_rect=screen.get_rect()

        #image at bottom
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        #decimal value for ships center
        self.center=float(self.rect.centerx)

        #movement flag
        self.moving_right=False
        self.moving_left=False

    def update(self):
        #update ship position
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.center -= self.ai_settings.ship_speed_factor

        #update rect from self.center
        self.rect.centerx=self.center

    def blitme(self):
        """Draw ship"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.center=self.screen_rect.centerx