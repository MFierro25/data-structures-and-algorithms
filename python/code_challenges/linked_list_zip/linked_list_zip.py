class Node:
    '''
    creates a new node object
    '''
    def __init__(self, value=None, next=None):
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
        
    def print_list(self):
        cur = self.head
        while (cur):
            print(cur.value)
            cur = cur.next

    def merge_lists(self, first_lst, second_lst):
        
        first_cur = first_lst.head
        sec_cur = second_lst.head
        
        while first_cur != None and sec_cur != None:
            first_next = first_cur.next
            sec_next = sec_cur.next
            
            sec_cur.next = first_next
            first_cur.next = sec_cur
            
            first_cur = first_next
            sec_cur = sec_next
            second_lst.head = sec_cur

list_one = LinkedList()
list_one.insert('one')
list_one.append('three')
list_one.append('five')
list_one.print_list()

list_two = LinkedList()
list_two.insert('two')
list_two.append('four')
list_two.append('six')
list_two.print_list()

list_one.merge_lists(first_lst = list_one, second_lst = list_two)
list_one.print_list()
