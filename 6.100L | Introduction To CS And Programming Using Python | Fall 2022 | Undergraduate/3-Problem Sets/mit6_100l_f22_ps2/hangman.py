# Problem Set 2, hangman.py
# Name: Steven Pan
# Date: Sat 26 Sep 2026, Tue 29 Sep 2026

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()
secret_word = choose_word(wordlist)


def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed, False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been guessed so far

    returns: string, comprised of letters and asterisks (*) that represents which letters in secret_word have not been
      guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    progress = ''
    for letter in secret_word:
        if letter in letters_guessed:
            progress += letter
        else:
            progress += '*'
    return progress


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been guessed so far

    returns: string, comprised of letters that represents which letters have not yet been guessed. The letters should be
      returned in alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    available_letters = ''
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            available_letters += letter
    return available_letters


def choose_revealed_letter(secret_word, available_letters):
    """
    secret_word: string, the lowercase word the user is guessing
    get_available_letters: function, comprised of letters that have not been guessed so far

    returns: string, the letter that picked randomly in secret_word and get_available_letters
    """
    choose_from = ''
    for letter in secret_word:
        if letter in available_letters:
            choose_from += letter
    new = random.randint(0, len(choose_from) - 1)
    revealed_letter = choose_from[new]
    return revealed_letter


def number_of_unique_letter(secret_word):
    """
    secret_word: string, the lowercase word the user is guessing

    returns: int, the number of unique letters in secret_word
    """
    unique_letters = 0
    letters = ''
    for letter in secret_word:
        if letter not in letters:
            unique_letters += 1
            letters += letter
    return unique_letters


def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many letters the secret_word contains and how many guesses they
      start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses they have left and the letters that the user
      has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make sure that the user puts in a single letter (or help
      character '!' for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess, while if the user inputs an incorrect
      vowel (a, e, i, o, u), then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess about whether their guess appears in the computer's
      word.

    * After each guess, you should display to the user the partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the letters missing from the word at the cost
      of 3 guesses. If the user does not have 3 guesses remaining, print a warning message. Otherwise, add this letter
      to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # Game setup
    print('Welcome to Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')

    # User-computer interaction
    guesses_remaining = 10
    letters_guessed = ''
    while True:
        print('--------------')
        print('You have', guesses_remaining, 'guesses left.')
        print('Available Letters:', get_available_letters(letters_guessed))

        letter_guessed = input('Please guess a letter: ').lower()

        if letter_guessed.isalpha() and len(letter_guessed) == 1:
            if letter_guessed in secret_word:
                guesses_remaining -= 0

                if letter_guessed not in letters_guessed:
                    letters_guessed += letter_guessed
                    print('Good guess:', get_word_progress(secret_word, letters_guessed))
                else:
                    letters_guessed += letter_guessed
                    print("Oops! You've already guessed that letter:", get_word_progress(secret_word, letters_guessed))

            else:
                if letter_guessed in ('a', 'e', 'i', 'o', 'u'):
                    guesses_remaining -= 2
                else:
                    guesses_remaining -= 1

                letters_guessed += letter_guessed
                print('Oops! That letter is not in my word:', get_word_progress(secret_word, letters_guessed))

        elif letter_guessed == '!' and with_help:
            if guesses_remaining >= 3:
                guesses_remaining -= 3

                revealed_letter = choose_revealed_letter(secret_word, get_available_letters(letters_guessed))
                print('Letter revealed:', revealed_letter)

                letters_guessed += revealed_letter
                print(get_word_progress(secret_word, letters_guessed))

            else:
                print('Oops! Not enough guesses left:', get_word_progress(secret_word, letters_guessed))

        else:
            print('Oops! That is not a valid letter. Please input a letter from the alphabet:', get_word_progress(secret_word, letters_guessed))

        if has_player_won(secret_word, letters_guessed):
            print('--------------')
            print('Congratulations, you won!')

            total_score = guesses_remaining + 4*number_of_unique_letter(secret_word) + 3*len(secret_word)
            print('Your total score for this game is:', total_score)

            break

        elif guesses_remaining <= 0:
            print('--------------')
            print('Sorry, you ran out of guesses. The word was', secret_word)

            break

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

# Run this block only when this file is executed directly
if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    with_help = True
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass
