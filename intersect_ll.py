#!/usr/bin/python
# Find intersecting nodes of a linked list - 3.4
# Given 2 singly linked lists find where they intersect 
# l1 = 1 -> 4 -> 6 -> 10
# l2 = 2 -> 3 -> 6 -> 9
# 6 is the intersect - returns node 6
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class llist:
    def __init__(self):
        self.head = None
    def print_list(self):
        printval = self.head
        while printval:
            print(printval.data)
            printval = printval.next
    def insert(self, data):
        NewNode = Node(data)
        NewNode.next = self.head
        self.head = NewNode
    def length(self, head):
        if not head:
            return 0
        return 1 + self.length(head.next)

    def intersect(self, node1, node2):
        m, n = self.length(node1), self.length(node2)
        print("node1 len = ", m)
        print("node2 len = ", n)
        cur_a, cur_b = node1, node2
        if m > n:
            for _ in range(m - n):
                cur_a = cur_a.next
                print("c_a.data = ", cur_a.data)
        else:
            for _ in range(n - m):
                cur_b = cur_b.next
                print(cur_a.data)
        #print(cur_b.data)
        while cur_a != cur_b:
            cur_a = cur_a.next
            #print("c_a.data = ", cur_a.data)
            cur_b = cur_b.next
            if cur_a.data == cur_b.data:
                #print("c_b.data = ", cur_b.data)
                #print("cur_a = ", cur_a.data)
                return cur_a.data
if __name__ == "__main__":
    l1 = llist()
    l2 = llist()
    l1.insert(3)
    l1.insert(7)
    l1.insert(8)
    l1.insert(10)
    l2.insert(99)
    l2.insert(1)
    l2.insert(8)
    l2.insert(10)
    res = llist()
    print(res.intersect(l1.head,l2.head))
    res.print_list()
