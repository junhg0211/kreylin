from pygame.font import Font as _Font_
from pygame.surface import Surface


class Font:
    def __init__(self, font_path, size, color):
        self.font_path = font_path
        self.size = size
        self.color = color

        self.font = None
        self.refresh_font()

    def render(self, text) -> Surface:
        return self.font.render(text, True, self.color)

    def set_color(self, color: tuple):
        self.color = color
        self.refresh_font()

    def refresh_font(self):
        self.font = _Font_(self.font_path, self.size)
