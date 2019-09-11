import pygame


class CursorManager:
    def __init__(self):
        self.position = pygame.mouse.get_pos()
        self.previous_pressed = self.pressed = pygame.mouse.get_pressed()
        self.start_pressed = list(self.pressed)
        self.end_pressed = list(self.pressed)

    def handle(self):
        self.position = pygame.mouse.get_pos()
        self.previous_pressed = self.pressed
        self.pressed = pygame.mouse.get_pressed()

    def tick(self):
        for i in range(3):
            self.start_pressed[i] = not self.previous_pressed[i] and self.pressed[i]
            self.end_pressed[i] = self.previous_pressed[i] and not self.pressed[i]
