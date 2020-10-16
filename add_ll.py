#!/usr/bin/python
# Chpater 3 Linked Lists - 3.2 Add two linked lists that represent numbers

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkl:
    def __init__(self):
        self.head = None
    def print_node(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next
    def insert(self, data):
        NewNode = Node(data)
        NewNode.next = self.head
        self.head = NewNode

def add(node0, node1, carry=0):
    if not node0 and not node1 and not carry:
        return None
    node0_val = node0.data if node0 else 0
    node1_val = node1.data if node1 else 0
    total = node0_val + node1_val + carry
    node0_next = node0.head.next if node0 else None
    node1_next = node1.head.next if node1 else None
    carry_next = 1 if total >= 10 else 0
    return Node(total % 10, add(node0_next, node1_next, carry_next))

if __name__ == "__main__":
    slnkl = linkl()
    slnkl.insert(9)
    slnkl.insert(9)
    slnkl2 = linkl() 
    slnkl2.insert(5)
    slnkl2.insert(2)
    # slnkl.insert(5)
    # slnkl.insert(4)
    # slnkl.insert(3)
    # slnkl.insert(2)
    # slnkl.insert(1)
    slnkl.print_node()
    slnkl2.print_node()
    a = add(slnkl, slnkl2, 1)
    print(a)
    