def center(x, y):
    return (x - y) / 2


def linear(value, m1, x1, m2, x2):
    return ((value - m1) / (x1 - m1)) * (x2 - m2) + m2
