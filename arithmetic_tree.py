#!/usr/bin/python
# Daily Coding Problem 6.3 - Each leaf is an integer and  each internal node
# is one of +, -, *, or /

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"

def evalu(root):
    if root.data == PLUS:
        return evalu(root.left) + evalu(root.right)
    if root.data == MINUS:
        return evalu(root.left) - evalu(root.right)
    if root.data == TIMES:
        return evalu(root.left) * evalu(root.right)
    if root.data == DIVIDE:
        return evalu(root.left) / evalu(root.right)
    else:
        return root.data

if __name__ == "__main__":
    PLUS = "+"
    MINUS = "-"
    TIMES = "*"
    DIVIDE = "/"
    n5 = Node(5)
    n4 = Node(4)
    n3 = Node(3)
    n2 = Node(2)
    nr = Node(PLUS, n4, n5)
    nl = Node(PLUS, n3, n2)
    tree = Node(TIMES,nl,nr)
    x = evalu(tree)
    print(x)
