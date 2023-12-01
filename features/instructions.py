"""
Prints instructions if user chooses to view them.
"""

import time
from features.colors import green_background, yellow_background, default_background

def inst_delay():
    """
    Provides delay between each line of instructions
    """
    time.sleep(1.5)

def instructions():
    """
    Prints rules/instructions for gameplay
    """
    print('\nDirections: \n')
    inst_delay()
    print('\nThe Goal: guess the secret 5-letter word.')
    inst_delay()
    print('Type any 5-letter, English word.')
    inst_delay()
    print(f'When you get a letter correct, in the correct spot, it will change to {green_background}green{default_background}.')
    inst_delay()
    print(f'Letters that are in the word, but in a different spot will be {yellow_background}yellow{default_background}.')
    inst_delay()
    print('Letters that are not in the word will not change color.')
    inst_delay()
    print("You get 5 tries, make 'em count!")
    inst_delay()