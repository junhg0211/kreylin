from pygame.surface import Surface


class State:
    def __init__(self):
        self.objects = []

    def tick(self):
        for _object_ in self.objects:
            _object_.tick()

    def render(self, surface: Surface):
        for _object_ in self.objects:
            _object_.render(surface)

    def window_resize(self, width: int, height: int):
        pass
