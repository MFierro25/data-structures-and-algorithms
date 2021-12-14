
from linked_list_insertions.linked_list_insertions import LinkedList


## succesfully insert node to empty list
def test_node_inserts_to_head():
    lst = LinkedList()
    lst.append('first')
    assert lst.head.value == 'first'
    
# Can successfully add a node to the end of the linked list

def test_append_to_end():
    lst = LinkedList()
    lst.insert('four')
    lst.append('five')
    actual = lst.head.value
    expected = 'four'
    assert actual == expected
    
    actual = lst.head.next.value
    expected = 'five'
    
    
# Can successfully add multiple nodes to the end of a linked list

def test_append_multiple():
    lst = LinkedList()
    lst.insert('four')
    lst.append('five')
    lst.append('six')
    actual = lst.head.value
    expected = 'four'
    assert actual == expected
    actual = lst.head.next.value
    expected = 'five'
    
    actual = lst.head.next.next.value
    expected = 'six'
    
    
# Can successfully insert a node before a node located in the middle of a linked list

def test_insert_middle_before():
    lst = LinkedList()
    lst.insert('four')
    lst.append('five')
    lst.insert_before('five', 'ten')
    actual = lst.head.value
    expected = 'four'
    assert actual == expected
    actual = lst.head.next.value
    expected = 'ten'
    
    actual = lst.head.next.next.value
    expected = 'five'
   

# Can successfully insert a node before the first node of a linked list
def test_prepend():
    lst =LinkedList()
    lst.insert('four')
    lst.prepend('three')
    actual = lst.head.value
    expected = 'three'
    
    actual = lst.head.next.value
    expected = 'four'
    
    assert actual == expected
    
# Can successfully insert after a node in the middle of the linked list

def test_insert_middle_after():
    lst = LinkedList()
    lst.insert('four')
    lst.append('five')
    lst.append('six')
    lst.insert_after('five', 'ten')
    actual = lst.head.value
    expected = 'four'
    assert actual == expected
    actual = lst.head.next.value
    expected = 'five'
    
    actual = lst.head.next.next.value
    expected = 'ten'
    
    actual = lst.head.next.next.next.value
    expected = 'six'

# Can successfully insert a node after the last node of the linked list

def test_insert_end():
    lst = LinkedList()
    lst.insert('four')
    lst.append('five')
    lst.append('six')
    lst.insert_after('six', 'ten')
    actual = lst.head.value
    expected = 'four'
    assert actual == expected
    actual = lst.head.next.value
    expected = 'five'
    
    actual = lst.head.next.next.value
    expected = 'six'
    
    actual = lst.head.next.next.next.value
    expected = 'ten'