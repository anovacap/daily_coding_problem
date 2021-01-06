#!/usr/bin/python
# Daily Coding Problem - Tries: 8.1 Implement autocomplete system

class Trie:
	def __init__(self): 
		self.ends_here = '#'
		self.trie = {}

	def __repr__(self): # allows print
		return repr(self.trie)

	def _insert(self, *words):
		trie = {}
		for word in words:
			temp_dict = trie
			for char in word:
				temp_dict = temp_dict.setdefault(char, {})
			temp_dict[self.ends_here] = self.ends_here
		return trie

	def _find(self, word):
		sub_trie = self.trie

		for char in word:
			if char in sub_trie:
				sub_trie = sub_trie[char]
			else:
				return False
		else:
			if self.ends_here in sub_trie:
				return True
			else:
				return False

	def add_word(self, word):
		if self._find(word):
			print("Word exists")
			return self.trie
		temp_trie = self.trie
		for char in word:
			if char in temp_trie:
				temp_trie = temp_trie[char]
			else:
				temp_trie = temp_trie.setdefault(char, {})
		temp_trie[self.ends_here] =self.ends_here
		return temp_trie

if __name__ == "__main__":
	tr = Trie()
	tr.add_word('bear')
	tr.add_word('bingo')
	tr.add_word('cat')
	tr.add_word('coat')
	tr.add_word('dog')
	print(tr)
	print(tr._find("dog"))
	print(tr._find("bear"))
	print(tr._find("bingo"))

