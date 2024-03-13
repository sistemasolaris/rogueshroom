import os
import pygame as pg
import config as conf

class Player(pg.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pg.image.load(os.path.join(conf.GRAPHICS_DIR, "characters", "player-character-prototype.png")).convert_alpha()
        self.rect = self.image.get_rect(center = pos)