import pygame

class Stage:
    def __init__(self, surface):
        self.timer = pygame.time.get_ticks()
        self.surface = surface
