#!/usr/bin/python
# Chpater 3 Linked Lists - Reverse a linked list 3.1
# 

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class slinkedl:
    def __init__(self):
        self.head = None

    def print_node(self):
        printval = self.head
        while printval != None:
            print(printval.data)
            printval = self.head.next

def reverse(node):
    # _reverse() reverses and returns both head and tail
    # Conventionally, an underscore denotes an unused variable.
    head, _ = _reverse(node)
    return head

def _reverse(node):
    if node is None: # checks for empty linked list
        return None, None

    if node.next is None: # returns the tail
        return node, node

    # Reverse rest of llinked list and move node to after tail
    head, tail = _reverse(node.next)
    node.next = None
    tail.next = node
    return head, node

if __name__ == "__main__":
    slist = slinkedl()
    slist.head = Node("A")
    n2 = Node("B")
    n3 = Node("C")
    slist.head.next = n2
    n2.next = n3
    n3.next = None
    slist.print_node()