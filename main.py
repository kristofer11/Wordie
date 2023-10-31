"""
This is the main entry-point to my word game clone (think Wordle)
"""
import os
from features.game import game
from features.instructions import instructions
from words import word_list

os.system('clear')

print('\033[36mWelcome to WORDIE.\n')
print('It is unlike any game you have played on any newspaper website...\033[30m')

instructions_query = input('\nWould you like to hear the \033[34minstructions\033[30m? (y/n) ')

if instructions_query == 'y':
    instructions()

ready = input('Are you ready to play Wordie!? (y/n)')

if ready == 'y':
    game(word_list)
