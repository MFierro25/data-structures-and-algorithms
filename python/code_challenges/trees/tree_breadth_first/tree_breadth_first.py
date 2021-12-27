from code_challenges.trees.error import EmptyError
from stacks_and_queue.queue import Queue

def breadth_first(tree):
    if not tree.root:
        raise EmptyError('Tree is empty')
    
    return_list = []
    queue = Queue()
    
    queue.enqueue(tree.root)
    
    while queue.peek():
        self = queue.dequeue()
        
        queue.enqueue(self.left)      
        queue.enqueue(self.right)
            
        return_list.append(self.value)
        
    return return_list