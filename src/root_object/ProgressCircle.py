from math import tau
from pygame.surface import Surface

from src import Constants
from src.Font import Font
from src.drawshapes import arc
from src.root_object.RootObject import RootObject
from src.root_object.Text import Text


class ProgressCircle(RootObject):
    def __init__(self, center_x, center_y, max_radius, width, color, initial_progress: float = 0.0):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = max_radius
        self.width = width
        self.color = color
        self.progress = initial_progress

        font = Font(Constants.NANUMSQUARE_LIGHT_FONT, 72, Constants.TEXT_COLOR)
        self.circle_progress = Text(0, self.center_y - font.size / 2, '', font)

    def tick(self):
        self.circle_progress.set_text('%.3f%%' % (self.progress * 100))
        self.circle_progress.center_x()

    def render(self, surface: Surface):
        arc(surface, self.color, (self.center_x, self.center_y), self.radius, end=self.progress * tau, width=self.width)
        self.circle_progress.render(surface)

    def window_resize(self, width: int, height: int):
        self.center_x = width / 2
        self.center_y = height / 2 - 100
        self.circle_progress.y = self.center_y - self.circle_progress.font.size / 2
