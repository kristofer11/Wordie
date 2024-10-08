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

To play Wordie online, you can simply fork my [Wordie Repl](https://replit.com/@klhvattum/Wordie?v=1#main.py) and run it in the terminal with "python main.py"

To play on your computer, you'll need to have Python installed. Once you've installed Python, you can follow these steps:

1. Clone the Wordie repository to your local machine.
2. Navigate to the project directory using the terminal.
3. Create a virtual environment by running `python3 -m venv venv`.
4. Activate the virtual environment: On Windows, run `venv\Scripts\activate`, and on macOS/Linux, run `source venv/bin/activate`.
5. Install dependencies from `requirements.txt` by running `pip install -r requirements.txt`.
6. Run the game by executing `python main.py` in the terminal.

Enjoy playing Wordie!

![Wordie Screenshot](assets/wordie_screenshot.png)

# Game Logic

The game logic is primarily contained within `game.py`. Here's a step-by-step breakdown:

1. **Game Initialization**: The `game()` function is called with a random word as a parameter, which is fetched from `scraper.past_words.get_random_word()`. The terminal is cleared, a variable to track turns is set, and an array of empty strings is initialized to track user guesses.

2. **Game Loop**: The game runs a loop that continues until the turn count reaches 5. In each turn, the game prints all the user's choices up to that point (except for the first turn), then prompts the user for their guess.

3. **Guess Validation**: The user's guess is validated. If it's not a valid guess, the game prompts the user to guess again.

4. **Guess Comparison**: The guess is compared against the secret word. If the guess is correct, the game ends and a winning message is displayed.

5. **Guess Interpretation**: If the guess is incorrect, the secret word and guess are passed to the `compare()` function in `features.compare`. This function codes the guess by marking each letter that is present in the secret word and each letter that is in the correct position. It then converts this coded guess into a string that displays correct letters in green and misplaced letters in yellow.

6. **Turn End**: The interpreted guess is added to the list of guesses at the position corresponding to the current turn, and the turn count is incremented.

7. **Game Over**: If the turn count reaches 5 and the user hasn't guessed the secret word, the game ends and a game over message is displayed along with the secret word.

This logic ensures that the game provides the right amount of challenge and feedback to make it engaging and fun.

![Wordie Screenshot](assets/game_play_screenshot.png)
