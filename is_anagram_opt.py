#!/usr/bin/python
# Strings 2.1.opt O(s)
# defaultdict builds a dictionary (in this case) where the key is the char in the string and the val is an int.

from collections import defaultdict

def del_if_zero(dict, char): #
	if dict[char] == 0:
		del dict[char]

def anagram_indices(word, s):
	result = []

	freq = defaultdict(int)
	for char in word: 
		freq[char] += 1
		#print("freq = ", freq) # freq = {'a':1, 'b':1}

	for char in s[:len(word)]: # for char in s[:2]
		freq[char] -= 1
		del_if_zero(freq, char)
		#print('freq after del_if_zero', freq) # freq = {}

	if not freq: # if the 2 above for loops produce nothing then the first characters of the string are ana anagram
				# The first index (0) is appended to result
		result.append(0)

	for i in range(len(word), len(s)): # for i in range(2, 6) - does the same as above but starts after len(word)
		start_char, end_char = s[i - len(word)], s[i] # start_char is 'a' (2 - 2) end_char is 'x' (word window vars)
		print('i = ', i)
		#print('len(word = ', len(word))
		print('start_char = ', start_char)
		print('end_char = ', end_char)
		freq[start_char] +=  1
		print('freq 2 build up', freq)
		del_if_zero(freq, start_char)
		print('freq after del_if', freq)

		freq[end_char] -= 1
		del_if_zero(freq, end_char)

		if not freq:
			beginning_index = i - len(word) + 1
			result.append(beginning_index)
	print(result)
	return result

if __name__ == "__main__":
	g = anagram_indices('ab', 'abxaba')
	print(g)

