import pygame


class GUI:
    def __init__(self, w, h):
        pygame.init()
        self.w = w
        self.h = h
        self.screen = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('SNAKE')
        self.clock = pygame.time.Clock()

    def getScreen(self):
        return self.screen

    def getClock(self):
        return self.clock
