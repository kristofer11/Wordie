import os
from features.compare import compare
# from words import request_word
# from scraper.past_words import get_random_word

def game(word):
    os.system('clear')
    turn = 0
    word = word
    print('gametime')
    secret_word = [*word()]
    print(secret_word)
    guesses = ['', '', '', '', '']

    while turn < 5:
        if guesses[4]:
            print('GUESSES:')
            print(f'1. {guesses[0]}')   
            print(f'2. {guesses[1]}')   
            print(f'3. {guesses[2]}')   
            print(f'4. {guesses[3]}')   
            print(f'5. {guesses[4]}')   
        elif guesses[3]:
            print('GUESSES:')
            print(f'1. {guesses[0]}')   
            print(f'2. {guesses[1]}')   
            print(f'3. {guesses[2]}')   
            print(f'4. {guesses[3]}')   
        elif guesses[2]:
            print('GUESSES:')
            print(f'1. {guesses[0]}')   
            print(f'2. {guesses[1]}')   
            print(f'3. {guesses[2]}')  
        elif guesses[1]:
            print('GUESSES:')
            print(f'1. {guesses[0]}')   
            print(f'2. {guesses[1]}')      
        elif guesses[0]:
            print('GUESSES:')
            print(f'1. {guesses[0]}')

        #GET USER GUESS
        guess = input('Enter your guess: ').upper()

        #VALUDATE GUESS
        while True:
            if len(guess) == 5:
                break            
            guess = input('Enter an english word of exactly 5 letters. No numbers or special characters...').upper()

        #CHECK GUESS AGAINST SECRET WORD
        guess_list = [*guess]
        interpreted_guess = compare(secret_word, guess_list)
    
        guesses[turn] = interpreted_guess
        # current_guess = [*guess]
        # print(current_guess)

        turn += 1
        if turn < 5:
            os.system('clear')
    print(f'That was guess number {turn}, the word was {secret_word}!')

game('SWIFT')