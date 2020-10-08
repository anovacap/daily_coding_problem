#!/usr/bin/python
# Strings 2.4 smallest rotated string
# determine the lexicographically smallest string that can be created after an unlimited number of moves

def bubble_swap(string, i, j):
    string = list(string)
    # rotate so that i is at the beginning.
    while i > 0:
        string = string[1:] + string[:1]
        i -= 1
    
    # move the first two letters to the end in reversed order
    string = string[:1] + string[2:] + string[1:2]
    string = string[1:] + string[:1]

    # rotate back to the initial position.
    while len(string) > j + 1:
        string = string[1:] + string[:1]
        j += 1
    
    return ''.join(string)

if __name__ == "__main__":
    st = 'daily'
    k = 1
    l = bubble_swap(st, k, k)
    print(l)
