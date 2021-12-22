from code_challenges.trees.error import EmptyError
from stacks_and_queue.queue import Queue

def breadth_first(tree):
    if not tree.root:
        raise EmptyError('Tree is empty')
    
    return_list = []
    queue = Queue()
    
    queue.enqueue(tree.root)
    
    while len(queue) > 0:
        self = queue.dequeue()
        
        if self.left:
            self.enqueue(self.left)
        if self.right:
            self.enqueue(self.right)
            
        return_list.append(self.value)
        
    return return_list