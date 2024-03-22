import os
import pygame as pg
from config import *

class Player(pg.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        # Sprite
        self.image = pg.image.load(os.path.join(GRAPHICS_DIR, "characters", "player-character-prototype.png")).convert_alpha()
        self.rect = self.image.get_rect(center = pos)

        # Movement
        self.direction = pg.math.Vector2()

    def update(self, dt):
        self.input()

    def input(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_UP] or keys[pg.K_w]:
            self.direction.y = -1
        elif keys[pg.K_DOWN] or keys[pg.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.direction.x = -1
        elif keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0

        print(self.direction)