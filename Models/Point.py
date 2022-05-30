import math


class Point:
    x = 0.0
    y = 0.0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, point) -> float:
        return math.sqrt(math.pow(self.x - point.x, 2) + math.pow(self.y - point.y, 2))
