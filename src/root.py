import pygame

import constants
import display
from font import Font
from handler.handler_manager import HandlerManager
from handler.quit import Quit
from handler.render_stop import RenderStop
from handler.responsive_color import ResponsiveColor
from manager.keyboard_manager import KeyboardManager
from root_object.resize_alert import ResizeAlert
from root_object.root_object_manager import RootObjectManager
from root_object.terminal import Terminal
from state.clock import Clock
from state.state_manager import StateManager

running = True
clock = pygame.time.Clock()

# noinspection PyTypeChecker
keyboard_manager: KeyboardManager = None
# noinspection PyTypeChecker
root_object_manager: RootObjectManager = None
# noinspection PyTypeChecker
state_manager: StateManager = None
# noinspection PyTypeChecker
handler_manager: HandlerManager = None


def shutdown():
    global running

    running = False


def init():
    global keyboard_manager, root_object_manager, state_manager, handler_manager

    pygame.init()

    pygame.display.set_caption(f'{constants.PROJECT_NAME} {constants.PROJECT_VERSION}')
    pygame.display.set_icon(pygame.image.load(constants.PROJECT_ICON))

    display.window = pygame.display.set_mode(display.size, pygame.RESIZABLE)

    keyboard_manager = KeyboardManager()
    root_object_manager = RootObjectManager()
    state_manager = StateManager(Clock())
    handler_manager = HandlerManager()

    handler_manager.add(Quit(keyboard_manager, shutdown))
    handler_manager.add(RenderStop(keyboard_manager))
    handler_manager.add(ResponsiveColor(state_manager))

    root_object_manager.add(
        Terminal(constants.TEXT_COLOR, Font(constants.NANUMSQUARE_REGULAR_FONT, 32, constants.BACKGROUND_COLOR),
                 keyboard_manager, state_manager, root_object_manager, handler_manager, shutdown))


def handle():
    global running

    keyboard_manager.initialize()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            display.resize(event.dict['size'], root_object_manager, state_manager, ResizeAlert)
        elif event.type == pygame.KEYDOWN:
            keyboard_manager.key_pressed(event.key)
            keyboard_manager.pressed(event.unicode)
        elif event.type == pygame.KEYUP:
            keyboard_manager.key_released(event.key)


def tick():
    handler_manager.tick()

    state_manager.tick()
    root_object_manager.tick()


def render(surface):
    if display.render_enable:
        display.window.fill(constants.BACKGROUND_COLOR)

        state_manager.render(surface)
        root_object_manager.render(surface)

        pygame.display.flip()


def main():
    init()

    while running:
        handle()
        tick()
        render(display.window)

        clock.tick(display.fps)

    pygame.quit()
