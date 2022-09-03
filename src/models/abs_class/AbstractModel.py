from abc import ABCMeta, abstractmethod


class AbstractCharacter(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, name: str, pos_x: int, pos_y: int):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def move(self, direction):
        if direction == 'up':
            self.pos_y -= 1

        elif direction == 'down':
            self.pos_y += 1

        elif direction == 'left':
            self.pos_x -= 1

        elif direction == 'right':
            self.pos_x += 1

