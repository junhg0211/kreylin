from datetime import datetime

import constants
from positioning import linear
from handler.handler import Handler

# TODO 폰트 색상 반응형으로 만들기
from state.state_manager import StateManager


def linear_color(value, m, x, c1, c2) -> tuple:
    return (
        linear(value, m, x, c1[0], c2[0]),
        linear(value, m, x, c1[1], c2[1]),
        linear(value, m, x, c1[2], c2[2])
    )


class ResponsiveColor(Handler):
    def __init__(self, state_manager: StateManager):
        self.state_manager: StateManager = state_manager

    def tick(self):
        if constants.responsible_color:
            now = datetime.now()

            time = now.hour + now.minute / 60 + (now.second + now.microsecond / 1000000) / 13600

            if 0 <= time < 5:
                constants.change_color(
                    linear_color(time, 0, 5, constants.SKY_0_COLOR, constants.SKY_5_COLOR),
                    constants.CIRCLE_COLOR, constants.TEXT_COLOR
                )
            elif 5 <= time < 7:
                constants.change_color(
                    linear_color(time, 5, 7, constants.SKY_5_COLOR, constants.SKY_7_COLOR),
                    constants.CIRCLE_COLOR, constants.TEXT_COLOR
                )
            elif 7 <= time < 13:
                constants.change_color(
                    linear_color(time, 7, 13, constants.SKY_7_COLOR, constants.SKY_13_COLOR),
                    constants.CIRCLE_COLOR, constants.TEXT_COLOR
                )
            elif 13 <= time < 17:
                constants.change_color(
                    linear_color(time, 13, 17, constants.SKY_13_COLOR, constants.SKY_17_COLOR),
                    constants.CIRCLE_COLOR, constants.TEXT_COLOR
                )
            elif 17 <= time < 18:
                constants.change_color(
                    linear_color(time, 17, 18, constants.SKY_17_COLOR, constants.SKY_18_COLOR),
                    constants.CIRCLE_COLOR, constants.TEXT_COLOR
                )
            elif 18 <= time < 20:
                constants.change_color(
                    linear_color(time, 18, 20, constants.SKY_18_COLOR, constants.SKY_20_COLOR),
                    constants.CIRCLE_COLOR, constants.TEXT_COLOR
                )
            else:
                constants.change_color(
                    linear_color(time, 20, 24, constants.SKY_20_COLOR, constants.SKY_0_COLOR),
                    constants.CIRCLE_COLOR, constants.TEXT_COLOR
                )

            color = (222, 222, 222) if sum(constants.BACKGROUND_COLOR) < 300 else (31, 33, 37)
            if color != constants.TEXT_COLOR or color != constants.CIRCLE_COLOR:
                constants.change_color(constants.BACKGROUND_COLOR, color, color)
                try:
                    self.state_manager.state = self.state_manager.state.__class__()
                except TypeError:
                    self.state_manager.state.recolor()
