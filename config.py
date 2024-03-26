import os

# Directories
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
GRAPHICS_DIR = os.path.join(ROOT_DIR, "resources", "graphics")

# Proportions
BASE_WIDTH, BASE_HEIGHT = 320, 180
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
SCALE_FACTOR = SCREEN_WIDTH // BASE_WIDTH
TILE = 16

# Colors

BLACK = (0, 0, 0)