"""
This is the main entry-point to my word game, WORDIE (think Wordle)
"""
import os
from features.game import game
from features.instructions import instructions
# from words import word_list
# from features.api.words import request_word
from scraper.past_words import get_random_word

os.system('clear')

print('\033[36mWelcome to WORDIE.\n')

instructions_query = input('\nWould you like to hear the \033[34minstructions\033[30m? (y/n) ')

if instructions_query == 'y':
    instructions()

ready = input('Are you ready to play Wordie!? (y/n)')

if ready == 'y':
    game(get_random_word)