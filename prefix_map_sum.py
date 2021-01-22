#!/usr/bin/python
# Daily Coding Problem - Tries: 8.2 Implement a Prefix Map Sum class
# methods = insert(key: str, value: int) - Sets a given key's value in the 
# map. If the key already exists, overwirte the value.
# methos = sum(grefix: str) - Return the sum of all values of keys that begin
# with the given prefix.

from collections import defaultdict

class PrefixMapSum:
    def __init__(self):
        self.map = {}
    
    def insert(self, key: str, value: int):
        self.map[key] = value
    
    def sum(self, prefix):
        return sum(value for key, value in self.map.items() if key.startswith(prefix))

class PrefixMapSum_two:
    def __init__(self):
        self.map = defaultdict(int)
        self.words = set()
    
    def insert(self, key: str, value: int):
        # if the key already exists, increment prefix totals
        # by the difference of old and new values
        if key in self.words:
            value -= self.map[key]
        self.words.add(key)

        for i in range(1, len(key) + 1):
            self.map[key[:i]] += value
    def sum(self, prefix):
        return self.map[prefix]

class TrieNode:
    def __init__(self):
        self.letters = {}
        self.total = 0

class Prefix_map_complex:
    def __init__(self):
        self._trie = TrieNode()
        self.map = {}
        
    def insert(self, key, value):
        # if key exists, increment prefix totals by difference of old and new vals
        value -= self.map.get(key, 0)
        self.map[key] = value
        trie = self._trie
        for char in key:
            if char not in trie.letters:
                trie.letters[char] = TrieNode()
            trie = trie.letters[char]
            trie.total += value
            print("Char = {}, total = {}".format(char, trie.total)) 
    def sum(self, prefix):
        d = self._trie
        for char in prefix:
            if char in d.letters:
                d = d.letters[char]
            else:
                return "H"
        return d.total

if __name__ == "__main__":
    prefmapsum = PrefixMapSum()
    prefmapsum.insert("column", 3)
    prefmapsum.insert("hello", 5)
    prefmapsum.insert("columns", 6)
    prefmapsum.insert("hellos", 22)
    print(prefmapsum.sum("col"))
    print(prefmapsum.sum('hel'))
    prema2 = PrefixMapSum_two()
    prema2.insert("column", 3)
    prema2.insert("hello", 5)
    prema2.insert("columns", 6)
    prema2.insert("hellos", 22)
    print(prema2.sum("col"))
    print(prema2.sum('hel'))
    pref_m_c = Prefix_map_complex()
    pref_m_c.insert('bag', 4)
    pref_m_c.insert('bath', 5)
    print("1 = ", pref_m_c.sum('b'))
    print("2 = ", pref_m_c.sum('ba'))
    print("3 = ", pref_m_c.sum('bat')) 