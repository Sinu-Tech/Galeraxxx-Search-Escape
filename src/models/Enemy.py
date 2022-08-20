import numpy as np
from .abs_class.AbstractModel import AbstractCharacter
from .Cell import *

map_1 = np.array([[3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
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
                  [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])


class Enemy(AbstractCharacter):
    def __init__(self, name: str, pos_x: int, pos_y: int, speed: float):
        super().__init__(name, pos_x, pos_y, speed)
        self.map_h = []
        for x in range(0, 20):
            temp = []
            for y in range(0, 20):
                temp.append(Cell(x, y, False, None))
            self.map_h.append(temp)
        self.expansions = []

    def update_maph(self, pos_xp: int, pos_yp: int):
        for y in range(0, 20):
            for x in range(0, 20):
                self.map_h[y][x].h = abs(pos_xp - x) + abs(pos_yp - y)
                # print(y, x)
                # print(self.map_h[y, x].h, self.map_h[y, x].x, self.map_h[y, x].y)

    def print_maph(self):
        for i in range(0, 20):
            for j in range(0, 20):
                print(self.map_h[j, i].h)
        print(self.map_h.shape)

    # def get_bigger_expansion(expansions):
    #     biggest_expansion = 0
    #     for expansion in expansions:

    #         if expansion > biggest_expansion:
    #             biggest_expansion = expansion
    #     return biggest_expansion

    def get_expansions(self, pos_xp: int, pos_yp: int):
        self.expansions.append(Cell(self.pos_x, self.pos_y, True, None))
        pos_x_aux, pos_y_aux = self.expansions[0].x, self.expansions[0].y

        while len(self.expansions) > 0 and self.expansions[0].x != pos_xp and self.expansions[0].y != pos_yp:
            print("Tamanho da fila no começo: ", len(self.expansions))

            if pos_x_aux < 19 and map_1[pos_x_aux + 1][pos_y_aux] == MAP_FREE:
                map_1[pos_x_aux + 1][pos_y_aux] = -1
                print("Entrou na: x+1")
                self.expansions.append(
                    Cell(pos_x_aux + 1, pos_y_aux, True, self.expansions[0]))
                for x in self.expansions:
                    print("Expandiu para", " - ", x.x, x.y, x.was_visited)

            if pos_x_aux > 0 and map_1[pos_x_aux - 1][pos_y_aux] == MAP_FREE:
                map_1[pos_x_aux - 1][pos_y_aux] = -1
                print("Entrou na: x-1")
                self.expansions.append(
                    Cell(pos_x_aux - 1, pos_y_aux, True, self.expansions[0]))
                for x in self.expansions:
                    print("Expandiu para", " - ", x.x, x.y, x.was_visited)

            if pos_y_aux < 19 and map_1[pos_x_aux][pos_y_aux + 1] == MAP_FREE:
                map_1[pos_x_aux][pos_y_aux + 1] = -1
                print("Entrou na: y+1")
                self.expansions.append(
                    Cell(pos_x_aux, pos_y_aux + 1, True, self.expansions[0]))
                for x in self.expansions:
                    print("Expandiu para", " - ", x.x, x.y, x.was_visited)

            if pos_y_aux > 0 and map_1[pos_x_aux][pos_y_aux - 1] == MAP_FREE:
                map_1[pos_x_aux][pos_y_aux - 1] = -1
                print("Entrou na: y-1")
                self.expansions.append(
                    Cell(pos_x_aux, pos_y_aux - 1, True, self.expansions[0]))
                for x in self.expansions:
                    print("Expandiu para", " - ", x.x, x.y, x.was_visited)

            print("Tamanho da fila no final: ", len(self.expansions))
            print(map_1)
            self.expansions.pop(0)
            print()
            pos_x_aux, pos_y_aux = self.expansions[0].x, self.expansions[0].y
