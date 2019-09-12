import pygame

from src import Constants, Display
from src.Font import Font
from src.handler.HandlerManager import HandlerManager
from src.handler.Quit import Quit
from src.handler.RenderStop import RenderStop
from src.manager.KeyboardManager import KeyboardManager
from src.root_object.HUD import HUD
from src.root_object.RootObjectManager import RootObjectManager
from src.root_object.Terminal import Terminal
from src.state.Clock import Clock
from src.state.StateManager import StateManager

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

    Display.window = pygame.display.set_mode(Display.size, pygame.RESIZABLE)

    pygame.display.set_caption(Constants.PROJECT_NAME)
    pygame.display.set_icon(pygame.image.load(Constants.PROJECT_ICON))

    keyboard_manager = KeyboardManager()
    root_object_manager = RootObjectManager()
    state_manager = StateManager(Clock())
    handler_manager = HandlerManager()

    handler_manager.add(Quit(keyboard_manager, shutdown))
    handler_manager.add(RenderStop(keyboard_manager))

    root_object_manager.add(
        Terminal(Constants.TEXT_COLOR, Font(Constants.NANUMSQUARE_REGULAR_FONT, 32, Constants.BACKGROUND_COLOR),
                 keyboard_manager, state_manager, root_object_manager, handler_manager, shutdown))


def handle():
    global running

    keyboard_manager.initialize()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            Display.size = event.dict['size']
            if Display.full_screen:
                Display.window = pygame.display.set_mode(Display.size, pygame.FULLSCREEN)
            else:
                Display.window = pygame.display.set_mode(Display.size, pygame.RESIZABLE)
            Display.resize_objects(root_object_manager, state_manager)
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
    if Display.render_enable:
        Display.window.fill(Constants.BACKGROUND_COLOR)

        state_manager.render(surface)
        root_object_manager.render(surface)

        pygame.display.flip()


def main():
    init()

    while running:
        handle()
        tick()
        render(Display.window)

        clock.tick(Display.fps)

    pygame.quit()
