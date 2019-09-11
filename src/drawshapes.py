# drawshapes.py
# written by Jeffrey Kleykamp

import math
import pygame

TAU = 2 * math.pi


def get_polygon(origin, radius, n, start=0, end=None):
    out = []
    x, y = origin
    nf = float(n)
    if end is None:
        end = TAU
    for i in range(n):
        xp = x + radius * math.sin(end * i / nf + start)
        yp = y - radius * math.cos(end * i / nf + start)
        out.append((xp, yp))
    return out


def reg_polygon(surf, color, origin, radius, width, n, start=0):
    if width == 0 or width >= radius:
        pl = get_polygon(origin, radius, n)
        r = pygame.draw.polygon(surf, color, pl)
        return r
    else:
        end = TAU * (n + 1) / float(n)
        p1 = get_polygon(origin, radius, n + 1, start=start, end=end)
        p2 = get_polygon(origin, radius - width, n + 1, start=start, end=end)
        p2.reverse()
        p1.extend(p2)
        r = pygame.draw.polygon(surf, color, p1)
        return r


def circle(surf, color, origin, radius, width=0, n=64):
    reg_polygon(surf, color, origin, radius, width, n, 0)


def arc(surf, color, origin, radius, start=0, end=None, width=0, n=64):
    if width == 0 or width >= radius * 0.5:
        p2 = [origin]
    else:
        p2 = get_polygon(origin, radius - width, n, start=start, end=end)
        p2.reverse()
    p1 = get_polygon(origin, radius, n, start=start, end=end)
    p1.extend(p2)
    r = pygame.draw.polygon(surf, color, p1)
    return r


def wedge(surf, color, origin, radius, start=0, end=None, width=0, n=64):
    if width == 0 or width >= radius * 0.5:
        return arc(surf, color, origin, radius, start=start, end=end, width=0, n=n)
    # does outside polygon
    p1 = [origin]
    p2 = get_polygon(origin, radius, n, start=start, end=end)
    p3 = [origin]
    p1.extend(p2)
    p1.extend(p3)

    # does inside polygon
    x, y = origin
    xp = x + width * math.sin(end * 0.5 + start)
    yp = y - width * math.cos(end * 0.5 + start)
    n_origin = (xp, yp)
    p3 = [n_origin]
    p2 = get_polygon(n_origin, radius - 2 * width, n, start=start, end=end)
    p2.reverse()
    p1.extend(p3)
    p1.extend(p2)
    p1.extend(p3)

    # draws the full polygon
    r = pygame.draw.polygon(surf, color, p1)
    return r


def ellipse(surf, color, rect, width=0, n=64):
    # draws an ellipse that bounds the rect
    x_radius = rect.width * 0.5
    y_radius = rect.height * 0.5
    origin = rect.center

    return ellipse_radius(surf, color, origin, x_radius, y_radius, width=width, n=n)


def ellipse_radius(surf, color, origin, x_radius, y_radius, width=0, n=64):
    # draws an ellipse that has the two radii
    pl = []
    x, y = origin
    if width >= min(x_radius, y_radius):
        width = 0
    if width is 0:
        end = TAU
    else:
        end = TAU * (n + 1) / float(n)
        n = n + 1
    nf = float(n)

    for i in range(n):
        xp = x + x_radius * math.sin(end * i / nf)
        yp = y - y_radius * math.cos(end * i / nf)
        pl.append((xp, yp))

    if width is not 0:
        x_radius -= width
        y_radius -= width
        for i in range(n):
            xp = x + x_radius * math.sin(-end * i / nf)
            yp = y - y_radius * math.cos(-end * i / nf)
            pl.append((xp, yp))

    r = pygame.draw.polygon(surf, color, pl)
    return r
