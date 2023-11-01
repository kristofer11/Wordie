"""
This is the main entry-point to my word game, WORDIE (think Wordle)
"""

import os
from features.game import game
from features.instructions import instructions
# from words import word_list
# from features.api.words import request_word
from scraper.past_words import get_random_word
from features.colors import light_text
from features.colors import blue_text
from features.colors import magenta_background, default_background
from features.colors import red_text

os.system('clear')

print(f'{light_text}{magenta_background}Welcome to WORDIE.{default_background}')

instructions_query = input(f'\nWould you like to hear the {blue_text}directions{light_text}? (y/n) ')

if instructions_query.upper() == 'Y' or instructions_query.upper() == 'YES':
    instructions()

ready = input(f'\nAre you ready to play {red_text}Wordie{light_text}!? (y/n)')

if ready == 'y' or ready.upper() == 'YES' or ready.upper() == 'Y':
    game(get_random_word)