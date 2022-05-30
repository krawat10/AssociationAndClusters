from typing import List
from Models.Point import Point


class Cluster:
    middle: Point
    points: List[Point]
    k: int

    def __init__(self, middle, k):
        self.middle = middle
        self.k = k
        self.points = []

    def add_point(self, point: Point):
        self.points.append(point)

    def clear_points(self):
        self.points = []

    def update_middle(self) -> bool:
        has_changed = False
        new_middle = Point(0.0, 0.0)

        for point in self.points:
            new_middle.x += point.x
            new_middle.y += point.y

        new_middle.x /= float(len(self.points))
        new_middle.y /= float(len(self.points))

        if new_middle.x != self.middle.x or new_middle.y != self.middle.y:
            has_changed = True

        self.middle = new_middle
        return has_changed
