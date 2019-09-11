import pygame

size = (480, 720)
fps = 60

full_screen = False

window = None

recorded_size = size


def toggle_full_screen():
    global full_screen, recorded_size, window, size

    full_screen = not full_screen

    if full_screen:
        recorded_size = size
        size = (1920, 1080)
        window = pygame.display.set_mode(size, pygame.FULLSCREEN)
    else:
        window = pygame.display.set_mode(recorded_size, pygame.RESIZABLE)
        size = recorded_size
