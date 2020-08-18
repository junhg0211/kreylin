from datetime import datetime, timedelta

from pygame.surface import Surface

import constants
import display
from font import Font
from positioning import center
from root_object.circle import Circle
from root_object.text import Text
from root_object.time import Time
from state.state import State


class Stopwatch(State):
    def __init__(self, start_time=None):
        super().__init__()
        self.start_time = start_time
        if self.start_time is None:
            self.start_time = datetime.now()

        self.circle = Circle(0, 0, 190, 20, constants.CIRCLE_COLOR, constants.progress)
        font = Font(constants.NANUMSQUARE_REGULAR_FONT, 72, constants.TEXT_COLOR)
        self.elapsed_time = Text(0, 0, '', font)
        font2 = Font(constants.NANUMSQUARE_LIGHT_FONT, 32, constants.TEXT_COLOR)
        self.elapsed_microsecond = Text(0, 0, '', font2)
        self.elapsed_days = Text(0, 0, '', font2)

        self.days = 0

        self.time = Time(0)

        self.start_text: Text = Text(0, 0, str(self.start_time).split('.')[0],
                                     Font(constants.NANUMSQUARE_LIGHT_FONT, 32, constants.TEXT_COLOR))

        self.window_resize(*display.size)

    # noinspection DuplicatedCode
    def tick(self):
        now = datetime.now()
        
        constants.progress = (now.second + now.microsecond / 1000000) / 60
        self.circle.tick()

        delta = now - self.start_time
        self.elapsed_time.set_text(str(delta % timedelta(days=1)).split('.')[0])
        self.elapsed_time.x = center(display.size[0], self.elapsed_time.surface.get_width())
        self.elapsed_microsecond.set_text(f'.{delta.microseconds:06d}')
        self.elapsed_microsecond.x = center(display.size[0], self.elapsed_microsecond.surface.get_width())

        self.days = delta // timedelta(days=1)
        if self.days:
            self.elapsed_days.set_text(f'{self.days} day' + ('' if self.days == 1 else 's'))
            self.elapsed_days.x = center(display.size[0], self.elapsed_days.surface.get_width())

        self.time.tick()

    def render(self, surface: Surface):
        super().render(surface)

        self.circle.render(surface)
        self.elapsed_time.render(surface)
        self.elapsed_microsecond.render(surface)
        self.time.render(surface)
        self.start_text.render(surface)
        if self.days:
            self.elapsed_days.render(surface)

    def window_resize(self, width: int, height: int):
        self.circle.window_resize(width, height)
        self.elapsed_time.y = self.circle.center_y - self.elapsed_time.font.size / 2
        self.elapsed_microsecond.y = self.elapsed_time.y + self.elapsed_time.font.size
        self.time.window_resize(width, height)
        self.start_text.x = center(width, self.start_text.surface.get_width())
        self.start_text.y = self.time.y - self.start_text.font.size
        self.elapsed_days.x = center(width, self.elapsed_days.surface.get_width())
        self.elapsed_days.y = self.elapsed_time.y - self.elapsed_days.font.size
