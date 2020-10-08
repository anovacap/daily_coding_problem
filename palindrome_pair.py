#!/usr/bin/python
# Strings 2.2 palindome_pair indices O(n*n)

def is_palindrome(word):
    return word == word[::-1]

def palindrome_pair(words):
    result = []

    for i, word1 in enumerate(words):
        for j, word2 in enumerate(words):
            if i == j:
                continue
            if is_palindrome(word1 + word2):
                result.append((i , j))
    return result

if __name__ == "__main__":
    x = ['code', 'edoc', 'da', 'd']
    p = palindrome_pair(x)
    print(p)
