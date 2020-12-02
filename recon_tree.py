#!/usr/bin/python
# Trees - 6.2 Reconstruct  tree from pre-order traversal
# Given pre-order and in-order traversalsof a binary tree, write a function
# to reconstruct the tree

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
    
    def is_unival(self, root):
        return self.unival_helper(root, root.data)
    
    def unival_helper(self, root, val):
        if root is None:
            return True
        if root.data == val:
            return self.unival_helper(root.left, val) and self.unival_helper(root.right, val)
        return False

    def count_unival_subtree(self, root):
        if root is None:
            return 0
        left = self.count_unival_subtree(root.left)
        right = self.count_unival_subtree(root.right)
        return 1 + left + right if self.is_unival(root) else left + right
                

    
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
    
    def reconstruct(self, preorder, inorder):
        if not preorder and not inorder:
            return None
        if len(preorder) == len(inorder) == 1:
            return 0
        recon_root = preorder[0]
        root_i = inorder.index(recon_root)
        recon_root.left = self.reconstruct(preorder[1:1 + root_i], inorder[0:root_i])
        recon_root.right = self.reconstruct(preorder[1 + root_i:], inorder[root_i + 1:])
        return recon_root


if __name__ == "__main__":
    root = None
    tree = Tree()
    root = tree.insert(root, 10)
    #print(root)
    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(30)
    n4 = Node(40)
    n5 = Node(1)
    n6 = Node(2)
    n7 = Node(70)
    n8 = Node(60)
    n9 = Node(80)
    tree.insert(root, 20)
    tree.insert(root, 30)
    tree.insert(root, 40)
    tree.insert(root, 1)
    tree.insert(root, 2)
    tree.insert(root, 70)
    tree.insert(root, 60)
    tree.insert(root, 80)
    inord = [n1,n2,n3,n4,n5,n6,n7,n8,n9]
    prord = [n1,n2,n3,n4,n5,n6,n7,n8,n9]
    print(tree.reconstruct(inord,prord))
