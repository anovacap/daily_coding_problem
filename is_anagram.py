#!/usr/bin/python
# Strings ex 2.1
# given a word and a string find all instances of the word or reverse word in the string
# Counter() evaluates if string 1 == to string 2 - ex 'hello' == 'ollhe'  True
from collections import Counter
def is_anagram(s1, s2):
	return Counter(s1) == Counter(s2)

def anagram_indices(word, s):
	result = []
	for i in range(len(s) - len(word) + 1): # len(s) = 6 len(word) = 2 - 6 - 2 + 1 = 5
		print("len s = ", len(s))
		print("len word = ", len(word))
		print("len(s) - len(word) = ", len(s) - len(word) + 1)
		print("x") 
		window = s[i:i + len(word)] # creates a window that moves with i
		if is_anagram(window, word):
			result.append(i)
	return result

if __name__ == "__main__":
	q = anagram_indices('ab', 'abxaba')
	print(q)
