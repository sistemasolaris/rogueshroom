import os
import pygame as pg
from config import *

class Player(pg.sprite.Sprite):
    def __init__(self, pos, group):

        super().__init__(group)

        # Sprite attributes
        self.image = pg.transform.scale(
                pg.image.load(os.path.join(GRAPHICS_DIR, "characters", "player-character-prototype.png")).convert_alpha(),
                (32, 64)
            )
        self.rect = self.image.get_rect(center = pos)

        # Movement attributes
        self.direction = pg.math.Vector2()
        self.pos = pg.math.Vector2(self.rect.center)

        # Stat attributes
        self.health = 3
        self.speed = 200

    def update(self, dt):

        self.input()
        self.move(dt)
    
    def move(self, dt):

        # Normalize direction vector
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        # Calculate new position
        self.pos += self.direction * self.speed * dt
        self.rect.center = self.pos

    def input(self):

        # Get keys currently being pressed
        keys = pg.key.get_pressed()

        # Translate movement key presses to movement directions
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
    
    def take_damage(self):
        self.health -= 1