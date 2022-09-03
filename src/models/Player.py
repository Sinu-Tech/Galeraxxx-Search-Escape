from .abs_class.AbstractModel import AbstractCharacter


class Player(AbstractCharacter):
    def __init__(self, name: str, pos_x: int, pos_y: int):
        super().__init__(name, pos_x, pos_y)
        self.is_alive = True

    def died(self):
        self.is_alive = False
