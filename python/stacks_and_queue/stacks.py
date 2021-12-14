from stacks_and_queue.node import Node
from stacks_and_queue.error import EmptyError

        
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def __len__(self):
        return self.size
        
    def push(self, value):
        self.top = Node(value, self.top)
        self.size += 1
        
    def pop(self):
        if self.is_empty():
            raise EmptyError('The stack is currently empty.')
        result = self.top.value
        # this assigns the next available value as the top after the first is popped
        self.top = self.top._next
        self.size -= 1
        return result
        
    def is_empty(self):
        return self.size == 0
            
    
    def peek(self):
        if self.is_empty():
            raise EmptyError('The stack is currently empty')
        return self.top.value
    
