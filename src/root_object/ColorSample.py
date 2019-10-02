from pygame import gfxdraw
from pygame.surface import Surface

from root_object.RootObject import RootObject


class ColorSample(RootObject):
    def __init__(self, x: int, y: int, radius: int, background_color: tuple, slider_color: tuple, text_color: tuple):
        self.x = x
        self.y = y
        self.radius = radius
        self.background_color = background_color
        self.slider_color = slider_color
        self.text_color = text_color

    def render(self, surface: Surface):
        gfxdraw.filled_circle(surface, int(self.x + self.radius), int(self.y + self.radius),
                              int(self.radius), self.background_color)
        gfxdraw.filled_circle(surface, int(self.x + self.radius * 3.5), int(self.y + self.radius),
                              int(self.radius), self.slider_color)
        gfxdraw.filled_circle(surface, int(self.x + self.radius * 6), int(self.y + self.radius),
                              int(self.radius), self.text_color)

    @staticmethod
    def get_width_by_radius(radius: int):
        return radius * 7
