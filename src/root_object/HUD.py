from time import time

from pygame.surface import Surface

import Constants
import Display
from Font import Font
from handler.HandlerManager import HandlerManager
from manager.KeyboardManager import KeyboardManager
from root_object.RootObject import RootObject
from root_object.RootObjectManager import RootObjectManager
from state.StateManager import StateManager


class HUD(RootObject):
    def __init__(self, state_manager: StateManager, root_object_manager: RootObjectManager,
                 keyboard_manager: KeyboardManager, handler_manager: HandlerManager,
                 font_path: str = Constants.CONSOLAS_FONT, size: int = 15):
        self.state_manager = state_manager
        self.root_object_manager = root_object_manager
        self.keyboard_manager = keyboard_manager
        self.handler_manager = handler_manager
        self.font = Font(font_path, size, Constants.TEXT_COLOR)

        self.surfaces = []

        self.last_call = time()
        self.fps_time = 0
        self.real_fps = 0

    def recolor_background(self):
        self.font = Font(self.font.font_path, self.font.size, Constants.TEXT_COLOR)

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
            string = f'{Constants.PROJECT_NAME} {Constants.PROJECT_VERSION}\n\n' \
                f'Display_ {Display.size[0]}x{Display.size[1]}@{fps:f}\nReal-Fps {self.real_fps} fps\n' \
                f'Full-Screen_ {Display.full_screen}\n\n' \
                f'State_ {self.state_manager.state.__class__.__name__} ({self.state_manager.state})\n' \
                f'Object_ {len(self.root_object_manager.objects)}  Handler_ {len(self.handler_manager.handlers)}\n\n' \
                f'Keyboard_ {self.keyboard_manager.keys.count(True)}\n\n' \
                f'Global-Progress_ {Constants.progress:.030f}\n\n' \
                f'Color -\nResponsible-Color_ {Constants.responsible_color}\n' \
                f'Background_ {Constants.BACKGROUND_COLOR}\n' \
                f'Circle_ {Constants.CIRCLE_COLOR}\nText_ {Constants.TEXT_COLOR}'
        except TypeError:
            pass
        else:
            self.surfaces = [self.font.render(line) if line else None for line in string.split('\n')]

        self.last_call = call

    def render(self, surface: Surface):
        for i in range(len(self.surfaces)):
            if self.surfaces[i]:
                surface.blit(self.surfaces[i], (0, i * self.font.size))
