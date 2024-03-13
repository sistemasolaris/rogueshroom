import pygame as pg
import config as conf
from src.characters.player import Player

def main():
    pg.init()
    screen = pg.display.set_mode((conf.WIDTH, conf.HEIGHT))
    clock = pg.time.Clock()
    running = True

    # Sprite groups
    all_sprites = pg.sprite.Group()

    # Sprites
    player = Player((640, 360), all_sprites)

    while running:
        # Poll for events
        for event in pg.event.get():
            if event == pg.QUIT:
                running = False
        
        screen.fill("purple")
        all_sprites.draw(screen)
        all_sprites.update()
        pg.display.flip()
        clock.tick(conf.FPS)

if __name__ == "__main__":
    main()