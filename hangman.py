import random
from hangman_art import *
from hangman_words import *


def play():
    word = random.choice(word_list).lower()
    guessed_word = ""
    score = 6
    while score > 0:
        print(f"\nScore : {score}")
        print(stages[score])
        print(f"Word: {" ".join(letter if letter in guessed_word else "_" for letter in word)}")
        guess = input("Guess a letter: ").lower()
        if guess in guessed_word:
            print("You already guessed that letter. Try again.")
        elif not len(guess) == 1:
            print("You can enter only one character!")
            score -= 1
        elif not guess in word:
            print("Incorrect guess. You lose a try.")
            score -= 1
        else:
            print("Good guess!")
        guessed_word += guess
        if all(char in guessed_word for char in word):
            print(f"\nCongratulations! You guessed the word: {word}")
            print(logo_win)
            break
    else:
        print(stages[score])
        print(f"Sorry, you've run out of tries. The word was: {word}")


def start(is_started):
    while True:
        if not is_started:
            yes_no = input("Are you ready to play game? [y/n]: ").lower()
        else:
            yes_no = input("Do you want to play again? [y/n]: ").lower()
        if yes_no == "y" or yes_no == "n": return True if yes_no == "y" else False


if __name__ == "__main__":
    print(logo)
    is_start = False
    while start(is_start):
        play()
        is_start = True
    print("See you again!")