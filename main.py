import pygame
from pygame.locals import *

import sys
import time

import classes as cla

def get_pressed(key_board, cords):

    for row in key_board:
        for col in row:
            left, top = col[1]
            
            if ((left <= cords[0] and cords[0] <= (left + 30)) and (top <= cords[1] and cords[1] <= (top + 30))):
                col[0].click()
                time.sleep(0.1)
                col[0].unclick()
                return col[0].get_key()


def add_guess(main_play, pressed):

    is_over = main_play.add_guess(pressed)
    print(is_over)
    return is_over


def main():
    pygame.init()
    pygame.display.set_caption("word-guess")
    screen = pygame.display.set_mode((420,700))

    guess_space = []
    key_board = []

    # create guess space
    for j in range(1, 7):
        row = []
        for i in range (1, 6):
            temp = cla.Guess(screen, (60*i), (60*j), 60, 60)
            row.append(temp)
        guess_space.append(row)

    # create keyboard
    key_top = (60*8)
    key_left = 60
    layout = [10, 9, 7]
    keys = ["QWERTYUIOP","ASDFGHJKL","ZXCVBNM"]

    for j in range(0, 3):

        if (j == 2):
            key_left += 45
        else:
            key_left += (15*j)

        row = []
        for i in range (0, layout[j]):
            temp = cla.Key(screen, key_left, key_top, 30, 30, keys[j][i])
            temp.add_key()
            row.append([temp, [key_left, key_top]])
            key_left += 30

        key_left = 60
        key_top += 30
        key_board.append(row)
    

    # # TO BE REMOVED
    # alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # i = 0 # row number
    # j = 0 # col number
    # for letter in alp:
    #     guess_space[i][j].add_guess(letter)
    #     j += 1
    #     if (j == 5):
    #         i += 1
    #         j = 0

    #     if(i == 6):
    #         break

    to_be_guessed = "HELLO"

    main_play = cla.Play(guess_space, to_be_guessed)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed():
                pos = pygame.mouse.get_pos()
                pressed = get_pressed(key_board, pos)

                add_guess(main_play, pressed)

        pygame.display.update()


if __name__ == "__main__":
    main()