from pygame.surface import Surface


class RootObjectManager:
    def __init__(self):
        self.objects = []

    def tick(self):
        for _object_ in self.objects:
            _object_.tick()

    def render(self, surface: Surface):
        for _object_ in self.objects:
            _object_.render(surface)

    def add(self, _object_):
        self.objects.append(_object_)

    def remove(self, _object_):
        if _object_ in self.objects:
            self.objects.remove(_object_)

    def window_resize(self, width, height):
        for _object_ in self.objects:
            _object_.window_resize(width, height)