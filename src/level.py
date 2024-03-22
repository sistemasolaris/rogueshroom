import pygame as pg
from config import *

class Level():
    def __init__(self):

        # Game screen
        self.display_surface = pg.display.get_surface()

        # Sprite groups
        self.all_sprites = pg.sprite.Group()

    def run(self, dt):
        
        # Draw on screen and update sprites
        self.display_surface.fill("purple")
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update()