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
        self.head = Node(value, self.head)    
                 
    def append(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.new_node != None:
                current = current.new_node
            current.new_node = new_node
        return self.head
    
    # prepend inserts in beggining of list (opposite of append)
    def prepend(self, value):
        new_node = Node(value)
        
        new_node.next = self.head
        self.head = new_node
    
    def insert_node_after(self, prev_node, value):
        
        # checks to see if node is in list
        if not prev_node:
            (print('Previous node selected is not in the list'))
            return
        new_node = Node(value)
        
        new_node.next = prev_node.next
        
        prev_node.next = new_node
    
    # changes list into strings
    def __str__(self):
        current = self.head
        output = ""

        while current:
            output += "{ " + current.value + " } -> "
            current = current.next

        output += "NULL"
        return output

            
# lst = LinkedList    
# lst.insert('4')
# lst.append('5')
# print(lst)

