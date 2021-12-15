from stacks_and_queue.error import EmptyError
from stacks_and_queue.stacks import Stack

class Dog:
    def __init__(self, name):
        self.name = name
        
class Cat:
    def __init__(self, name):
        self.name = name
        
class Monkey:
    pass

class AnimalError(Exception):
    pass

class AnimalShelter:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()
        
    def enqueue(self, animal):
        if isinstance(animal, Dog) or isinstance(animal, Cat):
            self.in_stack.push(animal)
            return
        
        else:
            raise AnimalError('Sorry, we only accept dogs and cats')
    
    def dequeue(self, pref = None):
        if len(self.in_stack) == 0 and len(self.out_stack) == 0:
            raise EmptyError('Shelter is empty')
            
        elif len(self.out_stack) == 0 and len(self.in_stack) > 0:
            while len(self.in_stack):
                pass
        #         temp = self.in_stack.pop()
        #         self.out_stack.push(temp)
                
        #     return self.out_stack.pop()
        # else:
        #     return self.out_stack.pop()