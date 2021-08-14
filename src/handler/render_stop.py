import pygame

import display
from handler.handler import Handler
from manager.keyboard_manager import KeyboardManager


class RenderStop(Handler):
    def __init__(self, keyboard_manager: KeyboardManager):
        self.keyboard_manager = keyboard_manager

    def tick(self):
        display.render_enable = not self.keyboard_manager.is_pressed(pygame.K_BACKSLASH)
