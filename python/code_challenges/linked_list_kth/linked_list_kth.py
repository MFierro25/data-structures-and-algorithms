class Node:
    '''
    creates a new node object
    '''
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
class LinkedList:
    '''
    creates a linked list made up of nodes
    '''
    def __init__(self):
        self.head = None   
    
    def insert(self, value):
        self.head = Node(value)
                         
    def append(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        
        while current.next:
            current = current.next
        
        current.next = new_node
    
    def kth_From_End(self, k):
        cur = self.head
        
        length = 0
        
        while cur is not None:
            cur = cur.next
            length += 1
         
        if k < 0:
            raise ValueError('Please enter a valid positive number')
           
        if k > length:
            raise ValueError('Value is greater than length of List')
        
        cur = self.head
        for _ in range(0, length - k):
            cur = cur.next
        return cur.value
        
        
        # def __str__(self):
    #     current = self.head
    #     output = ""

    #     while current:
    #         output += "{ " + current.value + " } -> "
    #         current = current.next

    #     output += "NULL"
    #     return output
