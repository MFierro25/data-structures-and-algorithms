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
        self.dog_in_stack = []
        self.dog_out_stack = []
        
        self.cat_in_stack = []
        self.cat_out_stack = []
        
    def enqueue(self, animal):
        if isinstance(animal, Dog):
            self.dog_in_stack.append(animal)
            return
        
        if isinstance(animal, Cat):
            self.cat_in_stack.append(animal) 
            return
        
        else:
            raise AnimalError('Sorry, we only accept dogs and cats')
    
    def dequeue(self, pref = None):
        pass
    #     if len(self.in_stack) == 0 and len(self.out_stack) == 0:
    #         raise EmptyError('Queue is empty')
            
    #     elif len(self.out_stack) == 0 and len(self.in_stack) > 0:
    #         while len(self.in_stack):
    #             head = self.in_stack.pop()
    #             self.out_stack.append(head)
    #         return self.out_stack.pop()
    #     else:
    #         return self.out_stack.pop()
        