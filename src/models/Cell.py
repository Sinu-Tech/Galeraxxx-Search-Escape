class Cell():
    def __init__(self, x: int, y: int, was_visited: bool, expanded_by):
        self.x = x
        self.y = y
        self.h = 0
        self.g = 0
        self.was_visited = was_visited
        self.expanded_by = expanded_by
