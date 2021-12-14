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
    
    # prepend inserts in beggining of list (opposite of append)
    def prepend(self, value):
        new_node = Node(value)
        
        new_node.next = self.head
        self.head = new_node
        
    def insert_before(self, key, value):
        cur = self.head
        
        if cur.value == key:
            self.insert(value)
            return
        while cur.next.value != key:
            cur = cur.next
        cur.next = Node(value, cur.next)
        
    def insert_after(self, key, value):
        cur = self.head

        if not key:
            print('Previous node is not in list')
            return
        
        while cur:
            if cur.value == key:
                cur.next = Node(value, cur.next)
                return
            
            else:
                cur = cur.next
            
    # def __str__(self):
    #     current = self.head
    #     output = ""

    #     while current:
    #         output += "{ " + current.value + " } -> "
    #         current = current.next

    #     output += "NULL"
    #     return output