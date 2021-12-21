# Trees
<!-- Short summary or background information -->
"A tree is a nonlinear hierarchical data structure that consists of nodes connected by edges" 

## Challenge
<!-- Description of the challenge -->
Node : Create a Node class that has values stored in the node, the left child node, and the right child node. <br> 
Binary Tree: define 3 methods.
- Pre-order
- In-order
- post-orderd

Binary Search Tree: should be a sub-class with additional methods
- add
- contains 

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
followed example from class to understand the difference between post, pre and in order.

Binary tree:<br>
Time = O(n) space = O(n)

add:<br>
Time = O(log) Space = O(1)

Contains:<br>
time = O(log) space = O(1)

## API
<!-- Description of each method publicly available in each of your trees -->
add() - adds a node to existing tree
contains() - searches tree for existing values in tree

## Sources 
[1](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-15/resources/Trees.html)
[2](https://github.com/codefellows/seattle-python-401d17/tree/main/class-15)
[3](https://www.programiz.com/dsa/trees)

# Challenge 16 Find Max

## Challenge Summary
<!-- Description of the challenge -->
Write the following method for the Binary Tree class

"find maximum value"
Arguments: none
Returns: number


Find the maximum value stored in the tree.


## Whiteboard Process
<!-- Embedded whiteboard image -->
![Tree Max Diagram](assets/tree_max.png)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Time: O(N)
Space: O(1)

## Solution
<!-- Show how to run your code, and examples of it in action -->

```python

def tree_max(self)
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
```