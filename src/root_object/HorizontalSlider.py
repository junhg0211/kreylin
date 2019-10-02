from pygame.draw import rect
from pygame.surface import Surface

from root_object.RootObject import RootObject


class HorizontalSlider(RootObject):
    def __init__(self, x: int, y: int, length: int, color: tuple, thickness: int = 4):
        self.x = x
        self.y = y
        self.length = length
        self.thickness = thickness
        self.color = color

        self.value: float = 0.0

    def render(self, surface: Surface):
        rect(surface, self.color, ((self.x, self.y), (self.length, self.thickness)))
