import pygame
from pygame.locals import *


class Rect:

    def __init__(self, screen, left, top, width, height):
        self.rect = pygame.draw.rect(screen, (127,127,127), (left,top,width,height), 2)
