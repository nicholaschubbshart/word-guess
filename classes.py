import pygame
from pygame.locals import *


class Guess:

    def __init__(self, screen, left, top, width, height):

        self.screen = screen
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.rect = pygame.draw.rect(screen, (127,127,127), (left,top,width,height), 2)
        self.font = pygame.font.SysFont("Roboto", 80)
    
    def add_guess(self, letter):

        w, h = self.font.size(letter)

        xoff = (self.width - w) // 2
        yoff = (self.height - h) // 2

        self.screen.blit(self.font.render(letter, True, (255,255,255)), (self.left + xoff, self.top + yoff+4))
        pygame.display.update()
