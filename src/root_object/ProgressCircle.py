from pygame.surface import Surface

from src import Constants
from src.Font import Font
from src.root_object.Circle import Circle
from src.root_object.Text import Text


class ProgressCircle(Circle):
    def __init__(self, center_x, center_y, max_radius, width, color):
        super().__init__(center_x, center_y, max_radius, width, color)

        font = Font(Constants.NANUMSQUARE_LIGHT_FONT, 72, Constants.TEXT_COLOR)
        self.circle_progress = Text(0, self.center_y - font.size / 2, '', font)

    def tick(self):
        self.circle_progress.set_text('%.3f%%' % (self.progress * 100))
        self.circle_progress.center_x()

    def render(self, surface: Surface):
        super().render(surface)
        self.circle_progress.render(surface)

    def window_resize(self, width: int, height: int):
        super().window_resize(width, height)
        self.circle_progress.y = self.center_y - self.circle_progress.font.size / 2
