#!/usr/bin/env python
# HW04_ch08_ex04

# The following functions are all intended to check whether a string contains
# any lowercase letters, but at least some of them are wrong. For each
# function, describe (is the docstring) what the function actually does.
# You can assume that the parameter is a string.

# Do not merely paste the output as a counterexample into the documentation
# string, explain what is wrong.

###############################################################################
# Body



def any_lowercase1(s):
    """ Stops scanning after first letter in s
    """ 
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    """ Only scans character 'c' instead of the variable c in s
    """ 
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    """ Only returns last letter it scans for c in s
    """
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):
    """ Nothing is wrong
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


def any_lowercase5(s):
    """ Returns false anytime a capital letter is present even if lower cases are present 
    """
    for c in s:
        if not c.islower():
            return False
    return True

###############################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong,
    # call that function with a string for which the function returns
    # incorrectly.
    # ex.: any_lowercase_("thisstringmessesupthefunction")
any_lowercase1("Anything")
any_lowercase2("ANYTHING")
any_lowercase3("anythinG")
any_lowercase5("anythinG")


if __name__ == '__main__':
    main()
