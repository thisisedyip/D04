#!/usr/bin/env python
# HW04_ch07_ex02

# The built-in function eval takes a string and evaluates it using the Python
# interpreter.
# For example:

#     >>> eval('1 + 2 * 3')
#     7
#     >>> import math
#     >>> eval('math.sqrt(5)')
#     2.2360679774997898
#     >>> eval('type(math.pi)')
#     <type 'float'>

# Write a function called eval_loop that iteratively prompts the user, takes
# the resulting input and evaluates it using eval, and prints the result.

# It should continue until the user enters 'done', and then return the value of
# the last expression it evaluated.

###############################################################################
# Imports
import math

# Body
def eval_loop():
    user = ''
    newvalue = 0
    while True:
        try:
            user = str(input("Please provide an eval input: "))
            newvalue = eval(user)
            print(newvalue)
        except:
            if user != 'done':
                print("You've provided an inappropriate eval input.")
        if user == 'done':
                break
    print("You're done!  Your most recent eval was: " + str(newvalue))

###############################################################################
def main():
    eval_loop()

if __name__ == '__main__':
    main()
