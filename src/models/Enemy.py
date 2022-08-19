from .abstracts.AbstractCharcater import AbstractCharacter


class Enemy(AbstractCharacter):
    def __init__(self, name:str, pos_x:int, pos_y:int, speed:float):
        super().__init__(name, pos_x, pos_y, speed)

