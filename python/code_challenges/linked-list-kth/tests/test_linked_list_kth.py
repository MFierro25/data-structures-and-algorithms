from linked_list_kth.linked_list_kth import LinkedList
import pytest

def test_node_inserts_to_head():
    lst = LinkedList()
    lst.append('first')
    assert lst.head.value == 'first'

#test that kth method is working

def test_kth_from_end():
    lst = LinkedList()
    lst.insert(1)
    lst.append(2)
    lst.append(3)
    actual = lst.kth_From_End(1)
    expected = 3
    assert actual == expected  
    
# Where k is greater than the length of the linked list

def test_kth_for_length_error():
    lst = LinkedList()
    lst.insert(1)
    lst.append(2)
    lst.append(3)
    with pytest.raises(ValueError):
        lst.kth_From_End(5)
    
# Where k and the length of the list are the same

def test_kth_same_length():
    lst = LinkedList()
    lst.insert(1)
    lst.append(2)
    lst.append(3)
    actual = lst.kth_From_End(3)
    expected = 1
    assert actual == expected  

# Where k is not a positive integer

def test_kth_for_negative_error():
    lst = LinkedList()
    lst.insert(1)
    lst.append(2)
    lst.append(3)
    with pytest.raises(ValueError):
        lst.kth_From_End(-1)
        
# Where the linked list is of a size 1

def test_kth_length_one():
    lst = LinkedList()
    lst.insert(1)
    actual = lst.kth_From_End(1)
    expected = 1
    assert actual == expected 

# “Happy Path” where k is not at the end, but somewhere in the middle of the linked list

def test_kth_middle():
    lst = LinkedList()
    lst.insert(1)
    lst.append(2)
    lst.append(3)
    actual = lst.kth_From_End(2)
    expected = 2
    assert actual == expected  