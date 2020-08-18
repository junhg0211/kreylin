from root_object.random_image import RandomImage
from state.state import State


class EasterEgg(State):
    def __init__(self):
        super().__init__()

        self.objects = [
            RandomImage('./res/image/pudding_guito.png'),
            RandomImage('./res/image/rabbit_guito.png')
        ]
