#!/usr/bin/env python3

# Created by: Andrew Ten-Den
# Created on: April 2022
# This program lets the user guess a number between 0 and 9

import random


def main():
    # this function lets the user guess a number between 0 and 9

    guess_variable = random.randint(0, 9)  # a number between 0 and 9
    guess_counter = 1
    number_guessed = 0
    # input

    while number_guessed != guess_variable:
        number_guessed = input("Enter a number between 0 and 9: ")
        try:
            number_guessed_int = int(number_guessed)

            # process & output

            if number_guessed_int == guess_variable:
                print("\nYou guessed correct after {} guesses!".format(guess_counter))
                break
            elif number_guessed_int < 0 or number_guessed_int > 9:
                print("\nUndefined\n")
                guess_counter = guess_counter + 1
            else:
                print("\nSorry, you guessed wrong. Try again.\n")
                guess_counter = guess_counter + 1

        except Exception:
            print("\nThis was not an integer\n")
            guess_counter = guess_counter + 1


if __name__ == "__main__":
    main()
