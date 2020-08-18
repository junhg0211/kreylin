from random import random

import display
from root_object.Image import Image


def limit(value, m, x):
    return max(min(value, x), m)


class RandomImage(Image):
    def __init__(self, path: str):
        super().__init__(100, 100, path)

        self.speed = 20000 / self.surface.get_height()
        self.speed = 20000 / self.surface.get_height()

    def tick(self):
        delta_x = (random() - 0.5) * self.speed
        delta_y = (random() - 0.5) * self.speed

        self.x = limit(self.x + delta_x, 0, display.size[0] - self.surface.get_width())
        self.y = limit(self.y + delta_y, 0, display.size[1] - self.surface.get_height())
