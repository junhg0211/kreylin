from datetime import datetime, timedelta
from time import time

import pygame.draw
from pygame.surface import Surface

import constants
import display
from font import Font
from root_object.resize_alert import ResizeAlert
from util import center
from handler.handler_manager import HandlerManager
from manager.keyboard_manager import KeyboardManager
from root_object.hud import HUD
from root_object.root_object import RootObject
from root_object.root_object_manager import RootObjectManager
from state.alarm import Timer
from state.clock import Clock
from state.color import Color
from state.easter_egg import EasterEgg
from state.state_manager import StateManager
from state.stopwatch import Stopwatch


class Terminal(RootObject):
    def __init__(self, background_color, font: Font, keyboard_manager: KeyboardManager, state_manager: StateManager,
                 root_object_manager: RootObjectManager, handler_manager: HandlerManager, shutdown):
        self.background_color = background_color
        self.font: Font = font
        self.keyboard_manager: KeyboardManager = keyboard_manager
        self.state_manager: StateManager = state_manager
        self.root_object_manager = root_object_manager
        self.handler_manager = handler_manager
        self.shutdown = shutdown

        self.line = ''
        self.surface = Surface([0, 0])

        self.surface_background_width = 0

        self.x = 0
        self.y = 100

        self.backspace_pressed_time = 0
        self.backspace_sleep_duration = 0.5
        self.backspace_repress_cycle = 0.05
        self.backspace_cycle_elapsed = 0

        self.last_loop_time = 0

    def tick(self):
        loop_time = time()
        if self.keyboard_manager.start_keys[pygame.K_BACKSPACE]:
            self.backspace_pressed_time = time()
        if self.keyboard_manager.keys[pygame.K_BACKSPACE] and \
                self.backspace_sleep_duration + self.backspace_pressed_time <= time():
            self.backspace_cycle_elapsed += loop_time - self.last_loop_time
            if self.backspace_cycle_elapsed >= self.backspace_repress_cycle:
                self.line += '\b'
                self.backspace_cycle_elapsed -= self.backspace_repress_cycle

        self.line += self.keyboard_manager.pop_buffer()
        while '\x7f' in self.line:
            i = self.line.index('\x7f')
            self.line = self.line[:i-1] + self.line[i+1:]
        while '\b' in self.line:
            i = self.line.index('\b')
            self.line = self.line[:i-1] + self.line[i+1:]

        self.surface = self.font.render(self.line)
        self.surface_background_width += \
            (self.surface.get_width() - self.surface_background_width) / constants.FRICTION

        start_time = center(display.size[0], self.surface.get_width())
        self.x += (start_time - self.x) / (constants.FRICTION / 3)

        if self.keyboard_manager.start_keys[pygame.K_ESCAPE]:
            self.line = ''
        elif self.line == 'c\n':
            self.state_manager.state = Clock()
        elif len(self.line) > 1 and (self.keyboard_manager.start_keys[pygame.K_RETURN] or
                                     self.keyboard_manager.start_keys[pygame.K_KP_ENTER]):
            self.line = self.line.lower()

            # noinspection SpellCheckingInspection
            if self.line[-2] == '.':
                self.alarm(self.line)
            elif self.line[-2] == '`':
                self.timer(self.line)
            elif self.line[-2] == '/':
                now = datetime.now()
                year, day = 0, 0
                hour, minute, second = 0, 0, 0
                change = True
                try:
                    minute += float(self.line[:-2])
                except ValueError:
                    try:
                        tmp = float(self.line[:-3])
                    except ValueError:
                        change = False
                    else:
                        if self.line[-3].lower() == 's':
                            second += tmp
                        elif self.line[-3].lower() == 'h':
                            hour += tmp
                        elif self.line[-3].lower() == 'd':
                            day += tmp
                        elif self.line[-3].lower() == 'y':
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
                        start_time = now - timedelta(days=(year * 365 + day), hours=hour, minutes=minute, seconds=second)
                    except ValueError:
                        pass
                    except OverflowError:
                        pass
                    else:
                        self.state_manager.state = Stopwatch(start_time)
                else:
                    self.state_manager.state = Stopwatch()
            elif self.line[-2] == '-':
                self.state_manager.state = Clock()
            elif self.line[-2] == 'x':
                self.shutdown()
            elif self.line[-2] == 'f':
                display.toggle_full_screen(self.root_object_manager, self.state_manager)
            elif self.line[-2] == 'h':
                self.root_object_manager.hud = None if self.root_object_manager.hud else \
                    HUD(self.state_manager, self.root_object_manager, self.keyboard_manager, self.handler_manager)
            elif self.line[-2] == 'c':
                constants.responsible_color = False
                if len(self.line) >= 19:
                    constants.change_color(
                        (int(self.line[:2], 16), int(self.line[2:4], 16), int(self.line[4:6], 16)),
                        (int(self.line[6:8], 16), int(self.line[8:10], 16), int(self.line[10:12], 16)),
                        (int(self.line[12:14], 16), int(self.line[14:16], 16), int(self.line[16:18], 16)))
                    self.state_manager.state = Clock()
                elif len(self.line) >= 3:
                    if ord(self.line[-3].upper()) - ord('G') < len(Color.SAMPLE_PALETTES):
                        constants.change_color(*Color.SAMPLE_PALETTES[ord(self.line[-3].upper()) - ord('G')])
                    self.state_manager.state = Clock()
                else:
                    if isinstance(self.state_manager.state, Color):
                        constants.responsible_color = True
                        self.state_manager.state = Clock()
                    else:
                        self.state_manager.state = Color()
                if self.root_object_manager.hud is not None:
                    self.root_object_manager.hud.recolor_background()
            elif self.line[-2] == 's':
                if 'x' in (resolution := self.line[:-2]):
                    width, height = resolution.split('x')
                    width, height = int(width), int(height)
                    display.resize((width, height), self.root_object_manager, self.state_manager, ResizeAlert)
                else:
                    display.resize((480, 720), self.root_object_manager, self.state_manager, ResizeAlert)
            elif self.line[-2] == 'o':
                Timer.PLAY_SOUND = not Timer.PLAY_SOUND
            elif self.line.lower().startswith('uuddlrlrab'):
                self.state_manager.state = EasterEgg()

            self.line = ''

        self.last_loop_time = loop_time

    def render(self, surface: Surface):
        if self.line or self.surface_background_width > 3:
            margin = 5

            pygame.draw.rect(surface, self.background_color,
                             ((center(surface.get_width(), self.surface_background_width + margin*4), self.y - margin),
                              (self.surface_background_width + margin*4, self.surface.get_height() + margin * 2)))
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
            minute += float(line[:-2])
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
            except OverflowError:
                pass
            else:
                if now < target:
                    self.state_manager.state = Timer(target, self.state_manager)
