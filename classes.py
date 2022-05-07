import pygame
from pygame.locals import *


class Guess:

    def __init__(self, screen, left, top, width, height):

        self.screen = screen
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.letter = ""
        self.rect = pygame.draw.rect(screen, (127,127,127), (left,top,width,height), 2)
        self.font = pygame.font.SysFont("Roboto", 80)
    
    def add_guess(self, letter):

        self.letter = letter
        w, h = self.font.size(letter)

        xoff = (self.width - w) // 2
        yoff = (self.height - h) // 2

        self.screen.blit(self.font.render(letter, True, (255,255,255)), (self.left + xoff, self.top + yoff+4))
        pygame.display.update()

    def remove_guess(self):
        if (self.letter != ""):
            self.rect = pygame.draw.rect(self.screen, (0,0,0), (self.left,self.top,self.width,self.height))
            self.rect = pygame.draw.rect(self.screen, (127,127,127), (self.left,self.top,self.width,self.height), 2)
            pygame.display.update()

    def get_letter(self):
        return self.letter
    
    def green(self):
        self.rect = pygame.draw.rect(self.screen, (0,128,0), (self.left,self.top,self.width,self.height))
        self.rect = pygame.draw.rect(self.screen, (127,127,127), (self.left,self.top,self.width,self.height), 2)
        self.add_guess(self.letter)
        pygame.display.update()

    def red(self):
        self.rect = pygame.draw.rect(self.screen, (255,0,0), (self.left,self.top,self.width,self.height))
        self.rect = pygame.draw.rect(self.screen, (127,127,127), (self.left,self.top,self.width,self.height), 2)
        self.add_guess(self.letter)
        pygame.display.update()


class Key:

    def __init__(self, screen, left, top, width, height, key, size):

        self.screen = screen
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.key = key
        self.rect = pygame.draw.rect(screen, (127,127,127), (left,top,width,height), 2)
        self.font = pygame.font.SysFont("Roboto", size)
    
    def add_key(self):

        w, h = self.font.size(self.key)

        xoff = (self.width - w) // 2
        yoff = (self.height - h) // 2

        self.screen.blit(self.font.render(self.key, True, (255,255,255)), (self.left + xoff, self.top + yoff+2))
        pygame.display.update()

    def get_key(self):
        return self.key

    def click(self):
        self.rect = pygame.draw.rect(self.screen, (255,165,0), (self.left,self.top,self.width,self.height))
        self.rect = pygame.draw.rect(self.screen, (127,127,127), (self.left,self.top,self.width,self.height), 2)
        self.add_key()
        pygame.display.update()

    def unclick(self):
        self.rect = pygame.draw.rect(self.screen, (0,0,0), (self.left,self.top,self.width,self.height))
        self.rect = pygame.draw.rect(self.screen, (127,127,127), (self.left,self.top,self.width,self.height), 2)
        self.add_key()
        pygame.display.update()


class Play:

    def __init__(self, guess_space, answer):
        self.guess_space = guess_space
        self.answer = answer
        self.row = 0
        self.col = 0
        self.max_row = 6
        self.max_col = 5

    def add_guess(self, guess):

        if (guess == "ENT"):
            if (self.check_row()):
                return "won"
            else:
                self.row += 1
                self.col = 0
                if (self.row == self.max_row):
                    return "lost"
        elif (guess == "DEL"):
            self.col -= 1
            if (self.col < 0):
                self.col = 0
            self.guess_space[self.row][self.col].remove_guess()
        elif (self.col < self.max_col):
            self.guess_space[self.row][self.col].add_guess(guess)
            self.col += 1

    def check_row(self):
        guessed = ""

        for i in range(0, self.max_col):
            guessed += self.guess_space[self.row][i].get_letter()
        
        if(guessed == self.answer):
            for i in range(0, self.max_col):
                self.guess_space[self.row][i].green()
            return True
        else:
            for i in range(0, self.max_col):
                self.guess_space[self.row][i].red()
            return False
