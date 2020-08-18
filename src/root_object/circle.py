from math import tau

from pygame.surface import Surface

import constants
from drawshapes import arc
from root_object.root_object import RootObject


class Circle(RootObject):
    def __init__(self, center_x, center_y, max_radius, width, color, initial_progress: float = 0.0):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = max_radius
        self.width = width
        self.color = color
        self.progress = initial_progress

    def tick(self):
        self.progress += (constants.progress - self.progress) / constants.FRICTION

    def render(self, surface: Surface):
        arc(surface, self.color, (self.center_x, self.center_y), self.radius, end=self.progress * tau, width=self.width)

    def window_resize(self, width: int, height: int):
        self.center_x = width / 2
        self.center_y = height / 2 - 100
