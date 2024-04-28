# Python Hangman Game

## Description
The Python Hangman Game is an interactive command-line application where players guess letters to form a word before their lives run out. This game was developed to demonstrate proficiency in Python fundamentals including loops, functions, and handling user inputs.

## Features
- **Interactive Gameplay**: Play directly from your command line.
- **Visual Feedback**: Provides ASCII art visualizations of the hangman as the player loses lives.
- **Dynamic Word Generation**: Words are randomly selected from a pre-defined list each game, ensuring varied gameplay.

## Technologies Used
- Python
- Random module for word selection
- Custom modules: `hangman_words` for the word list, `hangman_art` for ASCII art

## Getting Started
To run the Python Hangman Game on your local machine, follow these steps:

1. **Clone the repository**
   ```bash
   git clone https://github.com/SaadNasir92/Python-Hangman-Game
2. **Navigate to the repository folder**
    ```bash
    cd Hangman
3. **Run the game**
    ```bash
    python main.py

## Gameplay Instructions
- Upon launch, you will be prompted to enter your username and then start guessing letters.
- You can guess one letter at a time or attempt to guess the full word.
- Each incorrect guess will result in a loss of one life and the hangman drawing will progress.
- The game continues until you successfully guess the word or run out of lives.

## Code Example
```python
def hangman():
    chosen_word = random.choice(hangman_words.word_list)
    guessed_letters = []
    won = False
    lives = 6

    while not won and lives > 0:
        display = ""
        for letter in chosen_word:
            if letter in guessed_letters:
                display += letter
            else:
                display += "_"
        print(f"\nYou have {lives} lives remaining!\n")
        print("Already Guessed:")
        print(guessed_letters)
        print(hangman_art.stages[lives])
        print(display)
```
## Lessons Learned
Developing the Python Hangman Game provided a comprehensive practice in:

- Utilizing loops to manage game states.
- Implementing functions to organize logic and promote code reuse.
- Managing user input and providing feedback based on game logic.

## Future Improvements
- Graphical User Interface (GUI): Implementing a simple GUI to improve user experience.
- Multiplayer Functionality: Adding online multiplayer capabilities to play with friends.
- Expanded Vocabulary: Enlarging the word database to increase difficulty and replay value.
