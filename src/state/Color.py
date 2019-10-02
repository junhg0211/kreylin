import Constants
import Display
from Font import Font
from Positioning import center
from root_object.ColorSample import ColorSample
from root_object.Text import Text
from state.State import State


class Color(State):
    SAMPLE_PALETTES = (
        ((31, 33, 37), (253, 222, 89), (222, 222, 222)),
        ((62, 62, 50), (217, 37, 52), (239, 223, 187)),
        ((13, 13, 13), (166, 131, 88), (215, 215, 217))
    )

    def __init__(self):
        super().__init__()

        radius = 50
        center_x = center(Display.size[0], ColorSample.get_width_by_radius(radius))
        y_offset = 120

        font = Font(Constants.NANUMSQUARE_BOLD_FONT, radius // 3 * 2, Constants.TEXT_COLOR)

        for i in range(len(Color.SAMPLE_PALETTES)):
            x, y = center_x, i * radius * 4 + y_offset
            self.objects.append(ColorSample(x, y, radius, *Color.SAMPLE_PALETTES[i]))
            self.objects.append(Text(x + font.size // 3, y - font.size * 1.5, chr(i + ord('G')), font))
