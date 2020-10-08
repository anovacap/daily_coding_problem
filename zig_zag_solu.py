#!/usr/bin/python
# Strings 2.2 solution
# zigzag has 2 loops - a list of spaces the length of the given word is created as line. The while loop puts the letters in the 
# right position in line by moving i spaces + 1. spaces uses get_spaces which either return
# k = the pivot point where zig turns to zag - word = string to alter - 

def get_spaces(row, desc, k):
    # row is the current iteration to print starting at 0 -  desc is true or false - k is the last row to print 
    max_spaces = (k - 1) * 2 - 1 # the formula for the max number of spaces 
    if desc: # starts with max numer of spaces and get smaller 
        spaces = max_spaces - row * 2
        print("spaces in desc = ", spaces)
    else: #
        spaces = max_spaces - (k - 1 - row) * 2
        print("spaces not in desc", spaces)
    return spaces


def is_descending(index, k):
    # Check whether the index is more or less than halfway through its oscillation back to the starting point.
    print("index = ", index)
    print('k = ', k)
    print('index after change =', index % (2 * (k -1)) < k -1)
    return index % (2 * (k - 1)) < k - 1 # returns True or False depending on if index % (change in k) is less than k - 1

def zigzag(word, k):

    n = len(word)

    for row in range(k):
        i = row # duplicate row as i to control the while loop with i 
        line = [' ' for _ in range(n)] # line is a list of spaces n long - n is an integer the length of word

        while i < n:
            line[i] = word[i] # replaces the space in the line list with the letter in word 
            desc = is_descending(i, k) # desc is the return of is_descending which checks whether the index is more or less than halfway through its oscilation back the the starting point
            spaces = get_spaces(row, desc, k) # get_spaces returns
            i += spaces + 1

        print(''.join(line))

if __name__ == "__main__":
    w = 'thisisanotherzigzag'
    t = 5
    zigzag(w, t)
