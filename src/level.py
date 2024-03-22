import pygame as pg
from config import *

class Level():
    def __init__(self):
        self.display_surface = pg.display.get_surface()

    def run(self, dt):
        self.display_surface.fill("purple")