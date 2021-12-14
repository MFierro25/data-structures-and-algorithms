# Challenge Summary
<!-- Description of the challenge -->
create a PsuedoQueue class that uses proper enqueue and dequeue utilizing two stacks inside of queue

## Whiteboard Process
<!-- Embedded whiteboard image -->
![Stack and Queue Psuedo](https://github.com/MFierro25/data-structures-and-algorithms/blob/926479a79bdaa3589dcb374327b0f5adb0300e54/python/assets/stack-queue-pseudo.png)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
the process was simple, when enqueue insert everything in the first stack, once everything is entered then you can pop from the top and insert the elements to the second stack. after that the second stack is ready to pop and dequeue properly following the first in first out model.

time: O(1) - it takes constant time to complete the operations
space: O(N) - increases linearly, with more elements the more proportionaly it grows

## Solution
<!-- Show how to run your code, and examples of it in action -->
```python
def dequeue(self):
        if len(self.in_stack) == 0 and len(self.out_stack) == 0:
            raise EmptyError('Queue is empty')
            
        elif len(self.out_stack) == 0 and len(self.in_stack) > 0:
            while len(self.in_stack):
                head = self.in_stack.pop()
                self.out_stack.append(head)
            return self.out_stack.pop()
        else:
            return self.out_stack.pop()
```
