PROJECT_NAME = 'Kreylin'
PROJECT_VERSION = 'alpha_1.5'
PROJECT_ICON = './res/icon64.png'

BACKGROUND_COLOR = (31, 33, 37)
CIRCLE_COLOR = (253, 222, 89)
TEXT_COLOR = (222, 222, 222)

SKY_0_COLOR = 0, 7, 26
SKY_5_COLOR = 5, 21, 60
SKY_7_COLOR = 56, 179, 255
SKY_13_COLOR = 242, 250, 255
SKY_17_COLOR = 138, 193, 227
SKY_18_COLOR = 250, 108, 37
SKY_20_COLOR = 0, 17, 61


def change_color(background_color: tuple, circle_color: tuple, text_color: tuple):
    global BACKGROUND_COLOR, CIRCLE_COLOR, TEXT_COLOR

    BACKGROUND_COLOR = background_color
    CIRCLE_COLOR = circle_color
    TEXT_COLOR = text_color


# noinspection SpellCheckingInspection
CONSOLAS_FONT = './res/font/consola.ttf'
# noinspection SpellCheckingInspection
NANUMSQUARE_BOLD_FONT = './res/font/NANUMSQUAREB.TTF'
# noinspection SpellCheckingInspection
NANUMSQUARE_EXTRA_BOLD_FONT = './res/font/NANUMSQUAREEB.TTF'
# noinspection SpellCheckingInspection
NANUMSQUARE_LIGHT_FONT = './res/font/NANUMSQUAREL.TTF'
# noinspection SpellCheckingInspection
NANUMSQUARE_REGULAR_FONT = './res/font/NANUMSQUARER.TTF'

FRICTION = 12

progress = 0.0

responsible_color = True
