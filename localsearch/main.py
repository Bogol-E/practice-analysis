import pygame
import gfx
import threading
from util import *
from algo_info import ALGO_INFO, DIVIDERS


def loop():
    for i in range(len(ALGO_INFO)):
        print(i)

    while True:
        gfx.check_events()
        gfx.draw_dividers(surface, DIVIDERS)

        for i in range(len(ALGO_INFO)):
            if i < len(sim):
                gfx.draw_text_top_left(
                    surface,
                    ALGO_INFO[i]["name"],
                    GREEN,
                    font,
                    *ALGO_INFO[i]["name_coords"]
                )
                gfx.draw_path(surface, list_of_cities_list[i], sim[i].best_order)
            elif len(sim[ALGO_INFO[i]["depends"]].best_order) != 0:
                pass

        pygame.display.update()
        surface.fill(BLACK)


pygame.init()
surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
font = pygame.font.SysFont("Ubuntu", FONT_HEIGHT)
cities = make_cities(5)
list_of_cities_list = []
sim = []
threads = []

for i in range(len(ALGO_INFO)):
    list_of_cities_list.append(displace(cities, *ALGO_INFO[i]["displacement"]))

for i in range(len(ALGO_INFO)):
    if ALGO_INFO[i]["depends"] == -1:
        sim.append(ALGO_INFO[i]["sim"](list_of_cities_list[i]))
        threads.append(threading.Thread(target=sim[i].find))
        threads[i].daemon = True

if __name__ == "__main__":
    pygame.display.set_caption("TSP - Visualizer")
    loop()
