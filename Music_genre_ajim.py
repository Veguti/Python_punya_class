#!/usr/bin/env python

import random

def main():
    """Start a musical genre guessing game."""
    print("Guess the genre!")

    genre = ["pop","rock","jazz","r&b","blues","reggae","rap","classical","metal"]

    x = random.choice(genre)
    guess = None

    while x != guess:

        guess = str(input("What genre am I listening to? "))
        
        if x == guess:
            print("You guessed {}. Congratulations you got it right!".format(guess))
            break
        else:
            print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))
            print("Hint: The correct answer has {} letters.".format(len(x)))

main()