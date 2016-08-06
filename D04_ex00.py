#!/usr/bin/env python
# D04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports
import random
from random import randint

# Body

def randomguess():
    guess = ''
    actual = random.randint(1,25)
    countdown = 5

    while countdown > 0:
            try:
                    guess = float(input("Guess a number: "))
                    countdown -= 1
                    if guess > actual and 1<=guess<=25:
                            print("Your guess is too high")
                    if guess > 25 or guess < 1:
                            print("Remember that guesses must be between 1 and 25")
                    if guess < actual and 1<=guess<=25:
                            print("Your guess is too low")
                    if guess == actual:
                            print("Your guess is correct!")
            except:
                    print("You have not inputted a number")
                    countdown -= 1


################################################################################
def main():


    randomguess()
    

if __name__ == '__main__':
    main()
