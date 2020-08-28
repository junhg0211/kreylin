from pygame.surface import Surface

import display
from font import Font
from util import center
from root_object.root_object import RootObject


class Text(RootObject):
    def __init__(self, x, y, text, font):
        self.x = x
        self.y = y
        self.text = text
        self.font: Font = font

        self._surface = None
        self.width = 0
        self.height = 0
        self.reload_surface()

    def set_color(self, color):
        self.font.set_color(color)
        self.reload_surface()

    def reload_surface(self):
        self._surface = self.font.render(self.text)
        self.width = self._surface.get_width()
        self.height = self._surface.get_height()

    def set_text(self, text):
        self.text = text
        self.reload_surface()

    def center_x(self):
        self.x = center(display.size[0], self.width)

    def center_y(self):
        self.y = center(display.size[1], self.height)

    def render(self, surface: Surface):
        surface.blit(self._surface, (self.x, self.y))
