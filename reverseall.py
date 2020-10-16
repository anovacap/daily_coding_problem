#!/usr/bin/python
# Chpater 3 Linked Lists - Reverse a linked list 3.1
# 

class Node:
    # Constructor to initialize the Node object
    def __init__(self, data):
        self.data = data
        self.next = None

class slinkedl:
    # Function to initialize head
    def __init__(self):
        self.head = None

    def print_node(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next
    def insert(self, data):
        new_node = Node(data)

    def AtBegining(self, newdata):
        # new nodes are made head and previous head node is made next node of head stacked
        # Last in First Out LIFO
        NewNode = Node(newdata)
        NewNode.next = self.head
        self.head = NewNode

    #def reverse(node):
    # _reverse() reverses and returns both head and tail
    # Conventionally, an underscore denotes an unused variable.
        #head, _ = _reverse(node)
        #return head

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

if __name__ == "__main__":
    slist = slinkedl()
    slist.AtBegining("D")
    slist.AtBegining("C")
    slist.AtBegining("B")
    slist.AtBegining('A')
    slist.print_node()
    print("The reverse list = ", slist.reverse())
    print("slist.print_node()", slist.print_node())