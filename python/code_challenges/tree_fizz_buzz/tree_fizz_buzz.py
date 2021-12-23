from code_challenges.tree_fizz_buzz.k_ary_tree import Ktree
from code_challenges.trees.error import EmptyError

def fizz_buzz_tree(tree):
    if tree.root is None:
        raise EmptyError('Tree is Empty')

    result_tree = Ktree()
    
    def walk(root):
        
        if root.value % 3 == 0:
            result_tree.insert('fizz')
        elif root.value % 5 == 0:
            result_tree.insert('buzz')
        elif root.value % 3 == 0 and root.value % 5 == 0:
            result_tree.insert('fizzbuzz')
        
        else:
            result_tree.insert(str(root.value))
        
    walk(tree.root)
    
    return result_tree