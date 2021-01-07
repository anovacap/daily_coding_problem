#!/usr/bin/python
# Daily Coding Problem - Tries: 8.2 Implement a Prefix Map Sum class
# methods = insert(key: str, value: int) - Sets a given key's value in the 
# map. If the key already exists, overwirte the value.
# methos = sum(grefix: str) - Return the sum of all values of keys that begin
# with the given prefix.

class PrefixMapSum:
    def __init__(self):
        self.map = {}
    
    def insert(self, key: str, value: int):
        self.map[key] = value
    
    def sum(self, prefix):
        return sum(value for key, value in self.map.items() if key.startswith(prefix))

if __name__ == "__main__":
    prefmapsum = PrefixMapSum()
    prefmapsum.insert("column", 3)
    prefmapsum.insert("hello", 5)
    prefmapsum.insert("columns", 6)
    prefmapsum.insert("hellos", 22)
    print(prefmapsum.sum("col"))
    print(prefmapsum.sum('hel'))
