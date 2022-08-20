from .abstracts.AbstractCharcater import AbstractCharacter
import numpy as np

class Enemy(AbstractCharacter):
    def __init__(self, name:str, pos_x:int, pos_y:int, speed:float):
        super().__init__(name, pos_x, pos_y, speed)
        self.map_h = np.array([[0]*20]*20)

    def  update_maph(self, pos_xp:int, pos_yp:int):
        for y in range(0, 20):
            for x in range(0, 20):
                self.map_h[y, x] = abs(pos_xp-x) + abs(pos_yp-y)

    def print_maph(self):
        print(self.map_h)

