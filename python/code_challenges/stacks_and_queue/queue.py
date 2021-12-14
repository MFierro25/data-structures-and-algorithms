from stacks_and_queue.node import Node
from stacks_and_queue.error import EmptyError

class Queue:
    def __init__(self):
        self.front = None
        self.end = None
        self.size = 0
    
    def __len__(self):
        return self.size 
    
    def enqueue(self, value):
        new = Node(value, None)
        if self.is_empty():
            self.front = new
        else:
            self.end._next = new
        self.end = new
        self.size +=1
    
    def dequeue(self):
        if self.is_empty():
            raise EmptyError('Queue is empty')
        result = self.front.value
        self.front = self.front._next
        self.size -=1 
        if self.is_empty():
            self.end = None
        return result
    
    def peek(self):
        if self.is_empty():
            raise EmptyError('Queue is empty')
        return self.front.value
        
    def is_empty(self):
        return self.size == 0