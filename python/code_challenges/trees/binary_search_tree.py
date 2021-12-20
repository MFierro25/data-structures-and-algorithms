from code_challenges.trees.node import Node
from code_challenges.trees.binary_tree import BinaryTree
from code_challenges.trees.error import EmptyError


class BinarySearchTree(BinaryTree):
    
    def add(self, value):
        def __init__(self):
            self.root = None
            
        node = Node(value)
        
        if not self.root:
            self.root = node
            return
            
        def walk(root, inserted_node):
            if not root:
                return
            
            if inserted_node.value < root.value:
                if root.left:
                    walk(root.left, node)
                else: 
                    root.left = node
                    
            else:
                if root.right:
                    walk(root.right, node)
                else:
                    root.right = node
                    
        walk(self.root, node)
        
    def contains(self, value):
        if not self.root:
            raise EmptyError('List is empty')
        
        def walk(root, value):
            if root.value == value:
                return True
            
            elif value > root.value:
                if root.right:
                    return walk(root.right, value)
            
            elif value < root.value:
                if root.left:
                    return walk(root.left, value)
            
            return False
        
        return walk(self.root, value)