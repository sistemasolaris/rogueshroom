import pygame as pg
from config import *
from src.characters.player import Player

class Level():
    def __init__(self):

        # Game screen
        self.display_surface = pg.display.get_surface()

        # Sprite groups
        self.all_sprites = pg.sprite.Group()

        # Setup level
        self.setup()

    def setup(self):
        self.player = Player((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), self.all_sprites)

    def run(self, dt):

        # Draw on screen and update sprites
        self.display_surface.fill("purple")
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)