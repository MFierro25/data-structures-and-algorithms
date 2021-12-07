
from linked_list_insertions.linked_list_insertions import LinkedList


## succesfully insert node to empty list
def test_node_inserts_to_head():
    lst = LinkedList()
    lst.append('first')
    assert lst.head.value == 'first'
    
# Can successfully add a node to the end of the linked list

# def test_append_to_end():
#     lst = LinkedList
#     lst.insert('four')
#     lst.append('five')
#     assert lst.head.value == 'four'
#     assert lst.head.next.value == 'five'
    
# Can successfully add multiple nodes to the end of a linked list

# Can successfully insert a node before a node located in the middle of a linked list

# Can successfully insert a node before the first node of a linked list

# Can successfully insert after a node in the middle of the linked list

# Can successfully insert a node after the last node of the linked list
