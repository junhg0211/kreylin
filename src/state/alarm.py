from datetime import datetime

from pygame.surface import Surface

import display, constants
from font import Font
from util import center
from root_object.progress_circle import ProgressCircle
from root_object.text import Text
from root_object.time import Time
from sound.sound import play_wav
from state.clock import Clock
from state.state import State
from state.state_manager import StateManager


class Timer(State):
    END_SOUND = './res/sound/ding.wav'

    def __init__(self, target: datetime, state_manager: StateManager):
        super().__init__()

        self.target = target
        self.state_manager = state_manager

        self.start_time = datetime.now()

        self.circle = ProgressCircle(0, 0, 190, 20, constants.CIRCLE_COLOR, constants.progress)
        self.last_time = Text(0, 0, '', Font(constants.NANUMSQUARE_REGULAR_FONT, 16, constants.TEXT_COLOR))

        self.time = Time(0)
        self.target_time: Text = Text(0, 0, str(self.target).split('.')[0],
                                      Font(constants.NANUMSQUARE_LIGHT_FONT, 32, constants.TEXT_COLOR))

        self.window_resize(*display.size)

    def recolor(self):
        self.last_time.font.set_color(constants.TEXT_COLOR)
        self.target_time.set_color(constants.TEXT_COLOR)
        self.circle.set_color(constants.CIRCLE_COLOR, constants.TEXT_COLOR)
        self.time.set_color(constants.TEXT_COLOR)

    def tick(self):
        now = datetime.now()

        constants.progress = (now - self.start_time) / (self.target - self.start_time)
        self.circle.tick()

        self.last_time.set_text(str(self.target - now))
        self.last_time.x = center(display.size[0], self.last_time.surface.get_width())

        self.time.tick()

        if constants.progress >= 1:
            self.state_manager.state = Clock()
            play_wav(Timer.END_SOUND)

    def render(self, surface: Surface):
        super().render(surface)

        self.circle.render(surface)
        self.last_time.render(surface)
        self.time.render(surface)
        self.target_time.render(surface)

    def window_resize(self, width: int, height: int):
        self.circle.window_resize(width, height)
        self.last_time.y = self.circle.center_y + self.circle.circle_progress.font.size / 2
        self.time.window_resize(width, height)
        self.target_time.x = center(width, self.target_time.surface.get_width())
        self.target_time.y = self.time.y - self.target_time.font.size

