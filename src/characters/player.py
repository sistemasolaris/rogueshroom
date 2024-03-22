import os
import pygame as pg
from config import *

class Player(pg.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pg.image.load(os.path.join(GRAPHICS_DIR, "characters", "player-character-prototype.png")).convert_alpha()
        self.rect = self.image.get_rect(center = pos)

    def update(self, dt):
        self.input()

    def input(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_UP] or keys[pg.K_w]:
            print("up")
        elif keys[pg.K_DOWN] or keys[pg.K_s]:
            print("down")

        if keys[pg.K_LEFT] or keys[pg.K_a]:
            print("left")
        elif keys[pg.K_RIGHT] or keys[pg.K_d]:
            print("right")