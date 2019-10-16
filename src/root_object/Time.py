from datetime import datetime

from pygame.surface import Surface

import Constants
from Font import Font
from root_object.RootObject import RootObject
from root_object.Text import Text


class Time(RootObject):
    def __init__(self, y):
        self.y = y

        self.time = Text(0, self.y, '',
                         Font(Constants.NANUMSQUARE_BOLD_FONT, 72, Constants.TEXT_COLOR))
        self.millisecond = Text(0, self.time.y + self.time.font.size, '',
                                Font(Constants.NANUMSQUARE_REGULAR_FONT, 32, Constants.TEXT_COLOR))

    def set_color(self, text_color):
        self.time.font.set_color(text_color)
        self.millisecond.font.set_color(text_color)

    def tick(self):
        now = datetime.now()

        self.time.set_text(str(now)[11:19])
        self.time.center_x()
        self.millisecond.set_text(('.%06d' % now.microsecond)[:5])
        self.millisecond.x = self.time.x + self.time.surface.get_width() - self.millisecond.surface.get_width()

    def render(self, surface: Surface):
        self.time.render(surface)
        self.millisecond.render(surface)

    def window_resize(self, width: int, height: int):
        self.y = height / 2 + 150
        self.time.y = self.y
        self.millisecond.y = self.y + self.time.font.size
