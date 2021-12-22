# Challenge Summary
<!-- Description of the challenge -->
Write a function called breadth first

Arguments: tree

Return: list of all values in the tree, in the order they were encountered

[Code](python/code_challenges/trees/tree_breadth_first/tree_breadth_first.py)

## Whiteboard Process
<!-- Embedded whiteboard image -->
![Tree Breadth First](https://github.com/MFierro25/data-structures-and-algorithms/blob/b7787a5d2e40cce1c42743755ddb340e79abb934/python/assets/tree-breadth-first.png)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Time: O(n) - due to the number of nodes going one by one
space: O(n) - n is the total nodes

## Solution
<!-- Show how to run your code, and examples of it in action -->

```python
def breadth_first(tree):
    if not tree.root:
        raise EmptyError('Tree is empty')
    
    return_list = []
    queue = Queue()
    
    queue.enqueue(tree.root)
    
    while len(queue) > 0:
        self = queue.dequeue()
        
        if self.left:
            self.enqueue(self.left)
        if self.right:
            self.enqueue(self.right)
            
        return_list.append(self.value)
        
    return return_list
```

## Sources
[1](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-15/resources/Trees.html)
[2](https://www.youtube.com/watch?v=aM-oswPn19o)
[3](https://csanim.com/tutorials/breadth-first-search-python-visualization-and-code)
