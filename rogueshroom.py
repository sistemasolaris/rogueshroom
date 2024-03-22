import sys
import pygame as pg
from config import *
from src.level import Level

class Game:
    def __init__(self):
        pg.init()

        # Create display screen
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("ROGUESHROOM")

        # Create game clock
        self.clock = pg.time.Clock()

        # The level the game is going to run
        self.level = Level()

    def run(self):
        while True:
            for event in pg.event.get():

                # Quit the game
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            
            # Deltatime, used for framerate independence
            dt = self.clock.tick() / 1000

            self.level.run(dt)
            pg.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()