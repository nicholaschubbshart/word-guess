import pygame
from pygame.locals import *

import classes as cla


def main():
    pygame.init()
    pygame.display.set_caption("word-guess")
    screen = pygame.display.set_mode((420,840))

    guess_space = []

    for j in range(1, 7):
        row = []
        for i in range (1, 6):
            temp = cla.Guess(screen, (60*i), (60*j), 60, 60)
            row.append(temp)
        guess_space.append(row)

    alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    i = 0
    j = 0
    for letter in alp:
        guess_space[i][j].add_guess(letter)
        j += 1
        if (j == 5):
            i += 1
            j = 0

        if(i == 6):
            break

    driver_gate = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                driver_gate = False

        if(driver_gate == False):
            break

        pygame.display.update()


if __name__ == "__main__":
    main()