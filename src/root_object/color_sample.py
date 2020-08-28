from pygame import gfxdraw
from pygame.surface import Surface

import constants
from font import Font
from root_object.root_object import RootObject


class ColorSample(RootObject):
    def __init__(self, x: int, y: int, radius: int, background_color: tuple, slider_color: tuple, text_color: tuple):
        self.x = x
        self.y = y
        self.radius = radius
        self.background_color = background_color
        self.slider_color = slider_color
        self.text_color = text_color

        self.white_font = Font(constants.NANUMSQUARE_REGULAR_FONT, radius // 3, (255, 255, 255))
        self.black_font = Font(constants.NANUMSQUARE_REGULAR_FONT, radius // 3, (0, 0, 0))

        self.background_surface = self.get_colored_font_by_color(self.background_color) \
            .render('#%02X%02X%02X' % self.background_color)
        self.slider_surface = self.get_colored_font_by_color(self.slider_color) \
            .render('#%02X%02X%02X' % self.slider_color)
        self.text_surface = self.get_colored_font_by_color(self.text_color) \
            .render('#%02X%02X%02X' % self.text_color)
        self.background_pos = (int(self.x + self.radius) - self.background_surface.get_width() / 2,
                               int(self.y + self.radius) - self.background_surface.get_height() / 2)
        self.slider_pos = (int(self.x + self.radius * 3.5) - self.slider_surface.get_width() / 2,
                           int(self.y + self.radius) - self.slider_surface.get_height() / 2)
        self.text_pos = (int(self.x + self.radius * 6) - self.text_surface.get_width() / 2,
                         int(self.y + self.radius) - self.text_surface.get_height() / 2)

    def get_colored_font_by_color(self, color) -> Font:
        return self.white_font if sum(color) < 150 else self.black_font

    def render(self, surface: Surface):
        gfxdraw.filled_circle(surface, int(self.x + self.radius), int(self.y + self.radius),
                              int(self.radius), self.background_color)
        surface.blit(self.background_surface, self.background_pos)
        gfxdraw.filled_circle(surface, int(self.x + self.radius * 3.5), int(self.y + self.radius),
                              int(self.radius), self.slider_color)
        surface.blit(self.slider_surface, self.slider_pos)
        gfxdraw.filled_circle(surface, int(self.x + self.radius * 6), int(self.y + self.radius),
                              int(self.radius), self.text_color)
        surface.blit(self.text_surface, self.text_pos)

    @staticmethod
    def get_width_by_radius(radius: int):
        return radius * 7
