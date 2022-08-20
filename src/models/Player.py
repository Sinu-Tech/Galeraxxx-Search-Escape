from .abs_class.AbstractModel import AbstractCharacter


class Player(AbstractCharacter):
    def __init__(self, name: str, pos_x: int, pos_y: int, speed: float):
        super().__init__(name, pos_x, pos_y, speed)
        self.is_alive = True

    def died(self):
        self.is_alive = False
