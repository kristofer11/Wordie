"""
This is the main entry-point to my word game, WORDIE (think Wordle)
"""

import os
from features.game import game
from features.instructions import instructions
# from words import word_list
# from features.api.words import request_word
from scraper.past_words import get_random_word
from features.colors import (
    light_text,
    blue_text,
    magenta_background,
    default_background,
    red_text
)

os.system('clear')

print(f'\n{light_text}{magenta_background}Welcome to WORDIE.{default_background}')

#Ask user if they want to hear directions
instructions_query = input(f'\nWould you like to hear the {blue_text}directions{light_text}? (y/n) ')

#If they want to hear the directions, print them
if instructions_query.upper() == 'Y' or instructions_query.upper() == 'YES':
    instructions()

#Ask if they want to start a game
ready = input(f'\nAre you ready to play {red_text}Wordie{light_text}!? (y/n)')

#If they want to start a game, start it
if ready == 'y' or ready.upper() == 'YES' or ready.upper() == 'Y':
    game(get_random_word)
