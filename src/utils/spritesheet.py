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
    sheet: pygame.Surface
        The loaded sprite sheet image
    """

    def __init__(self, filename: str):

        # Load sprite sheet
        try:
            self.sheet = pg.image.load(filename).convert()
        except pg.error:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit
        
    def get_image_at(self, rectangle: pg.Rect, colorkey: pg.Color = None):
        """
        Get one sprite from sprite sheet

        Parameters
        ----------
        rectangle: pygame.Rect
            The location of the sprite to be returned, in the format of (x, y, width, height)
        colorkey: pygame.Color, optional
            The color, in (R, G, B), to be made transparent in the sprite, defaults to None

        Returns
        -------
        Surface
            The requested sprite
        """

        rect = pg.Rect(rectangle)
        image = pg.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            image.set_colorkey(colorkey, pg.RLEACCEL)
        
        return image