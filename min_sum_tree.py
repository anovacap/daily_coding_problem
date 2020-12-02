#!/usr/bin/python
# Daily Coding Problem 6.4 - returns the node level with the lowest sum
from collections import deque, defaultdict
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
def min_sum_tree(root):
    queue = deque([])
    queue.append((root, 0))
    level_to_sum = defaultdict(int)

    while queue:
        node, level = queue.popleft()
        level_to_sum[level] += node.data
        if node.right:
            queue.append((node.right, level + 1))
        if node.left:
            queue.append((node.left, level + 1))
    return min(level_to_sum, key=level_to_sum.get)
if __name__ == "__main__":
    n5 = Node(5)
    n4 = Node(4)
    n3 = Node(3, n4, n5)
    n2 = Node(2)
    tree = Node(1, n2, n3)
    print(min_sum_tree(tree))