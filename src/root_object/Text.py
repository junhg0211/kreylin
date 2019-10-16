from pygame.surface import Surface

import Display
from Font import Font
from Positioning import center
from root_object.RootObject import RootObject


class Text(RootObject):
    def __init__(self, x, y, text, font):
        self.x = x
        self.y = y
        self.text = text
        self.font: Font = font

        self.surface = None
        self.reload_surface()

    def set_color(self, color):
        self.font.set_color(color)
        self.reload_surface()

    def reload_surface(self):
        self.surface = self.font.render(self.text)

    def set_text(self, text):
        self.text = text
        self.reload_surface()

    def center_x(self):
        self.x = center(Display.size[0], self.surface.get_width())

    def center_y(self):
        self.y = center(Display.size[1], self.surface.get_width())

    def render(self, surface: Surface):
        surface.blit(self.surface, (self.x, self.y))
