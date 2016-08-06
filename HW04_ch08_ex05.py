# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 5 for the task.
# Please do provide function calls that test/demonstrate your
# function.

def rotate_letter(letter, n):
    """Provide case for upper and lower cases"""
    if letter.isupper():
        start = ord('A') #65
    elif letter.islower():
        start = ord('a') #97

    c = ord(letter) - start     #normalize original letter
    new = (c + n)%26 + start    #add integer to normalized value, %26 to ensure 
                                #it doesn't go over or under alphabet scale, 
                                #convert back to assigned letter number
    
    return chr(new) #return newly converted letter

def rotate_word(word, n):
    newword = ''    #setting up blank variable to put letters into
    for letter in word:     #take each letter in word and run it through rotate_letter
        newword = newword+rotate_letter(letter, n) #add in each new letter one at a time
    return newword
    
if __name__ == '__main__':
    print(rotate_word('Python', 40))
