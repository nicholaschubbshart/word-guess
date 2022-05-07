import pygame
from pygame.locals import *

import sys
import time

import classes as cla

def get_pressed(key_board, cords):

    for row in key_board:
        for col in row:
            left, top = col[1]
            width, height = col[2]
            
            if ((left <= cords[0] and cords[0] <= (left + width)) and (top <= cords[1] and cords[1] <= (top + height))):
                col[0].click()
                time.sleep(0.1)
                col[0].unclick()
                return col[0].get_key()


def add_guess(main_play, pressed):

    is_over = main_play.add_guess(pressed)
    return is_over

def reset_screen(screen):
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (127,127,127), (60,180,300,300))
    pygame.display.update()

def display_won(screen):
    time.sleep(0.5)
    reset_screen(screen)

    gate = True
    while(gate):
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    gate = False

def display_lost(screen):
    time.sleep(0.5)
    reset_screen(screen)

    gate = True
    while(gate):
        for event in pygame.event.get():
                gate = False

def check_result(screen, result):

    if (result == "won"):
        display_won(screen)
        return True
    elif (result == "Lost"):
        display_lost(screen)
        return True

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
            temp = cla.Key(screen, key_left, key_top, 30, 30, keys[j][i], 30)
            temp.add_key()
            row.append([temp, [key_left, key_top], [30, 30]])
            key_left += 30

        key_left = 60
        key_top += 30
        key_board.append(row)

    # add enter and backspace buttons
    temp = []
    en = cla.Key(screen, 60, 540, 45, 30, "ENT", 20)
    en.add_key()
    temp.append([en, [60, 540], [45, 30]])
    for ele in key_board[2]:
        temp.append(ele)
    de = cla.Key(screen, 315, 540, 45, 30, "DEL", 20)
    de.add_key()
    temp.append([de, [315, 540], [45, 30]])
    key_board[2] = temp

    to_be_guessed = "HELLO" ###################################################################

    main_play = cla.Play(guess_space, to_be_guessed)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed():
                pos = pygame.mouse.get_pos()
                pressed = get_pressed(key_board, pos)

                result = add_guess(main_play, pressed)
                check = check_result(screen, result)

                if (check):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


if __name__ == "__main__":
    main()