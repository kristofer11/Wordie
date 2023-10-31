"""
This is the main entry-point to my word game clone (think Wordle)
"""

import os
import time
import random

word_list = ['first', 'words', 'sword', 'cooks', 'yeast', 'beers', 'water']

os.system('clear')

def inst_delay():
    time.sleep(2)

def instructions():
    print('\nDirections: \n')
    inst_delay()
    print('\nThe Goal: guess the secret 5-letter word.')
    inst_delay()
    print('Type any 5-letter, English word.')
    inst_delay()
    print('When you get a letter correct, in the correct spot, it will change to \033[32mgreen\033[0m.')
    inst_delay()
    print('Letters that are in the word, but in a different spot will be yellow.')
    inst_delay()
    print('Letters that are not in the word will not change color.')
    inst_delay()
    print("You get 5 tries, make 'em count!")
    inst_delay()

def game():
    os.system('clear')
    turn = 0
    word = random.choice(word_list)
    while turn < 5:
        guess = input('Enter your guess: ')
        print(guess)
        turn += 1
    print(word)

print('\033[36mWelcome to WORDIE. It is unlike any game you have played on any newspaper website...\033[30m')

instructions_query = input('\nWould you like to hear the \033[34minstructions\033[30m? (y/n) ')

if instructions_query == 'y':
    instructions()

ready = input('Are you ready to play Wordie!? (y/n)')

if ready == 'y':
    game()