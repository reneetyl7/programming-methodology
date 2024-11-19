"""
File: hangman.py
Name: Renee
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random

# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    word = str(random_word())
    guess_word = []
    wrong_guesses = 0

    while wrong_guesses < N_TURNS:
        display_word = word_band(word, guess_word)
        print("The word looks like: " + display_word)
        print("You have " + str(N_TURNS - wrong_guesses) + " wrong guesses left.")

        guess = digit_c()  # catch the word
        if guess in guess_word:
            print("You've already guessed that letter.")
            if guess not in word:
                wrong_guesses += 1
        elif guess in word:
            print("You are correct!")
            guess_word.append(guess)
        else:
            print("There is no " + guess + "'s in the word.")
            wrong_guesses += 1
            guess_word.append(guess)
            # Preventing repeated guesses
        if all_letters_guessed(word, guess_word):
            print("You win!!")
            print("The answer is: " + word)
            return
    print("You are completely hung :(")
    print("Thw answer is: " + word)


def word_band(word, guess_word):
    """
    Creates a string representation of the word with guessed letters revealed.

    Param word (str): The secret word to be guessed.
    Param guessed_letters (list): A list of letters that have been guessed.

    Returns:
    str: A string where guessed letters are revealed and others are replaced by '-'.
    """
    hidden = ""
    for cha in word:
        if cha in guess_word:
            hidden += cha
        else:
            hidden += "-"
    return hidden


def all_letters_guessed(word, guess_word):
    """
    Checks if all letters in the word have been guessed.

    Param word (str): The secret word to be guessed.
    Param guessed_letters (list): A list of letters that have been guessed.

    Returns:
    bool: True if all letters in the word have been guessed, False otherwise.
    """
    for letter in word:
        if letter not in guess_word:
            return False
    return True


def digit_c():
    """
    Prompts the user for a single letter guess and validates the input.

    No parameters.

    Returns:
    str: A single uppercase letter that the user has guessed.
    """
    while True:
        guess = input("Your guess: ").upper()
        if not guess.isalpha():
            print("Illegal format.")
        elif len(str(guess)) > 1:
            print("Illegal format.")
        else:
            return guess


def random_word():
    """
    Selects a random word from a predefined list of words.

    No parameters.

    Returns:
    str: A randomly selected word from the list.
    """
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
