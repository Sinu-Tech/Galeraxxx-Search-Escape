import numpy as np


def get_position(_map: np.array, _MAP_ENUM: int) -> tuple:
    for y in range(0, len(_map)):
        for x in range(0, len(_map)):
            if _map[y][x] == _MAP_ENUM:
                return y, x


def less_f_index(expansions: list):
    better_index = 0
    better_f = expansions[0].f
    for index, e in enumerate(expansions):
        if e.f <= better_f:
            better_f = e.f
            better_index = index
    return better_index


def get_distance(x_aux: int, y_aux: int, pos_xp: int, pos_yp: int):
    # return ((pos_xp - x_aux) ** 2 + (pos_yp - y_aux) ** 2) ** (1 / 2) # Distancia euclidiana (não usar se não saber para que serve)
    return abs(pos_xp - x_aux) + abs(pos_yp - y_aux)


def print_visiteds(_map: np.array):
    for y in _map:
        for x in y:
            if x.was_visited:
                print(1, end=" ")
            else:
                print(0, end=" ")
        print("")


def print_map_h(_map: np.array):
    print("Mapa heurístico")
    for y in _map:
        for x in y:
            print(x.h, end=" ")
        print("")


def print_map_g(_map: np.array):
    print("Mapa função g")
    for y in _map:
        for x in y:
            print(x.g, end=" ")
        print("")


def print_map_f(_map: np.array):
    print("Mapa função f")
    for y in _map:
        for x in y:
            print(x.f, end=" ")
        print("")

