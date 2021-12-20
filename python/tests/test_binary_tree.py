from code_challenges.trees.node import Node
from code_challenges.trees.binary_tree import BinaryTree

# Can successfully instantiate an empty tree
def test_binary_tree():
    tree = BinaryTree()
    assert True
    
# Can successfully instantiate a tree with a single root node
def test_single_node():
    one = Node('A')
    tree = BinaryTree(one)
    actual = tree.root.value
    expected = 'A'
    assert actual == expected

# Can successfully add a left child to a single root node
def test_left_child():
    one = Node('A')
    one.left = Node('B')
    
    tree = BinaryTree(one)
    expected = ['A', 'B']
    actual = tree.pre_order()
    
    assert actual == expected
    
# Can succesfully add a right child to a single root node

def test_right_child():
    one = Node('A')
    one.right = Node('C')
    
    tree = BinaryTree(one)
    expected = ['C', 'A']
    actual = tree.post_order()
    
    assert actual == expected 
    
    
#Can successfully return a collection from a preorder traversal
def test_pre_order():
    one = Node('A')
    one.left = Node('B')
    one.right = Node('C')
    
    tree = BinaryTree(one)
    expected = ['A', 'B', 'C']
    actual = tree.pre_order()
    
    assert actual == expected 
    
# Can successfully return a collection from an inorder traversal
def test_in_order():
    one = Node('A')
    one.left = Node('B')
    one.right = Node('C')
    
    tree = BinaryTree(one)
    expected = ['B', 'A', 'C']
    actual = tree.in_order()
    
    assert actual == expected 
    
# Can successfully return a collection from a postorder traversal
def test_post_order():
    one = Node('A')
    one.left = Node('B')
    one.right = Node('C')
    
    tree = BinaryTree(one)
    expected = ['B', 'C', 'A']
    actual = tree.post_order()
    
    assert actual == expected 
    