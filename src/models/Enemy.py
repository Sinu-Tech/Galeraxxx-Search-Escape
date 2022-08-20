import numpy as np
from .abs_class.AbstractModel import AbstractCharacter
from .Cell import *
from .enums.EnumMap import *
from .Map import *
from utils import *


class Enemy(AbstractCharacter):
    def __init__(self, name: str, pos_x: int, pos_y: int, speed: float):
        super().__init__(name, pos_x, pos_y, speed)
        self.map_bot = []
        for y in range(0, len(game_map)):
            temp = []
            for x in range(0, len(game_map[0])):
                temp.append(Cell(x, y, 0, 0, 0, False, None))
            self.map_bot.append(temp)
        self.map_bot = np.array(self.map_bot)
        print(self.map_bot)
        self.expansions = []

    def get_expansions(self, pos_xp: int, pos_yp: int):
        self.expansions.append(self.map_bot[self.pos_x][self.pos_y])
        x_aux, y_aux = self.expansions[0].x, self.expansions[0].y
        index = better_index(self.expansions)

        while len(self.expansions) > 0:
            if self.expansions[index].x == pos_xp and self.expansions[index].y == pos_yp:
                return self.expansions[index]

            print(map_1)
            print()

            if x_aux < 19 and map_1[x_aux + 1][y_aux] == MAP_FREE and self.map_bot[x_aux + 1][y_aux].was_visited == False:
                map_1[x_aux + 1][y_aux] = -1
                g = self.map_bot[x_aux][y_aux].g + 1
                h = get_distance(x_aux + 1, y_aux, pos_xp, pos_yp)
                f = g + h
                self.map_bot[x_aux + 1][y_aux].g = g
                self.map_bot[x_aux + 1][y_aux].h = h
                self.map_bot[x_aux + 1][y_aux].f = f
                self.map_bot[x_aux + 1][y_aux].was_visited = True
                self.expansions.append(
                    Cell(x_aux + 1, y_aux, f, g, h, True, self.expansions[index]))

            if x_aux > 0 and map_1[x_aux - 1][y_aux] == MAP_FREE and self.map_bot[x_aux - 1][y_aux].was_visited == False:
                map_1[x_aux - 1][y_aux] = -1
                g = self.map_bot[x_aux][y_aux].g + 1
                h = get_distance(x_aux - 1, y_aux, pos_xp, pos_yp)
                f = g + h
                self.map_bot[x_aux - 1][y_aux].h = h
                self.map_bot[x_aux - 1][y_aux].g = g
                self.map_bot[x_aux - 1][y_aux].f = f
                self.map_bot[x_aux - 1][y_aux].was_visited = True
                self.expansions.append(
                    Cell(x_aux - 1, y_aux, f, g, h, True, self.expansions[index]))

            if y_aux < 19 and map_1[x_aux][y_aux + 1] == MAP_FREE and self.map_bot[x_aux][y_aux + 1].was_visited == False:
                map_1[x_aux][y_aux + 1] = -1
                g = self.map_bot[x_aux][y_aux].g + 1
                h = get_distance(x_aux, y_aux + 1, pos_xp, pos_yp)
                f = g + h
                self.map_bot[x_aux][y_aux + 1].h = h
                self.map_bot[x_aux][y_aux + 1].g = g
                self.map_bot[x_aux][y_aux + 1].f = f
                self.map_bot[x_aux][y_aux + 1].was_visited = True
                self.expansions.append(
                    Cell(x_aux, y_aux + 1, f, g, h, True, self.expansions[index]))

            if y_aux > 0 and map_1[x_aux][y_aux - 1] == MAP_FREE and self.map_bot[x_aux][y_aux - 1].was_visited == False:
                map_1[x_aux][y_aux - 1] = -1
                g = self.map_bot[x_aux][y_aux].g + 1
                h = get_distance(x_aux, y_aux - 1, pos_xp, pos_yp)
                f = g + h
                self.map_bot[x_aux][y_aux - 1].h = h
                self.map_bot[x_aux][y_aux - 1].g = g
                self.map_bot[x_aux][y_aux - 1].f = f
                self.map_bot[x_aux][y_aux - 1].was_visited = True
                self.expansions.append(
                    Cell(x_aux, y_aux + 1, f, g, h, True, self.expansions[index]))

            self.expansions.pop(index)
            if len(self.expansions) > 0:
                index = better_index(self.expansions)
                x_aux, y_aux = self.expansions[index].x, self.expansions[index].y
