from code_challenges.trees.node import Node
from code_challenges.trees.binary_tree import BinaryTree
from code_challenges.trees.binary_search_tree import BinarySearchTree
from code_challenges.trees.error import EmptyError
import pytest

def test_binary_search_tree():
    bst = BinarySearchTree()
    assert True
    
def test_empty_list_error():
    bst = BinarySearchTree()
    with pytest.raises(EmptyError):
        bst.contains(5)
        
def test_add():
    bst = BinarySearchTree()
    bst.add(1)
    actual = bst.root.value
    expected = 1
    assert actual == expected
    
    
def test_contain():
    bst = BinarySearchTree()
    bst.add(1)
    actual = bst.contains(1)
    expected = True
    assert actual == expected
    
def test_add_multiple():
    bst = BinarySearchTree()
    bst.add(10)
    bst.add(1)
    bst.add(100)
    actual = bst.in_order()
    expected = [1, 10, 100]
    assert actual == expected 
    
def test_contain_large_tree():
    bst = BinarySearchTree()
    bst.add(10)
    bst.add(1)
    bst.add(100)
    actual = bst.contains(10)
    expected = True
    assert actual == expected 

def test_contain_false():
    bst = BinarySearchTree()
    bst.add(10)
    bst.add(1)
    bst.add(100)
    actual = bst.contains(2)
    expected = False
    assert actual == expected