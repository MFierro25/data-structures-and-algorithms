from code_challenges.trees.node import Node
from code_challenges.trees.error import EmptyError

class BinaryTree: 
    def __init__(self, root = None):
        self.root = root
        
    def pre_order(self):
        '''
        root -> left -> right
        '''
        pre_list = []
        
        def walk(root):
            if root is None:
                return
            pre_list.append(root.value)
            walk(root.left)
            walk(root.right)
            
        walk(self.root)
        
        return pre_list
    
    def in_order(self):
        '''
        left -> root -> right
        '''
        in_list = []
        
        def walk(root):
            if root is None:
                return
            
            walk(root.left)
            in_list.append(root.value)
            walk(root.right)
            
        walk(self.root)
        
        return in_list
    
    def post_order(self):
        '''
        left -> right -> root
        '''
        
        post_list = []
        
        def walk(root):
            if root is None:
                return
            walk(root.left)
            walk(root.right)
            post_list.append(root.value)
            return
        
        walk(self.root)
        
        return post_list
    
    def tree_max(self):
        '''
        returns max value
        '''
        if not self.root:
            raise EmptyError('List is empty')
        
        def walk(root, cur_max):
            if root is None:
                return cur_max
            
            if root.value > cur_max:
                cur_max = root.value
                
            cur_max = walk(root.left, cur_max)
            return walk(root.right, cur_max)
        
        if self.root:
            return walk(self.root, self.root.value)
             