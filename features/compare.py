#WORDS FOR TESTING...
word1 = ['a', 'b', 'c', 'd', 'e']
word2 = ['a', 'b', 'c', 'd', 'e']

#ADD A Y TO THE END OF EACH LETTER OF WORD2 THAT IS IN WORD1
def is_present(word1, word2):
    if word2[0] in word1:
        word2[0] = word2[0] + 'y'
    if word2[1] in word1:
        word2[1] = word2[1] + 'y'
    if word2[2] in word1:
        word2[2] = word2[2] + 'y'
    if word2[3] in word1:
        word2[3] = word2[3] + 'y'
    if word2[4] in word1:
        word2[4] = word2[4] + 'y'

    if len(word2[0]) > 1:
        if word2[0][0] == word1[0][0]:
            word2[0] = word2[0] + 'g'
    if len(word2[1]) > 1:
        if word2[1][0] == word1[1][0]:
            word2[1] = word2[1] + 'g'
    if len(word2[2]) > 1:
        if word2[2][0] == word1[2][0]:
            word2[2] = word2[2] + 'g'
    if len(word2[3]) > 1:
        if word2[3][0] == word1[3][0]:
            word2[3] = word2[3] + 'g'
    if len(word2[4]) > 1:
        if word2[4][0] == word1[4][0]:
            word2[4] = word2[4] + 'g'
    return word2

# def compare(word1, word2):

is_present(word1, word2)

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
    # print(coded_guess)
    interpreted_guess = interpret_word(coded_guess)
    # print(interpreted_guess)
    return interpreted_guess
