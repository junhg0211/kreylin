import constants
import display
from font import Font
from util import center
from root_object.color_sample import ColorSample
from root_object.text import Text
from state.state import State


class Color(State):
    SAMPLE_PALETTES = (
        ((31, 33, 37), (253, 222, 89), (222, 222, 222)),
        ((62, 62, 50), (217, 37, 52), (239, 223, 187)),
        ((13, 13, 13), (166, 131, 88), (215, 215, 217))
    )

    def __init__(self):
        super().__init__()

        self.radius = 50
        center_x = center(display.size[0], ColorSample.get_width_by_radius(self.radius))
        y_offset = center(display.size[1], self.radius * 9.6)

        self.font = Font(constants.NANUMSQUARE_BOLD_FONT, self.radius // 3 * 2, constants.TEXT_COLOR)

        for i in range(len(Color.SAMPLE_PALETTES)):
            x, y = center_x, i * self.radius * 4 + y_offset
            self.objects.append(ColorSample(x, y, self.radius, *Color.SAMPLE_PALETTES[i]))
            self.objects.append(Text(x + self.font.size // 3, y - self.font.size * 1.5, chr(i + ord('G')), self.font))

    def window_resize(self, width: int, height: int):
        center_x = center(display.size[0], ColorSample.get_width_by_radius(self.radius))
        y_offset = center(display.size[1], self.radius * 9.6)

        self.objects = []
        for i in range(len(Color.SAMPLE_PALETTES)):
            x, y = center_x, i * self.radius * 4 + y_offset
            self.objects.append(ColorSample(x, y, self.radius, *Color.SAMPLE_PALETTES[i]))
            self.objects.append(Text(x + self.font.size // 3, y - self.font.size * 1.5, chr(i + ord('G')), self.font))

    def recolor(self):
        self.font.set_color(constants.TEXT_COLOR)
