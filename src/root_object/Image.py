from pygame import image
from pygame.surface import Surface

from root_object.root_object import RootObject


class Image(RootObject):
    def __init__(self, x: int, y: int, path: str):
        self.x = x
        self.y = y
        self.path = path

        self._surface = image.load(path)
        self.width = self._surface.get_width()
        self.height = self._surface.get_height()

    def render(self, surface: Surface):
        surface.blit(self._surface, (self.x, self.y))
