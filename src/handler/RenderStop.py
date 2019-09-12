import pygame

import src.Display
from src.handler.Handler import Handler
from src.manager.KeyboardManager import KeyboardManager


class RenderStop(Handler):
    def __init__(self, keyboard_manager: KeyboardManager):
        self.keyboard_manager = keyboard_manager

    def tick(self):
        src.Display.render_enable = not self.keyboard_manager.keys[pygame.K_BACKSLASH]
