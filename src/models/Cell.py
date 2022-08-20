class Cell():
    def __init__(self, x: int, y: int, f: int, g: int, h: int, was_visited: bool, expanded_by):
        self.x = x
        self.y = y
        self.f = f
        self.g = g
        self.h = h
        self.was_visited = was_visited
        self.expanded_by = expanded_by
