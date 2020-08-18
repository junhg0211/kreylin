from math import cos, sin, tau

from pygame.gfxdraw import aapolygon, filled_polygon


def center(x, y):
    return (x - y) / 2


def linear(value, m1, x1, m2, x2):
    return ((value - m1) / (x1 - m1)) * (x2 - m2) + m2


def draw_arc(surface, x, y, r, th, start, stop, color):
    # from https://stackoverflow.com/a/57457571
    stop %= tau

    points_outer = []
    points_inner = []
    n = round(r * abs(stop - start) / 20)
    if n < 2:
        n = 2
    for i in range(n):
        delta = i / (n - 1)
        phi0 = start + (stop - start) * delta
        x0 = round(x + r * cos(phi0))
        y0 = round(y + r * sin(phi0))
        points_outer.append([x0, y0])
        phi1 = stop + (start - stop) * delta
        x1 = round(x + (r - th) * cos(phi1))
        y1 = round(y + (r - th) * sin(phi1))
        points_inner.append([x1, y1])
    points = points_outer + points_inner
    aapolygon(surface, points, color)
    filled_polygon(surface, points, color)