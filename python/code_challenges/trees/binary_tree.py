from code_challenges.trees.node import Node

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