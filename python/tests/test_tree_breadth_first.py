from code_challenges.trees.tree_breadth_first.tree_breadth_first import breadth_first
from code_challenges.trees.node import Node
from code_challenges.trees.binary_tree import BinaryTree
from code_challenges.trees.error import EmptyError
import pytest 

def test_import():
    assert breadth_first
    
# test empty error 

def test_empty_error():
    tree = BinaryTree()
    with pytest.raises(EmptyError):
        breadth_first(tree)
        
def test_one_value():
    first = Node(1)
    tree = BinaryTree(first)
    assert breadth_first(tree) == [1]
    
def test_one_height():
    first = Node(1)
    first.left = Node(10)
    first.right = Node(100)
    tree = BinaryTree(first)
    assert breadth_first(tree) == [1, 10, 100]
    
def test_two_height():
    first = Node(1)
    first.left = Node(10)
    first.right = Node(100)
    first.left.left = Node(20)
    first.left.right = Node(200)
    tree = BinaryTree(first)
    assert breadth_first(tree) == [1, 10, 100, 20, 200]