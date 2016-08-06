#!/usr/bin/env python
# HW04_ch08_ex00
# See 8.7

# The following program counts the number of times the letter 'a' appears in a
# string:

#     word = 'banana'
#     count = 0
#     for letter in word:
#         if letter == 'a':
#             count = count + 1
#     print(count)

# Encapsulate this code in a function named "count", and generalize it so that
# it accepts the string and the letter as arguments.

###############################################################################
# Imports


# Body
def count():
    word = str(input("Gimme a word: "))
    userletter = str(input("Gimme a letter: "))
    count = 0
    for letter in word:
        if letter == userletter:
            count = count + 1
    print("BOOM!  The number of " + str(userletter)+"'s" + " in "+ str(word) + " is " + str(count))
    

###############################################################################
def main():

    # Remove print("Hello World!") and add several functions calls to count()
    # below, passing various strings and letters
    count()


if __name__ == '__main__':
    main()
