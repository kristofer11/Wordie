import time

def inst_delay():
    time.sleep(2)

def instructions():
    print('\nDirections: \n')
    inst_delay()
    print('\nThe Goal: guess the secret 5-letter word.')
    inst_delay()
    print('Type any 5-letter, English word.')
    inst_delay()
    print('When you get a letter correct, in the correct spot, it will change to \033[32mgreen\033[30m.')
    inst_delay()
    print('Letters that are in the word, but in a different spot will be \033[33myellow\033[30m.')
    inst_delay()
    print('Letters that are not in the word will not change color.')
    inst_delay()
    print("You get 5 tries, make 'em count!")
    inst_delay()