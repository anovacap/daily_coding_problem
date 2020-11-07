#!/usr/bin/python
# Hash Tables 5.3 - Implement a sparse array
# A large array with most elements being 0 - init(size) set(val) get(i)
# A list that either has 0's or numbers (ex. 257 in a binary number = [1,0,0,0,0,0,0,0,1])
# The class keeps track of the 1's in a dictionary that associates the index of the 1 with tthe value

class SparseArray:
    def __init__(self, arr, size):
        self.size = size
        self._dict = {}
        for i, e in enumerate(arr):
            if e != 0:
                self._dict[i] = e

    def check_bounds(self, i):
        if i < 0 or i >= self.size:
            raise IndexError('Out of bounds')
    def set(self, i, val):
        self.check_bounds(i)
        if val != 0:
            self._dict[i] = val
            return

    def get(self, i):
        self.check_bounds(i)
        return self._dict.get(i, 0)

if __name__ == "__main__":
    arr = [1,0,0,0,0,0,0,0,1] #257
    sa = SparseArray(arr, 25)
    #sa.check_bounds(26)
    #sa.set(28, 1)
    sa.set(15, 1)
    print(sa.get(14))
    print(sa.get(0))
