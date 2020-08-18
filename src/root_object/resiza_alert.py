from time import time

from pygame.surface import Surface

from constants import TEXT_COLOR, NANUMSQUARE_BOLD_FONT, BACKGROUND_COLOR
from font import Font
from positioning import center
from root_object.root_object import RootObject
from root_object.root_object_manager import RootObjectManager


class ResizeAlert(RootObject):
    def __init__(self, width, height, root_object_manager: RootObjectManager, timeout=1):
        self.width = width
        self.height = height
        self.root_object_manager = root_object_manager
        self.timeout = timeout

        self.start_time = time()

        self.background = Surface((300, 200))
        self.background.fill(BACKGROUND_COLOR)
        self.background.set_alpha(127)
        self.background_x = center(self.width, self.background.get_width())
        self.background_y = center(self.height, self.background.get_height())
        self.surface = Font(NANUMSQUARE_BOLD_FONT, 36, TEXT_COLOR).render(f'{width}x{height}')
        self.x = center(self.width, self.surface.get_width())
        self.y = center(self.height, self.surface.get_height())

        self.root_object_manager.remove_by_class(ResizeAlert)

    def tick(self):
        if time() - self.timeout > self.start_time:
            self.destroy()

    def render(self, surface: Surface):
        surface.blit(self.background, (self.background_x, self.background_y))
        surface.blit(self.surface, (self.x, self.y))

    def destroy(self):
        self.root_object_manager.remove(self)
