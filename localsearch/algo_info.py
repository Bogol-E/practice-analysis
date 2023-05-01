from util import *
from algo import BruteForce

ALGO_INFO = [
    {
        "name": "Brute Algo",
        "displacement": (0, FONT_HEIGHT),
        "name_coords": (0,0),
        "length_coords": (0, HEIGHT + FONT_HEIGHT),
        "depends": -1,
        "sim": BruteForce.BruteForceSolver,
    },
]

DIVIDERS = [
    (0, HEIGHT + FONT_HEIGHT, WINDOW_WIDTH, HEIGHT + FONT_HEIGHT),
    (WIDTH, 0, WIDTH, WINDOW_HEIGHT),
    (WIDTH, 0, WIDTH, WINDOW_HEIGHT),
    (WIDTH, 0, WIDTH, WINDOW_HEIGHT),
    (2 * WIDTH, 0, 2 * WIDTH, WINDOW_HEIGHT),
    (3 * WIDTH, 0, 3 * WIDTH, WINDOW_HEIGHT),
]
