#!/usr/bin/python
# Daily Coding Problem 7.2 - Convert a sorted array into a binary search tree
# Given a sorted array, create a binary search tree by taking the middle of
# the array as the root and building the tree from there.

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val, root):
        if val < root.data:
            if not root.left:
                root.left = Node(val)
            else:
                self._insert(val, root.left)
        else:
            if not root.right:
                root.right = Node(val)
            else:
                self._insert(val, root.right)

    def find(self, val):
        if not self.root:
            return False
        else:
            return self._find(val, self.root)

    def _find(self, val, root):
        if not root:
            return False
        elif val == root.data:
            return True
        elif val < root.data:
            return self._find(val, self.root.left)
        else:
            return self._find(val, self.root.right)
    
    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)

    def preorder(self, root):
        if root is not None:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)
    
    def postorder(self, root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)
    
    def find_floor_n_ceil(self, root, val, floor=None, ceil=None):
        if not root:
            return floor, ceil
        if val == root.data:
            return val, val
        elif val < root.data:
            floor, ceil = self.find_floor_n_ceil(root.left, val, floor, root.data)
        elif val > root.data:
            floor, ceil = self.find_floor_n_ceil(root.right, val, root.data, ceil)
        return floor, ceil

    def make_bst(self, arr): # takes an array returns the root of a bst
        if not arr:
            return None
        mid = len(arr) // 2
        root = Node(arr[mid])
        root.left = self.make_bst(arr[:mid])
        root.right = self.make_bst(arr[mid + 1:])
        return root

if __name__ == "__main__":
    bst_tree = BST()
    bst_tree.insert(22)
    bst_tree.insert(90)
    bst_tree.insert(80)
    bst_tree.insert(11)
    bst_tree.insert(70)
    bst_tree.insert(35)
    bst_tree.insert(60)
    bst_tree.insert(40)
    bst_tree.insert(5)
    print("Inorder")
    bst_tree.inorder(bst_tree.root)
    print("Pre-Order")
    bst_tree.preorder(bst_tree.root)
    print("Post-Order")
    bst_tree.postorder(bst_tree.root)
    print("find_floor_ceil")
    print(bst_tree.find_floor_n_ceil(bst_tree.root, 71))
    print("Convert_arr_bst")
    a = [2,14,22,35,45,55,66,77,88,99]
    bst_tree.inorder(bst_tree.make_bst(a))
