# https://stackoverflow.com/a/57457571

import math
import pygame


# noinspection PyUnresolvedReferences
def draw_arc(surface, x, y, r, th, start, stop, color):
    points_outer = []
    points_inner = []
    n = round(r * abs(stop - start) / 20)
    if n < 2:
        n = 2
    for i in range(n):
        delta = i / (n - 1)
        phi0 = start + (stop - start) * delta
        x0 = round(x + r * math.cos(phi0))
        y0 = round(y + r * math.sin(phi0))
        points_outer.append([x0, y0])
        phi1 = stop + (start - stop) * delta
        x1 = round(x + (r - th) * math.cos(phi1))
        y1 = round(y + (r - th) * math.sin(phi1))
        points_inner.append([x1, y1])
    points = points_outer + points_inner
    pygame.gfxdraw.aapolygon(surface, points, color)
    pygame.gfxdraw.filled_polygon(surface, points, color)
