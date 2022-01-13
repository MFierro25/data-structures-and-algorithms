from hashtable.error import EmptyError

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        
class Hashtable:
    def __init__(self,):
        self.capacity = 1024
        self.size = 0
        self.buckets = [None] * self.capacity
    
    def add(self, key, value):
        self.size += 1
        hash_index = self.hash(key)
        node = self.buckets[hash_index]
        
        if node is None:
            self.buckets[hash_index] = Node(key, value)
            return
        prev = node
        while node is not None:
            prev = node
            node =node.next
            
            prev.next = Node(key, value)
            
            
    def get(self, key):
        hash_index = self.hash(key)
        node = self.buckets[hash_index]
        
        #traverses through 
        while node is not None and node.key != key:
            node = node.next
            
        if node is None:
            raise EmptyError('No value at this key')
        else:
            return node.value
    
    def contains(self, key):
        hash_index = self.hash(key)
        node = self.buckets[hash_index]
        
        #traverses through 
        while node is not None and node.key != key:
            node = node.next
            
        if node is None:
            return False
        else:
            return True
    
    def hash(self, key):
        return sum([ord(char) for char in key]) * 599 % len(self.buckets)