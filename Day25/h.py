from sys import *
from collections import *
from math import *

# Following is the Binary Tree node structure:
class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

def getTreeTraversal(root):
    inorder_result = []
    preorder_result = []
    postorder_result = []

    # --- Helper Functions for each traversal ---
    
    def traverse_inorder(node):
        if not node:
            return
        traverse_inorder(node.left)      # Left
        inorder_result.append(node.data) # Root
        traverse_inorder(node.right)     # Right

    def traverse_preorder(node):
        if not node:
            return
        preorder_result.append(node.data)# Root
        traverse_preorder(node.left)     # Left
        traverse_preorder(node.right)    # Right

    def traverse_postorder(node):
        if not node:
            return
        traverse_postorder(node.left)    # Left
        traverse_postorder(node.right)   # Right
        postorder_result.append(node.data)# Root

    # --- Execution ---
    
    traverse_inorder(root)
    traverse_preorder(root)
    traverse_postorder(root)
    
    return [inorder_result, preorder_result, postorder_result]