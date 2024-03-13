import pygame as pg
import config as conf

def main():
    pg.init()
    screen = pg.display.set_mode((conf.WIDTH, conf.HEIGHT))
    clock = pg.time.Clock()
    running = True

    while running:
        # Poll for events
        for event in pg.event.get():
            if event == pg.QUIT:
                running = False
        
        screen.fill("purple")
        pg.display.flip()
        clock.tick(conf.FPS)

if __name__ == "__main__":
    main()