import numpy as np
from .abs_class.AbstractModel import AbstractCharacter
from .Cell import *
from .enums.EnumMap import *

map_1 = np.array([[3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
                  [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
                  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

map_2 = np.array([[3, 0, 0, 0, 0],
                  [0, 1, 0, 1, 0],
                  [0, 0, 0, 1, 1],
                  [0, 1, 0, 1, 0],
                  [1, 1, 0, 0, 0]])
print(map_2)


def better_index(expansions: list):
    better_index = 0
    better_f = expansions[0].f
    for index, e in enumerate(expansions):
        if e.f <= better_f:
            better_f = e.f
            better_index = index
    return better_index


def get_euclidean_distance(x_aux: int, y_aux: int, pos_xp: int, pos_yp: int):
    # return ((pos_xp - x_aux) ** 2 + (pos_yp - y_aux) ** 2) ** (1 / 2)
    return abs(pos_xp - x_aux) + abs(pos_yp - y_aux)


class Enemy(AbstractCharacter):
    def __init__(self, name: str, pos_x: int, pos_y: int, speed: float):
        super().__init__(name, pos_x, pos_y, speed)
        self.map_h = []
        for y in range(0, 5):
            temp = []
            for x in range(0, 5):
                temp.append(Cell(x, y, 0, 0, 0, False, None))
            self.map_h.append(temp)
        self.map_h = np.array(self.map_h)
        print(self.map_h)
        self.expansions = []

    
    def print_visiteds(self):
        for x in self.map_h:
            for y in x:
                if y.was_visited:
                    print(1, end=" ")
                else:
                    print(0, end=" ")
            print("")

    def print_map_h(self):
        print("Mapa heurístico")
        for i in range(0, 5):
            for j in range(0, 5):
                print("{:.0f}".format(self.map_h[i][j].h), end=" ")
            print("")

    def print_map_g(self):
        print("Mapa da função g")
        for i in range(0, 5):
            for j in range(0, 5):
                print(self.map_h[i][j].g, end=" ")
            print("")

    def print_map_f(self):
        print("Mapa da função F")
        for i in range(0, 5):
            for j in range(0, 5):
                print("{:.0f}".format(self.map_h[i, j].f), end=" ")
            print("")

    def get_expansions(self, pos_xp: int, pos_yp: int):
        self.expansions.append(self.map_h[self.pos_x][self.pos_y])
        x_aux, y_aux = self.expansions[0].x, self.expansions[0].y
        index = better_index(self.expansions)

        while len(self.expansions) > 0:
            if self.expansions[index].x == pos_xp and self.expansions[index].y == pos_yp:
                return self.expansions[index]
            # down
            if x_aux < 4 and map_2[x_aux + 1][y_aux] == MAP_FREE and self.map_h[x_aux + 1][y_aux].was_visited == False:
                print("down")
                map_2[x_aux + 1][y_aux] = -1
                g = self.map_h[x_aux][y_aux].g + 1
                h = get_euclidean_distance(x_aux + 1, y_aux, pos_xp, pos_yp)
                f = g + h
                self.map_h[x_aux + 1][y_aux].g = g
                self.map_h[x_aux + 1][y_aux].h = h
                self.map_h[x_aux + 1][y_aux].f = f
                self.map_h[x_aux + 1][y_aux].was_visited = True
                self.print_visiteds()
                self.expansions.append(
                    Cell(x_aux + 1, y_aux, f, g, h, True, self.expansions[index]))
            # up
            if x_aux > 0 and map_2[x_aux - 1][y_aux] == MAP_FREE and self.map_h[x_aux - 1][y_aux].was_visited == False:
                print("up")
                map_2[x_aux - 1][y_aux] = -1
                g = self.map_h[x_aux][y_aux].g + 1
                h = get_euclidean_distance(x_aux - 1, y_aux, pos_xp, pos_yp)
                f = g + h
                self.map_h[x_aux - 1][y_aux].h = h
                self.map_h[x_aux - 1][y_aux].g = g
                self.map_h[x_aux - 1][y_aux].f = f
                self.map_h[x_aux - 1][y_aux].was_visited = True
                self.print_visiteds()
                self.expansions.append(
                    Cell(x_aux - 1, y_aux, f, g, h, True, self.expansions[index]))
            # right
            if y_aux < 4 and map_2[x_aux][y_aux + 1] == MAP_FREE and self.map_h[x_aux][y_aux + 1].was_visited == False:
                print("right")
                map_2[x_aux][y_aux + 1] = -1
                g = self.map_h[x_aux][y_aux].g + 1
                h = get_euclidean_distance(x_aux, y_aux + 1, pos_xp, pos_yp)
                f = g + h
                self.map_h[x_aux][y_aux + 1].h = h
                self.map_h[x_aux][y_aux + 1].g = g
                self.map_h[x_aux][y_aux + 1].f = f
                self.map_h[x_aux][y_aux + 1].was_visited = True
                self.print_visiteds()
                self.expansions.append(
                    Cell(x_aux, y_aux + 1, f, g, h, True, self.expansions[index]))
            # left
            if y_aux > 0 and map_2[x_aux][y_aux - 1] == MAP_FREE and self.map_h[x_aux][y_aux - 1].was_visited == False:
                print("left")
                map_2[x_aux][y_aux - 1] = -1
                g = self.map_h[x_aux][y_aux].g + 1
                h = get_euclidean_distance(x_aux, y_aux - 1, pos_xp, pos_yp)
                f = g + h
                self.map_h[x_aux][y_aux - 1].h = h
                self.map_h[x_aux][y_aux - 1].g = g
                self.map_h[x_aux][y_aux - 1].f = f
                self.map_h[x_aux][y_aux - 1].was_visited = True
                self.print_visiteds()
                self.expansions.append(
                    Cell(x_aux, y_aux + 1, f, g, h, True, self.expansions[index]))

            self.expansions.pop(index)
            if len(self.expansions) > 0:
                index = better_index(self.expansions)
                x_aux, y_aux = self.expansions[index].x, self.expansions[index].y
