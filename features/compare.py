#WORDS FOR TESTING...
# word1 = ['a', 'b', 'c', 'd', 'e']
# word2 = ['a', 'b', 'c', 'd', 'e']

#ADD A Y TO THE END OF EACH LETTER OF WORD2 THAT IS IN THE SECRET WORD
def is_present(secret_word, guess):
    if guess[0] in secret_word:
        guess[0] = guess[0] + 'y'
    if guess[1] in secret_word:
        guess[1] = guess[1] + 'y'
    if guess[2] in secret_word:
        guess[2] = guess[2] + 'y'
    if guess[3] in secret_word:
        guess[3] = guess[3] + 'y'
    if guess[4] in secret_word:
        guess[4] = guess[4] + 'y'

    # CHECK EACH LETTER THAT IS PRESENT AND SEE IF IT IS IN THE RIGHT PLACE
    if len(guess[0]) > 1:
        if guess[0][0] == secret_word[0][0]:
            guess[0] = guess[0] + 'g'
    if len(guess[1]) > 1:
        if guess[1][0] == secret_word[1][0]:
            guess[1] = guess[1] + 'g'
    if len(guess[2]) > 1:
        if guess[2][0] == secret_word[2][0]:
            guess[2] = guess[2] + 'g'
    if len(guess[3]) > 1:
        if guess[3][0] == secret_word[3][0]:
            guess[3] = guess[3] + 'g'
    if len(guess[4]) > 1:
        if guess[4][0] == secret_word[4][0]:
            guess[4] = guess[4] + 'g'
    return guess

# def compare(word1, word2):

# is_present(word1, word2)

def interpret_word(word):
    word_string = ''

#CHECK TO SEE IF FIRST LETTER IS RIGHT PLACE, WRONG PLACE, OR NOT PRESENT/CHANGE COLOR ACCORDINGLY
    if len(word[0]) == 3:
        word_string += f'\033[32m{word[0][0]}\033[0m'
    elif len(word[0]) == 2:
        word_string += f'\033[33m{word[0][0]}\033[0m'
    else:
        word_string += word[0][0]

#CHECK TO SEE IF SECOND LETTER IS RIGHT PLACE, WRONG PLACE, OR NOT PRESENT/CHANGE COLOR ACCORDINGLY
    if len(word[1]) == 3:
        word_string += f'\033[32m{word[1][0]}\033[0m'
    elif len(word[1]) == 2:
        word_string += f'\033[33m{word[1][0]}\033[0m'
    else:
        word_string += word[1][0]
        
#CHECK TO SEE IF THIRD LETTER IS RIGHT PLACE, WRONG PLACE, OR NOT PRESENT/CHANGE COLOR ACCORDINGLY
    if len(word[2]) == 3:
        word_string += f'\033[32m{word[2][0]}\033[0m'
    elif len(word[2]) == 2:
        word_string += f'\033[33m{word[2][0]}\033[0m'
    else:
        word_string += word[2][0]
#CHECK TO SEE IF FOURTH LETTER IS RIGHT PLACE, WRONG PLACE, OR NOT PRESENT/CHANGE COLOR ACCORDINGLY
    if len(word[3]) == 3:
        word_string += f'\033[32m{word[3][0]}\033[0m'
    elif len(word[3]) == 2:
        word_string += f'\033[33m{word[3][0]}\033[0m'
    else:
        word_string += word[3][0]
#CHECK TO SEE IF FIFTH LETTER IS RIGHT PLACE, WRONG PLACE, OR NOT PRESENT/CHANGE COLOR ACCORDINGLY
    if len(word[4]) == 3:
        word_string += f'\033[32m{word[4][0]}\033[0m'
    elif len(word[4]) == 2:
        word_string += f'\033[33m{word[4][0]}\033[0m'
    else:
        word_string += word[4][0]

    # print(word_string)
    return word_string

#USE THIS FUNCTION IN GAME.PY TO COMPARE EACH GUESS TO THE SECRET WORD
def compare(secret, guess):
    coded_guess = is_present(secret, guess)
    interpreted_guess = interpret_word(coded_guess)
    return interpreted_guess
