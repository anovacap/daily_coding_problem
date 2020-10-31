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
        while printval:
            print(printval.data)
            printval = printval.next

    def insert(self, data):
        NewNode = Node(data)
        NewNode.next = self.head
        self.head = NewNode

    def add(self, node0, node1):
        prev = None
        temp = None
        carry = 0
        
        while node0 is not None or node1 is not None:
            fdata = 0 if node0 is None else node0.data 
            sdata = 0 if node1 is None else node1.data 
            Sum = carry + fdata + sdata
            carry = 1 if Sum >= 10 else 0
            Sum = Sum if Sum < 10 else Sum % 10
            temp = Node(Sum)
            if self.head is None:
                self.head = temp
            else: 
                prev.next = temp
            prev = temp
            if node0 is not None:
                node0 = node0.next
            if node1 is not None:
                node1 = node1.next
        if carry > 0:
            temp.next = Node(carry)

        # node0_val = node0.data if node0 else 0
        # node1_val = node1.data if node1 else 0
        # total = node0_val + node1_val + carry
        # node0_next = node0.next if node0 else None
        # node1_next = node1.next if node1 else None
        # carry_next = 1 if total >= 10 else 0
        # return linkl(total % 10, add(node0_next, node1_next, carry_next))

if __name__ == "__main__":
    slnkl = linkl()
    slnkl2 = linkl() 
    slnkl.insert(5)
    slnkl.insert(4)
    slnkl.insert(3)
    slnkl.insert(2)
    slnkl.insert(1)
    slnkl2.insert(6)
    slnkl2.insert(7)
    slnkl2.insert(8) 
    print("slnk = {}".format(slnkl.print_node()))
    print("slnk2 = {}".format(slnkl2.print_node()))
    res = linkl()
    res.add(slnkl.head,slnkl2.head)
    # print("Add result = {}".format(res.print_node()))
    res.print_node()
