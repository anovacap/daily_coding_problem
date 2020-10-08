#!/usr/bin/python
# String 2.3 given a string and an integer, zig_zag the word the integer patern
# my version - not good 
def zig_zag(word, i):
    new_string = ''
    new_i = (i - 1) * 2 - 1
    space = ' '
    front_string = 0
    mid_string = (i - 1) * 2
    end_string = len(word) - 1
    #for x in range(i):
    for y in range(i):
        if y == 0:
            new_string = word[front_string] + space * new_i + word[mid_string] + space * new_i + word[end_string]
            print(new_string)
        elif y == i - 1:
            new_string = space * y + word[front_string + y] + space * (y + 1) + word[end_string - y] + space*y
            print(new_string)
        else:
            new_string = space * y + word[front_string + y] + space * (new_i - (2*y)) + word[mid_string - y] + space*y + word[mid_string + y] + space * (new_i - (2*y)) + word[end_string - y] + space*y
            print(new_string)
    new_string = ''
if __name__ == "__main__":
    word = "thisisazigzag"
    i = 3
    zig_zag(word, i)
