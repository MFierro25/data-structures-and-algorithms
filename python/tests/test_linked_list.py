from linked_list.linked_list import Node, LinkedList

# Can successfully instantiate an empty linked list
def test_list():
    assert LinkedList()

# Can properly insert into the linked list
def test_node_insert():
    lst = LinkedList()
    lst.insert('car')
    assert lst.head.value == 'car'

# The head property will properly point to the first node in the linked list
def test_node_head():
    lst = LinkedList()
    lst.insert('car')
    lst.insert('house')
    assert lst.head.value == 'car'
    
# Can properly insert multiple nodes into the linked list

def list_mult_inserts():
    lst = LinkedList()
    lst.insert('car')
    lst.insert('house')
    assert lst.head.value == 'car'
    assert lst.head.next.value == 'house'
    
# Will return true when finding a value within the linked list that exists

def list_true():
    lst = LinkedList()
    lst.insert('money')
    actual = lst.includes('money')
    expected = True
    assert actual == expected

# Will return false when searching for a value in the linked list that does not exist

def list_false():
    lst = LinkedList()
    lst.insert('money')
    actual = lst.includes('house')
    expected = False
    assert actual == expected
    
# Can properly return a collection of all the values that exist in the linked list
def return_list():
    lst = LinkedList()
    lst.insert('run')
    lst.insert('fast')
    actual = ['run', 'fast']
    expected = ['run', 'fast']
    assert actual == expected