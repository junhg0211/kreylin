from time import time

from pygame.surface import Surface

import constants
import display
from font import Font
from handler.handler_manager import HandlerManager
from manager.keyboard_manager import KeyboardManager
from root_object.root_object import RootObject
from root_object.root_object_manager import RootObjectManager
from state.state_manager import StateManager


class HUD(RootObject):
    def __init__(self, state_manager: StateManager, root_object_manager: RootObjectManager,
                 keyboard_manager: KeyboardManager, handler_manager: HandlerManager,
                 font_path: str = constants.CONSOLAS_FONT, size: int = 15):
        self.state_manager = state_manager
        self.root_object_manager = root_object_manager
        self.keyboard_manager = keyboard_manager
        self.handler_manager = handler_manager
        self.font = Font(font_path, size, constants.TEXT_COLOR)

        self.surfaces = []

        self.last_call = time()
        self.fps_time = 0
        self.real_fps = 0

    def recolor_background(self):
        self.font = Font(self.font.font_path, self.font.size, constants.TEXT_COLOR)

    def tick(self):
        call = time()
        self.fps_time += 1
        if int(self.last_call) < int(call):
            self.real_fps = self.fps_time
            self.fps_time = 0

        try:
            fps = 1 / (call - self.last_call)
        except ZeroDivisionError:
            fps = None

        try:
            string = f'{constants.PROJECT_NAME} {constants.PROJECT_VERSION}\n\n' \
                f'Display_ {display.size[0]}x{display.size[1]}@{fps:f}\nReal-Fps {self.real_fps} fps\n' \
                f'Full-Screen_ {display.full_screen}\n\n' \
                f'State_ {self.state_manager.state.__class__.__name__} ({self.state_manager.state})\n' \
                f'Object_ {len(self.root_object_manager.objects)}  Handler_ {len(self.handler_manager.handlers)}\n\n' \
                f'Keyboard_ {self.keyboard_manager.keys.count(True)}\n\n' \
                f'Global-Progress_ {constants.progress:.030f}\n\n' \
                f'Color -\nResponsible-Color_ {constants.responsible_color}\n' \
                f'Background_ {constants.BACKGROUND_COLOR}\n' \
                f'Circle_ {constants.CIRCLE_COLOR}\nText_ {constants.TEXT_COLOR}'
        except TypeError:
            pass
        else:
            self.font.set_color(constants.TEXT_COLOR)
            self.surfaces = [self.font.render(line) if line else None for line in string.split('\n')]

        self.last_call = call

    def render(self, surface: Surface):
        for i in range(len(self.surfaces)):
            if self.surfaces[i]:
                surface.blit(self.surfaces[i], (0, i * self.font.size))
