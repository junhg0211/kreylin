from datetime import datetime

from pygame.surface import Surface

from src import Constants, Display
from src.Font import Font
from src.Positioning import center
from src.root_object.Circle import Circle
from src.root_object.Text import Text
from src.root_object.Time import Time
from src.state.State import State


class Stopwatch(State):
    def __init__(self):
        super().__init__()

        self.circle = Circle(0, 0, 190, 20, Constants.CIRCLE_COLOR, Constants.progress)
        font = Font(Constants.NANUMSQUARE_REGULAR_FONT, 72, Constants.TEXT_COLOR)
        self.elapsed_time = Text(0, 0, '', font)
        font2 = Font(Constants.NANUMSQUARE_LIGHT_FONT, 32, Constants.TEXT_COLOR)
        self.elapsed_microsecond = Text(0, 0, '', font2)

        self.time = Time(0)

        self.start_time = datetime.now()
        self.start_text: Text = Text(0, 0, str(self.start_time).split('.')[0],
                                     Font(Constants.NANUMSQUARE_LIGHT_FONT, 32, Constants.TEXT_COLOR))

        self.window_resize(*Display.size)

    def tick(self):
        now = datetime.now()
        
        Constants.progress = (now.second + now.microsecond / 1000000) / 60
        self.circle.tick()

        delta = now - self.start_time
        self.elapsed_time.set_text(str(delta).split('.')[0])
        self.elapsed_time.x = center(Display.size[0], self.elapsed_time.surface.get_width())
        self.elapsed_microsecond.set_text(f'.{delta.microseconds:06d}')
        self.elapsed_microsecond.x = center(Display.size[0], self.elapsed_microsecond.surface.get_width())

        self.time.tick()

    def render(self, surface: Surface):
        super().render(surface)

        self.circle.render(surface)
        self.elapsed_time.render(surface)
        self.elapsed_microsecond.render(surface)
        self.time.render(surface)
        self.start_text.render(surface)

    def window_resize(self, width: int, height: int):
        self.circle.window_resize(width, height)
        self.elapsed_time.y = self.circle.center_y - self.elapsed_time.font.size / 2
        self.elapsed_microsecond.y = self.elapsed_time.y + self.elapsed_time.font.size
        self.time.window_resize(width, height)
        self.start_text.x = center(width, self.start_text.surface.get_width())
        self.start_text.y = self.time.y - self.start_text.font.size
