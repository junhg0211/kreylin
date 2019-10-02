from pygame import image
from pygame.surface import Surface

from root_object.RootObject import RootObject


class Image(RootObject):
    def __init__(self, x: int, y: int, path: str):
        self.x = x
        self.y = y
        self.path = path

        self.surface = image.load(path)

    def render(self, surface: Surface):
        surface.blit(self.surface, (self.x, self.y))
