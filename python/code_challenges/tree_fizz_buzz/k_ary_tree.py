from code_challenges.tree_fizz_buzz.node import Node
from collections import deque

class Ktree:
    def __init__(self, k):
        self.root = None
        self.k = k
        
    def insert(self, value):
        node = Node(value)
        
        if self.root is None:
            self.root = node
            return
        
        
        
            
        
            