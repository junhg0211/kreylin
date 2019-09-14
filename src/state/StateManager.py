from pygame.surface import Surface

from state.State import State


class StateManager:
    def __init__(self, initial_state: State):
        self.state: State = initial_state

    def tick(self):
        self.state.tick()

    def render(self, surface: Surface):
        self.state.render(surface)
    
    def window_resize(self, width, height):
        self.state.window_resize(width, height)
