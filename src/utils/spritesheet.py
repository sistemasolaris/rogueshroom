import pygame as pg

class SpriteSheet():
    """
    Handle all sprite sheet functionality

    Parameters
    ----------
    filename: str
        Path to the sprite sheet image

    Attributes
    ----------
    sheet: Surface
        The loaded sprite sheet image
    """

    def __init__(self, filename):

        # Load sprite sheet
        try:
            self.sheet = pg.image.load(filename).convert_alpha()
        except pg.error:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit