from cmath import exp
import numpy as np
from .abs_class.AbstractModel import AbstractCharacter
from .Cell import *
from .enums.EnumMap import *

map_1 = np.array([[3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
                  [0, 1, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
                  [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
                  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])


def better_index(expansions: list):
    better_index = 0
    better_f = expansions[0].f
    for index, e in enumerate(expansions):
        if e.f < better_f:
            better_f = e.f
            better_index = index
    return better_index


class Enemy(AbstractCharacter):
    def __init__(self, name: str, pos_x: int, pos_y: int, speed: float):
        super().__init__(name, pos_x, pos_y, speed)
        self.map_h = []
        for x in range(0, 20):
            temp = []
            for y in range(0, 20):
                temp.append(Cell(x, y, 0, 0, 0, False, None))
            self.map_h.append(temp)
        self.expansions = []

    def update_map_fh(self, pos_xp: int, pos_yp: int):
        for y in range(0, 20):
            for x in range(0, 20):
                self.map_h[y][x].h = abs(pos_xp - x) + abs(pos_yp - y)

    def print_maph(self):
        print("f")
        for i in range(0, 20):
            for j in range(0, 20):
                print(self.map_h[i][j].f, end=" ")
            print("")
        print("g")
        for i in range(0, 20):
            for j in range(0, 20):
                print(self.map_h[i][j].g, end=" ")
            print("")
        print("h")
        for i in range(0, 20):
            for j in range(0, 20):
                print(self.map_h[i][j].h, end=" ")
            print("")

    def print_expansions(self):
        for e in self.expansions:
            print(e.x, e.y, e.f, e.g, e.h)

    def get_expansions(self, pos_xp: int, pos_yp: int):
        self.expansions.append(self.map_h[self.pos_x][self.pos_y])
        x_aux, y_aux = self.expansions[0].x, self.expansions[0].y
        index = better_index(self.expansions)

        while len(self.expansions) > 0 and (self.expansions[index].x != pos_xp or self.expansions[index].y != pos_yp):

            # down
            if x_aux < 19 and map_1[x_aux + 1][y_aux] == MAP_FREE and self.map_h[x_aux + 1][y_aux].was_visited == False:
                map_1[x_aux + 1][y_aux] = -1
                g = self.map_h[x_aux][y_aux].g + 1
                h = self.map_h[x_aux][y_aux].h
                f = g + h
                self.map_h[x_aux+1][y_aux].g = g
                self.map_h[x_aux+1][y_aux].f = f
                self.expansions.append(
                    Cell(x_aux + 1, y_aux, f, g, h, True, self.expansions[index]))
            # up
            if x_aux > 0 and map_1[x_aux - 1][y_aux] == MAP_FREE and self.map_h[x_aux - 1][y_aux].was_visited == False:
                map_1[x_aux - 1][y_aux] = -1
                g = self.map_h[x_aux][y_aux].g + 1
                self.map_h[x_aux-1][y_aux].g = g
                h = self.map_h[x_aux-1][y_aux].h
                f = g + h
                self.map_h[x_aux-1][y_aux].f = f
                self.expansions.append(
                    Cell(x_aux - 1, y_aux, f, g, h, True, self.expansions[index]))
            # right
            if y_aux < 19 and map_1[x_aux][y_aux + 1] == MAP_FREE and self.map_h[x_aux ][y_aux+1].was_visited == False:
                map_1[x_aux][y_aux + 1] = -1
                g = self.map_h[x_aux][y_aux].g + 1
                self.map_h[x_aux][y_aux+1].g = g
                h = self.map_h[x_aux][y_aux+1].h
                f = g + h
                self.map_h[x_aux][y_aux + 1].f = f
                self.expansions.append(
                    Cell(x_aux, y_aux + 1, f, g, h, True, self.expansions[index]))
            # lef
            if y_aux > 0 and map_1[x_aux][y_aux - 1] == MAP_FREE and self.map_h[x_aux][y_aux-1].was_visited == False:
                map_1[x_aux][y_aux - 1] = -1
                g = self.map_h[x_aux][y_aux].g + 1
                self.map_h[x_aux][y_aux+1].g = g
                h = self.map_h[x_aux][y_aux-1].h
                f = g + h
                self.map_h[x_aux][y_aux - 1].f = f
                self.expansions.append(
                    Cell(x_aux, y_aux + 1, f, g, h, True, self.expansions[index]))

            self.expansions.pop(index)
            if len(self.expansions) > 0:
                index = better_index(self.expansions)
                x_aux, y_aux = self.expansions[index].x, self.expansions[index].y
                if self.expansions[index].x == pos_xp and self.expansions[index].y == pos_yp:
                    return self.expansions[index]

