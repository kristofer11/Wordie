import os
# from words import request_word

def game(word):
    os.system('clear')
    turn = 0
    word = word
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

        guess = input('Enter your guess: ')
        while True:
            if len(guess) == 5:
                break            
            guess = input('Enter an english word of exactly 5 letters. No numbers or special characters...')

        guesses[turn] = guess
        current_guess = [*guess]
        print(current_guess)

        turn += 1
        # if turn < 5:
        #     os.system('clear')
    print(f'That was guess number {turn}, the word was {secret_word}!')