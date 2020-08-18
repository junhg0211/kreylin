from sys import platform

import pygame

from handler.handler import Handler


class Quit(Handler):
    def __init__(self, keyboard_manager, shutdown):
        self.keyboard_manager = keyboard_manager
        self.shutdown = shutdown

    def tick(self):
        if self.keyboard_manager.start_keys[pygame.K_F4]:
            if platform == 'win32':
                if self.keyboard_manager.keys[pygame.K_LALT] or self.keyboard_manager.keys[pygame.K_RALT]:
                    self.shutdown()
        if self.keyboard_manager.start_keys[pygame.K_q]:
            if platform == 'darwin':
                if self.keyboard_manager.keys[pygame.K_LMETA] or self.keyboard_manager.keys[pygame.K_RMETA]:
                    self.shutdown()
