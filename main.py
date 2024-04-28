import random
import hangman_words
import hangman_art

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


def welcome(life):
    user_name = input("\nPlease type in your username: ")
    print(f'\nHeya {user_name}! Welcome to my novice Hangman game that you could play on your phone in 2022.\n')
    print("-The rules are simple: You are given a word, and you have to guess the letters.")
    print("-If you think you know the word, you can guess the word itself.")
    print(f"-For each incorrect guess of word or letter, you lose a life. You have {life} lives.")
    print(f"\nGood luck {user_name}!\n")


def play_again():
    rerun = (input("\nType 'y' to play again or 'n' to exit: ")).lower()
    if rerun == "y":
        hangman()
    else:
        print("\nThanks for playing, have a great day/night!")
        exit()


print(hangman_art.logo)
welcome(6)


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

        guess = input("\nPlease input a letter or word as your guess:\n").lower()
        if not guess.isalpha():
            print("You didn't enter a letter or word, you lose a life.\n")
            lives -= 1
        elif guess in guessed_letters:
            print("You have already guessed this letter. Try again.\n")
        elif len(guess) == len(chosen_word):
            if guess == chosen_word:
                won = True
            else:
                print("\nIncorrect, you lose a life.\n")
                guessed_letters.append(guess)
                lives -= 1
        elif len(guess) != 1:
            print("\nPlease guess a letter or an entire word.\n")
        elif guess in chosen_word:
            print("\nThat was a correct guess!\n")
            guessed_letters.append(guess)
            if set(guessed_letters) == set(chosen_word):
                won = True
        else:
            print("\nIncorrect, you lose a life.\n")
            lives -= 1
            guessed_letters.append(guess)

    if won:
        print(f"\nYou guessed the word with {lives} lives remaining, you win!")
        play_again()

    else:
        print(hangman_art.stages[lives])
        print(f'\nThe correct word was {chosen_word}. You ran out of lives, you lose!')
        play_again()

hangman()
