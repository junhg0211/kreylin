from time import time

from pygame.surface import Surface

import Constants
from src.handler.HandlerManager import HandlerManager
from src.manager.KeyboardManager import KeyboardManager
from src.root_object.RootObjectManager import RootObjectManager
from src import Display
from src.Font import Font
from src.root_object.RootObject import RootObject
from src.state.StateManager import StateManager


class HUD(RootObject):
    def __init__(self, state_manager: StateManager, root_object_manager: RootObjectManager,
                 keyboard_manager: KeyboardManager, handler_manager: HandlerManager,
                 font_path: str = Constants.CONSOLAS_FONT, size: int = 15, color: tuple = (255, 255, 255)):
        self.state_manager = state_manager
        self.root_object_manager = root_object_manager
        self.keyboard_manager = keyboard_manager
        self.handler_manager = handler_manager
        self.font = Font(font_path, size, color)

        self.surfaces = []

        self.last_call = time()

    def tick(self):
        call = time()

        try:
            fps = 1 / (call - self.last_call)
        except ZeroDivisionError:
            fps = None

        try:
            string = f'Display_ {Display.size[0]}x{Display.size[1]}@{fps:f}\nFull-Screen_ {Display.full_screen}\n\n' \
                f'State_ {self.state_manager.state.__class__.__name__} ({self.state_manager.state})\n' \
                f'Object_ {len(self.root_object_manager.objects)}  Handler_ {len(self.handler_manager.handlers)}\n\n' \
                f'Keyboard_ {self.keyboard_manager.keys.count(True)}'
        except TypeError:
            pass
        else:
            self.surfaces = [self.font.render(line) if line else None for line in string.split('\n')]

        self.last_call = call

    def render(self, surface: Surface):
        for i in range(len(self.surfaces)):
            if self.surfaces[i]:
                surface.blit(self.surfaces[i], (0, i * self.font.size))
