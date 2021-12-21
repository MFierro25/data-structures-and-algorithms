from code_challenges.trees.binary_tree import BinaryTree
from code_challenges.trees.node import Node
from code_challenges.trees.error import EmptyError
import pytest


# test max on empty list to raise an error

def test_empty_list_max():
    tree = BinaryTree()
    with pytest.raises(EmptyError):
        tree.tree_max()
        
# test max on solo tree       
def test_solo_tree():
    one = Node(1)
    tree = BinaryTree(one)
    actual = tree.tree_max()
    expected = 1
    assert actual == expected
    
## multiple max tests below

def test_right_max():
    one = Node(5)
    one.left = Node(10)
    one.right = Node(15)
    
    tree = BinaryTree(one)
    expected = tree.tree_max()
    actual = 15
    
    assert actual == expected 
    
def test_left_max():
    one = Node(5)
    one.left = Node(20)
    one.right = Node(10)
    
    tree = BinaryTree(one)
    expected = tree.tree_max()
    actual = 20
    
    assert actual == expected 
    
def test_large_max():
    one = Node(5)
    one.left = Node(20)
    one.right = Node(10)
    one.left.left = Node(12)
    one.left.right = Node(100)
    one.right.right = Node(50)
    
    tree = BinaryTree(one)
    expected = tree.tree_max()
    actual = 100
    
    assert actual == expected 