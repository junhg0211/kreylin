from datetime import datetime

import Constants
from Positioning import linear
from handler.Handler import Handler


# TODO 폰트 색상 반응형으로 만들기
from state.StateManager import StateManager


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
        if Constants.responsible_color:
            now = datetime.now()

            time = now.hour + now.minute / 60 + (now.second + now.microsecond / 1000000) / 13600

            if 0 <= time < 5:
                Constants.change_color(
                    linear_color(time, 0, 5, Constants.SKY_0_COLOR, Constants.SKY_5_COLOR),
                    Constants.CIRCLE_COLOR, Constants.TEXT_COLOR
                )
            elif 5 <= time < 7:
                Constants.change_color(
                    linear_color(time, 5, 7, Constants.SKY_5_COLOR, Constants.SKY_7_COLOR),
                    Constants.CIRCLE_COLOR, Constants.TEXT_COLOR
                )
            elif 7 <= time < 13:
                Constants.change_color(
                    linear_color(time, 7, 13, Constants.SKY_7_COLOR, Constants.SKY_13_COLOR),
                    Constants.CIRCLE_COLOR, Constants.TEXT_COLOR
                )
            elif 13 <= time < 17:
                Constants.change_color(
                    linear_color(time, 13, 17, Constants.SKY_13_COLOR, Constants.SKY_17_COLOR),
                    Constants.CIRCLE_COLOR, Constants.TEXT_COLOR
                )
            elif 17 <= time < 18:
                Constants.change_color(
                    linear_color(time, 17, 18, Constants.SKY_17_COLOR, Constants.SKY_18_COLOR),
                    Constants.CIRCLE_COLOR, Constants.TEXT_COLOR
                )
            elif 18 <= time < 20:
                Constants.change_color(
                    linear_color(time, 18, 20, Constants.SKY_18_COLOR, Constants.SKY_20_COLOR),
                    Constants.CIRCLE_COLOR, Constants.TEXT_COLOR
                )
            else:
                Constants.change_color(
                    linear_color(time, 20, 24, Constants.SKY_20_COLOR, Constants.SKY_0_COLOR),
                    Constants.CIRCLE_COLOR, Constants.TEXT_COLOR
                )

            color = (222, 222, 222) if sum(Constants.BACKGROUND_COLOR) < 300 else (31, 33, 37)
            if color != Constants.TEXT_COLOR or color != Constants.CIRCLE_COLOR:
                Constants.change_color(Constants.BACKGROUND_COLOR, color, color)
                try:
                    self.state_manager.state = self.state_manager.state.__class__()
                except TypeError:
                    self.state_manager.state.recolor()
