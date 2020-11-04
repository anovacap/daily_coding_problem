#!/usr/bin/python
# Hash Tables - 5.1 Implement a least recently used cache
# 

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class dbl_ll:
    def __init__(self):
        self.head = Node(None, 'head')
        self.tail = Node(None, 'tail')
        self.head.next = self.tail
        self.tail.prev = self.head
    def prnt(self):
        printval = self.head
        while printval:
            print(printval.val)
            printval = printval.next
    
    def get_h(self):
        return self.head.next
    
    def get_t(self):
        return self.tail.prev

    def add(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

class lru_cache:
    def __init__(self, n):
        self.n = n
        self.dct = {}
        self.lst = dbl_ll()

    def set(self, key, val):
        if key in self.dct:
            self.dct[key].delete()
        n = Node(key, val)
        self.lst.add(n)
        self.dct[key] = n

        if len(self.dct) > self.n:
            head = self.lst.get_h()
            self.lst.remove(head)
            del self.dct[head.key]

    def get(self, key):
        if key in self.dct:
            n = self.dct[key]

            self.lst.remove(n)
            self.lst.add(n)
            return n.val
if __name__ == "__main__":
    n1 = Node(1, 'A')
    n2 = Node(2, 'B')
    n3 = Node(3, 'C')
    n4 = Node(4, 'D')
    dbl = dbl_ll()
    dbl.add(n1)
    dbl.add(n2)
    dbl.add(n3)
    dbl.add(n4)
    dbl.prnt()
    print("get_h", dbl.get_h())
    print("get_t", dbl.get_t())
    dbl.remove(n3)
    dbl.prnt()
    lruc = lru_cache(1)
    lruc.set(2,'B')
    print("lruc.get = ",lruc.get(2))


