from pygame.surface import Surface

import Constants
from root_object.HorizontalSlider import HorizontalSlider
from state.State import State


class Color(State):
    def __init__(self):
        super().__init__()
        
        self.length = 300
        self.gap = 30

        x = 100
        y = 100

        self.background_red = HorizontalSlider(x, y , self.length, Constants.TEXT_COLOR)
        self.background_green = HorizontalSlider(x, y + self.gap, self.length, Constants.TEXT_COLOR)
        self.background_blue = HorizontalSlider(x, y + self.gap * 2, self.length, Constants.TEXT_COLOR)

        self.text_red = HorizontalSlider(x, y + self.gap * 4, self.length, Constants.TEXT_COLOR)
        self.text_green = HorizontalSlider(x, y + self.gap * 5, self.length, Constants.TEXT_COLOR)
        self.text_blue = HorizontalSlider(x, y + self.gap * 6, self.length, Constants.TEXT_COLOR)

        self.progress_red = HorizontalSlider(x, y + self.gap * 8, self.length, Constants.TEXT_COLOR)
        self.progress_green = HorizontalSlider(x, y + self.gap * 9, self.length, Constants.TEXT_COLOR)
        self.progress_blue = HorizontalSlider(x, y + self.gap * 10, self.length, Constants.TEXT_COLOR)

    def render(self, surface: Surface):
        self.background_red.render(surface)
        self.background_green.render(surface)
        self.background_blue.render(surface)

        self.text_red.render(surface)
        self.text_green.render(surface)
        self.text_blue.render(surface)

        self.progress_red.render(surface)
        self.progress_green.render(surface)
        self.progress_blue.render(surface)
