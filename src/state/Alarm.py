from datetime import datetime

from pygame.surface import Surface

import Display, Constants
from Font import Font
from Positioning import center
from root_object.ProgressCircle import ProgressCircle
from root_object.Text import Text
from root_object.Time import Time
from sound.Sound import play_wav
from state.Clock import Clock
from state.State import State
from state.StateManager import StateManager


class Timer(State):
    END_SOUND = './res/sound/ding.wav'

    def __init__(self, target: datetime, state_manager: StateManager):
        super().__init__()

        self.target = target
        self.state_manager = state_manager

        self.start_time = datetime.now()

        self.circle = ProgressCircle(0, 0, 190, 20, Constants.CIRCLE_COLOR, Constants.progress)
        self.last_time = Text(0, 0, '', Font(Constants.NANUMSQUARE_REGULAR_FONT, 16, Constants.TEXT_COLOR))

        self.time = Time(0)
        self.target_time: Text = Text(0, 0, str(self.target).split('.')[0],
                                      Font(Constants.NANUMSQUARE_LIGHT_FONT, 32, Constants.TEXT_COLOR))

        self.window_resize(*Display.size)

    def recolor(self):
        self.last_time.font.set_color(Constants.TEXT_COLOR)
        self.target_time.set_color(Constants.TEXT_COLOR)
        self.circle.set_color(Constants.CIRCLE_COLOR, Constants.TEXT_COLOR)
        self.time.set_color(Constants.TEXT_COLOR)

    def tick(self):
        now = datetime.now()

        Constants.progress = (now - self.start_time) / (self.target - self.start_time)
        self.circle.tick()

        self.last_time.set_text(str(self.target - now))
        self.last_time.x = center(Display.size[0], self.last_time.surface.get_width())

        self.time.tick()

        if Constants.progress >= 1:
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

