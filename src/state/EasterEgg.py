from root_object.RandomImage import RandomImage
from state.State import State


class EasterEgg(State):
    def __init__(self):
        super().__init__()

        self.objects = [
            RandomImage('./res/image/pudding_guito.png'),
            RandomImage('./res/image/rabbit_guito.png')
        ]
