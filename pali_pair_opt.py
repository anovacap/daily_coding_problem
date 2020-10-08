#!/usr/bin/python
# Strings 2.2 giving a list of words, find all pairs of unique indices such that the concatination of two
# words is a palindrome
# uses a dictionary

def is_palindrome(word):
    return word == word[::-1]

def palindrome_pairs(words):
    d = {}
    for i, word in enumerate(words):
        d[word] = i

    result = []

    for i, word in enumerate(words):
        for char_i in range(len(word)):
            prefix, suffix = word[:char_i], word[char_i:]
            reversed_prefix = prefix[::-1]
            reversed_suffix = suffix[::-1]

            if (is_palindrome(suffix) and reversed_prefix in d):
                if i != d[reversed_prefix]:
                    result.append((i, d[reversed_prefix]))
            if (is_palindrome(prefix) and  reversed_suffix in d):
                if i != d[reversed_suffix]:
                    result.append((d[reversed_suffix], i))
    return result

if __name__ == "__main__":
    x = ['code', 'edoc', 'da', 'd']
    p = palindrome_pairs(x)
    print(p)