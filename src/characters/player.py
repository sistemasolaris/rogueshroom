import os
import pygame as pg
from src.utils.spritesheet import SpriteSheet
from config import *

class Player(pg.sprite.Sprite):
    def __init__(self, pos, group):

        super().__init__(group)

        # Sprite attributes
        self.animations = self.import_assets()
        self.status = "down-idle"
        self.frame = 0
        self.image = pg.transform.scale(
                self.animations[self.status][self.frame],
                (16 * SCALE_FACTOR, 24 * SCALE_FACTOR)
            )
        self.rect = self.image.get_rect(center = pos)

        # Movement attributes
        self.direction = pg.math.Vector2()
        self.pos = pg.math.Vector2(self.rect.center)

        # Stat attributes
        self.health = 3
        self.speed = 200

    def import_assets(self):
        animations = {
            "up-idle": None, "left-idle": None, "right-idle": None, "down-idle": None,
            "up-walk": None, "left-walk": None, "right-walk": None, "down-walk": None
            }

        for animation in animations.keys():
            path = os.path.join(GRAPHICS_DIR, "characters", "shroomy", animation, f"{animation}.png")
            sprite_sheet = SpriteSheet(path)
            animations[animation] = sprite_sheet.get_strip((0, 0, 16, 24), sprite_sheet.sheet.get_width() // 16, BLACK)

        return animations
    
    def animate(self, dt):
        self.frame += 5 * dt

        if self.frame > len(self.animations[self.status]):
            self.frame = 0
        
        self.image = pg.transform.scale(
                self.animations[self.status][int(self.frame)],
                (16 * SCALE_FACTOR, 24 * SCALE_FACTOR)
            )

    def update(self, dt):

        self.input()
        self.move(dt)
        self.animate(dt)
    
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
            self.status = "up-walk"
        elif keys[pg.K_DOWN] or keys[pg.K_s]:
            self.direction.y = 1
            self.status = "down-walk"
        else:
            self.direction.y = 0

        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.direction.x = -1
            self.status = "left-walk"
        elif keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.direction.x = 1
            self.status = "right-walk"
        else:
            self.direction.x = 0
    
    def take_damage(self):
        self.health -= 1