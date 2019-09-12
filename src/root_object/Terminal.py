from datetime import datetime, timedelta

import pygame.draw
from pygame.surface import Surface

from src import Display
from src.Font import Font
from src.Positioning import center
from src.manager.KeyboardManager import KeyboardManager
from src.root_object.RootObject import RootObject
from src.root_object.RootObjectManager import RootObjectManager
from src.state.Alarm import Timer
from src.state.Clock import Clock
from src.state.StateManager import StateManager
from src.state.Stopwatch import Stopwatch


class Terminal(RootObject):
    def __init__(self, background_color, font: Font, keyboard_manager: KeyboardManager, state_manager: StateManager,
                 root_object_manager: RootObjectManager, shutdown):
        self.background_color = background_color
        self.font: Font = font
        self.keyboard_manager: KeyboardManager = keyboard_manager
        self.state_manager: StateManager = state_manager
        self.root_object_manager = root_object_manager
        self.shutdown = shutdown

        self.line = ''
        self.surface = Surface([0, 0])

        self.x = 0
        self.y = 100

    def tick(self):
        self.line += self.keyboard_manager.pop_buffer()
        while '\x7f' in self.line:
            i = self.line.index('\x7f')
            self.line = self.line[:i-1] + self.line[i+1:]
        while '\b' in self.line:
            i = self.line.index('\b')
            self.line = self.line[:i-1] + self.line[i+1:]

        self.surface = self.font.render(self.line)

        self.x = center(Display.size[0], self.surface.get_width())

        if self.keyboard_manager.start_keys[pygame.K_ESCAPE]:
            self.line = ''
        elif self.line == 'c\n':
            self.state_manager.state = Clock()
        elif len(self.line) > 1 and (self.keyboard_manager.start_keys[pygame.K_RETURN] or
                                     self.keyboard_manager.start_keys[pygame.K_KP_ENTER]):
            if self.line[-2] == '.':
                self.alarm(self.line)
            elif self.line[-2] == '`':
                self.timer(self.line)
            elif self.line[-2] == '/':
                self.state_manager.state = Stopwatch()
            elif self.line[-2] == '-':
                self.state_manager.state = Clock()
            elif self.line[-2] == 'x':
                self.shutdown()
            elif self.line[-2] == 'f':
                Display.toggle_full_screen(self.root_object_manager, self.state_manager)

            self.line = ''

    def render(self, surface: Surface):
        if self.line:
            pygame.draw.rect(surface, self.background_color, ((self.x, self.y),
                                                              (self.surface.get_width(), self.surface.get_height())))
            surface.blit(self.surface, (self.x, self.y))

    def alarm(self, line):
        now = datetime.now()
        year, month, day = now.year, now.month, now.day
        hour, minute, second = now.hour, now.minute, now.second
        change = True
        if len(line) == 6:
            try:
                hour, minute, second = int(line[:2]), int(line[2:4]), 0
            except ValueError:
                change = False
        elif len(line) == 8:
            try:
                hour, minute, second = int(line[:2]), int(line[2:4]), int(line[4:6])
            except ValueError:
                change = False
        elif len(line) == 14:
            try:
                year, month, day = int(line[:4]), int(line[4:6]), int(line[6:8])
                hour, minute, second = int(line[8:10]), int(line[10:12]), 0
            except ValueError:
                change = False
        elif len(line) == 16:
            try:
                year, month, day = int(line[:4]), int(line[4:6]), int(line[6:8])
                hour, minute, second = int(line[8:10]), int(line[10:12]), int(line[12:14])
            except ValueError:
                change = False
        if change:
            try:
                target = datetime(year, month, day, hour, minute, second, now.microsecond)
            except ValueError:
                pass
            else:
                if now < target:
                    self.state_manager.state = Timer(target, self.state_manager)

    def timer(self, line):
        now = datetime.now()
        year, day = 0, 0
        hour, minute, second = 0, 0, 0
        change = True
        try:
            minute += int(line[:-2])
        except ValueError:
            try:
                tmp = float(line[:-3])
            except ValueError:
                change = False
            else:
                if line[-3].lower() == 's':
                    second += tmp
                elif line[-3].lower() == 'h':
                    hour += tmp
                elif line[-3].lower() == 'd':
                    day += tmp
                elif line[-3].lower() == 'y':
                    year += tmp
            while second > 60:
                second -= 60
                minute += 1
            while minute > 60:
                minute -= 60
                hour += 1
            while hour > 24:
                hour -= 24
                day += 1
        if change:
            try:
                target = now + timedelta(days=(year * 365 + day), hours=hour, minutes=minute, seconds=second)
            except ValueError:
                pass
            else:
                if now < target:
                    self.state_manager.state = Timer(target, self.state_manager)
