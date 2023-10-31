# wordie

Writing random notes while this is fresh on my mind. Sort this out later...

main.py is the entry point. 
    it clears the terminal
    it welcomes the user
    it gives the user the option to hear the instructions. if they want, it calls the function that prints instructions (features -> instructions.py)
    it asks user if they are ready. if they respond yes, it calls the game() function (features -> game.py)

game.py
    takes a word as a parameter (main.py passes it a random word from scraper -> past_words -> get_random_word()) 
    clears the terminal
    sets a variable to track turns
    sets up an array of empty strings that will track user guesses
    runs a while loop that, while the turn count is less than 5, prints all the user's choices up to that point (skips this for first turn)
        then takes user's guess
        validates the guess
        compares the guess against the secret_word
            ends the game and displays winning message if the guess is correct
        passes the secret word and guess into the compare() function (features -> compare)
            At this point the secret word and guess are lists with one letter for each item
            compare() first codes the guess by adding y to each item that is a letter that is present in the secret word
            then, it compares each letter again and adds a g to each item where the first letter is the same as the letter at that position in the secret word.
            After the guess word has been coded, the compare function converts the coded word into a string that will print letters that are correct and in the right position in green and the letters that are correct but in the wrong position yellow.
        Next, game adds the newly interpreted word to the list of guesses at the position corresponding to the current turn
        The turn tracking variable is increased by one. 

        The final lines of game() check if turn == 5. If so, the user has used all their turns and has lost. A game over message is printed along with the secret_word.

Where are we getting the words??
    in scraper -> past_words.py we have a function that uses BeautifulSoup to collect words from https://www.rockpapershotgun.com/wordle-past-answers/
        in order to do this, the function finds the <ul> where the words are displayed and creates a list of the text content of each <li> (called words)
        it uses the 'random' library to return a random word from the hundreds of words in the list.