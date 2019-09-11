from datetime import datetime

from pygame.surface import Surface

from src import Display, Constants
from src.Font import Font
from src.Positioning import center
from src.root_object.ProgressCircle import ProgressCircle
from src.root_object.Text import Text
from src.root_object.Time import Time
from src.state.Clock import Clock
from src.state.State import State
from src.state.StateManager import StateManager


class Timer(State):
    def __init__(self, target: datetime, state_manager: StateManager):
        super().__init__()

        self.target = target
        self.state_manager = state_manager

        self.start_time = datetime.now()

        self.circle = ProgressCircle(0, 0, 190, 20, Constants.CIRCLE_COLOR)

        self.time = Time(0)
        self.target_time: Text = Text(0, 0, str(self.target).split('.')[0],
                                      Font(Constants.NANUMSQUARE_LIGHT_FONT, 32, Constants.TEXT_COLOR))

        self.target_time.x = center(Display.size[0], self.target_time.surface.get_width())

        self.window_resize(*Display.size)

    def tick(self):
        now = datetime.now()

        self.circle.progress = (now - self.start_time) / (self.target - self.start_time)
        self.circle.tick()

        self.time.tick()

        if self.circle.progress >= 1:
            self.state_manager.state = Clock()

    def render(self, surface: Surface):
        super().render(surface)

        self.circle.render(surface)
        self.time.render(surface)
        self.target_time.render(surface)

    def window_resize(self, width: int, height: int):
        self.circle.window_resize(width, height)
        self.time.window_resize(width, height)
        self.target_time.x = center(width, self.target_time.surface.get_width())
        self.target_time.y = self.time.y - self.target_time.font.size

