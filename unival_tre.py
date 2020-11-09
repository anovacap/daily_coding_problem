#!/usr/bin/python
# Trees - 6.1 Count unival (Universal Value) trees
# Given the root of a binary tree, count the numbr or unival subtrees

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def create_tree(self, data):
        return Node(data)
    
    def insert(self, node, data):
        if node is None:
            return self.create_tree(data)
        if data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)
        return node
    
    def search(self, node, data):
        if node is None or node.data == data:
            return node
        if node.data < data:
            return self.search(node.right, data)
        else:
            return self.search(node.left, data)

    def delete(self, node, data):
        if node is None:
            return None
        if node.data < data:
            node.right = self.delete(node.right, data)
        elif node.data > data:
            node.left = self.delete(node.left, data)
        else:
            if node.right is None and node.right is None:
                del node
            if node.left == None:
                temp = node.right
                del node
                return temp
            elif node.right == None:
                temp = node.left
                del node
                return temp
        return node
    
    def traverse_inorder(self, root):
        if root is not None:
            self.traverse_inorder(root.left)
            print(root.data)
            self.traverse_inorder(root.right)
            
        
    def traverse_preorder(self, root):
        if root is not None:
            print(root.data)
            self.traverse_preorder(root.left)
            self.traverse_preorder(root.right)

    def traverse_postorder(self, root):
        if root is not None:
            self.traverse_postorder(root.left)
            self.traverse_postorder(root.right)
            print(root.data)

if __name__ == "__main__":
    root = None
    tree = Tree()
    root = tree.insert(root, 10)
    print(root)
    tree.insert(root, 20)
    tree.insert(root, 30)
    tree.insert(root, 40)
    tree.insert(root, 70)
    tree.insert(root, 60)
    tree.insert(root, 80)
    print ("Traverse Inorder")
    tree.traverse_inorder(root)

    print ("Traverse Preorder")
    tree.traverse_preorder(root)

    print ("Traverse Postorder")
    tree.traverse_postorder(root)
            

    