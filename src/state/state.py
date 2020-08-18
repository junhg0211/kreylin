from pygame.surface import Surface


class State:
    def __init__(self):
        self.objects = []

    def tick(self):
        for object_ in self.objects:
            object_.tick()

    def render(self, surface: Surface):
        for object_ in self.objects:
            object_.render(surface)

    def recolor(self):
        pass

    def window_resize(self, width: int, height: int):
        pass
