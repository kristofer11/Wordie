# Wordie

Welcome to Wordie, a command-line version of the popular game Wordle. This game challenges you to guess a secret word by making educated guesses and using the feedback provided to refine your subsequent guesses.

## How to Play

When you start the game, you'll be welcomed and given the option to hear the instructions. If you choose to hear them, the game will call a function that prints the instructions.

Once you indicate that you're ready to play, the game begins. The game function takes a random word as a parameter and sets up an array to track your guesses. You have five turns to guess the secret word.

In each turn, the game prints your previous guesses and prompts you for your next guess. It then validates your guess and compares it against the secret word. If your guess is correct, the game ends and a winning message is displayed.

If your guess is incorrect, the game passes your guess and the secret word to the compare function. This function codes your guess by marking each letter that is present in the secret word and each letter that is in the correct position. It then converts this coded guess into a string that displays correct letters in green and misplaced letters in yellow.

After interpreting your guess, the game adds it to the list of guesses and increments the turn count. If you've used all your turns without guessing the secret word, the game ends and a game over message is displayed along with the secret word.

## Word Source

The words for the game are scraped from [Rock Paper Shotgun's list of past Wordle answers](https://www.rockpapershotgun.com/wordle-past-answers/) using BeautifulSoup. The scraper function finds the list of words on the page and returns a random word from the list.

## Getting Started

To play Wordie, you'll need to have Python installed on your computer. Once you've installed Python, you can download the Wordie code and run `main.py` to start the game. Enjoy!

# Game Logic

The game logic is primarily contained within `game.py`. Here's a step-by-step breakdown:

1. **Game Initialization**: The `game()` function is called with a random word as a parameter, which is fetched from `scraper -> past_words -> get_random_word()`. The terminal is cleared, a variable to track turns is set, and an array of empty strings is initialized to track user guesses.

2. **Game Loop**: The game runs a loop that continues until the turn count reaches 5. In each turn, the game prints all the user's choices up to that point (except for the first turn), then prompts the user for their guess.

3. **Guess Validation**: The user's guess is validated. If it's not a valid guess, the game prompts the user to guess again.

4. **Guess Comparison**: The guess is compared against the secret word. If the guess is correct, the game ends and a winning message is displayed.

5. **Guess Interpretation**: If the guess is incorrect, the secret word and guess are passed to the `compare()` function in `features -> compare`. This function codes the guess by marking each letter that is present in the secret word and each letter that is in the correct position. It then converts this coded guess into a string that displays correct letters in green and misplaced letters in yellow.

6. **Turn End**: The interpreted guess is added to the list of guesses at the position corresponding to the current turn, and the turn count is incremented.

7. **Game Over**: If the turn count reaches 5 and the user hasn't guessed the secret word, the game ends and a game over message is displayed along with the secret word.

This logic ensures that the game provides the right amount of challenge and feedback to make it engaging and fun.

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