import pygame as pg

pg.init()
screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()
running = True

while running:
    # Poll for events
    for event in pg.event.get():
        if event == pg.QUIT:
            running = False
    
    screen.fill("purple")
    pg.display.flip()
    clock.tick(60) 