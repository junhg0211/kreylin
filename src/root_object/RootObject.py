from pygame.surface import Surface


class RootObject:
    def tick(self):
        pass

    def render(self, surface: Surface):
        pass

    def window_resize(self, width: int, height: int):
        pass
