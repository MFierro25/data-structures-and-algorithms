from stacks_and_queue.error import EmptyError

class PsuedoQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
        
    def enqueue(self, value):
        self.in_stack.append(value)
    
    def dequeue(self):
        if len(self.in_stack) == 0 and len(self.out_stack) == 0:
            raise EmptyError('Queue is empty')
            
        elif len(self.out_stack) == 0 and len(self.in_stack) > 0:
            while len(self.in_stack):
                head = self.in_stack.pop()
                self.out_stack.append(head)
            return self.out_stack.pop()
        else:
            return self.out_stack.pop()
        