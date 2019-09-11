from pygame.surface import Surface

from src import Display
from src.Font import Font
from src.Positioning import center
from src.root_object.RootObject import RootObject


class Text(RootObject):
    def __init__(self, x, y, text, font):
        self.x = x
        self.y = y
        self.text = text
        self.font: Font = font

        self.surface = None
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
