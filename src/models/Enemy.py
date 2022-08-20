from .abstracts.AbstractCharcater import AbstractCharacter
import numpy as np
from models.enums.EnumMap import MAP_FREE
from models.Cell import Cell

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
        self.map_h = np.array([[0]*20]*20)
        self.expansions = []

    def update_maph(self, pos_xp: int, pos_yp: int):
        for y in range(0, 20):
            for x in range(0, 20):
                self.map_h[y, x] = abs(pos_xp-x) + abs(pos_yp-y)

    def print_maph(self):
        print(self.map_h)

    def get_expansions(self, pos_xp: int, pos_yp: int):
        self.expansions.append(Cell(self.pos_x, self.pos_y, True, None))
        pos_x_aux, pos_y_aux = self.expansions[0].x, self.expansions[0].y

        while len(self.expansions) > 0:
            print("Tamanho da fila no começo: ", len(self.expansions))
            if pos_x_aux == pos_xp and pos_y_aux == pos_yp:
                return "Encontrado"

            if pos_x_aux < 19 and map_1[pos_x_aux + 1][pos_y_aux] == MAP_FREE:
                map_1[pos_x_aux + 1][pos_y_aux] = -1
                print("Entrou na: x+1")
                self.expansions.append(
                    Cell(pos_x_aux + 1, pos_y_aux, True, self.expansions[0]))
                for x in self.expansions:
                    print("Expandiu para", " - ",x.x, x.y, x.was_visited)

            if pos_x_aux > 0 and map_1[pos_x_aux - 1][pos_y_aux] == MAP_FREE:
                map_1[pos_x_aux - 1][pos_y_aux] = -1
                print("Entrou na: x-1")
                self.expansions.append(
                    Cell(pos_x_aux - 1, pos_y_aux, True, self.expansions[0]))
                for x in self.expansions:
                    print("Expandiu para", " - ",x.x, x.y, x.was_visited)

            if pos_y_aux < 19 and map_1[pos_x_aux][pos_y_aux + 1] == MAP_FREE:
                map_1[pos_x_aux][pos_y_aux + 1] = -1
                print("Entrou na: y+1")
                self.expansions.append(
                    Cell(pos_x_aux, pos_y_aux + 1, True, self.expansions[0]))
                for x in self.expansions:
                    print("Expandiu para", " - ",x.x, x.y, x.was_visited)

            if pos_y_aux > 0 and map_1[pos_x_aux][pos_y_aux - 1] == MAP_FREE:
                map_1[pos_x_aux][pos_y_aux-1] = -1
                print("Entrou na: y-1")
                self.expansions.append(
                    Cell(pos_x_aux, pos_y_aux - 1, True, self.expansions[0]))
                for x in self.expansions:
                    print("Expandiu para", " - ",x.x, x.y, x.was_visited)

            print("Tamanho da fila no final: ", len(self.expansions))
            self.expansions.pop(0)
            print()
            pos_x_aux, pos_y_aux = self.expansions[0].x, self.expansions[0].y
