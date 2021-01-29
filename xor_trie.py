#!/usr/bin/python
# Tries 8.3: Find maximum XOR of elemant pairs
# Given an array of ints, find the max XOR of and 2 elements

class Trie:
    def __init__(self, k):
        self._trie = {}
        self.size = k
    
    def insert(self, item):
        trie = self._trie

        for i in range(self.size, -1, -1):
            bit = bool(item & (1 << i))
            if bit not in trie:
                trie[bit] = {}
            trie = trie[bit]
    
    def find_max_xor(self, item):
        trie = self._trie
        xor = 0
        for i in range(self.size, -1, -1):
            bit = bool(item & (1 << 1))
            if (1 - bit) in trie:
                xor |= (1 << i)# |= is ior (either or). This is equal to xor = xor | (1 << i)
                # | is bitwise OR
                trie = trie[1 - bit]
            else:
                trie = trie[bit]
        return xor

if __name__ == "__main__":
    xtrie = Trie(1)
    xtrie.insert(0)
    xtrie.insert(1)
    xtrie.insert(0)
    xtrie.insert(1)
    xtrie.insert(0)
    xtrie.insert(0)
    xtrie.insert(1)
    print("res = ", xtrie.find_max_xor(1))