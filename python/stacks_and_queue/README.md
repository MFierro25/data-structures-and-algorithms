# Stacks and Queues
<!-- Short summary or background information -->
A Stack is a container of objects inserted and removed from the top or last in first out. A Queue is a container of objects that are inserted and removed according first-in first-out. 

## Challenge
<!-- Description of the challenge -->
Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue. Add push, pop, peek, and is empty to stack class.for Queue add enqueueu, dequeue, peek and is empty.

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
it was a straight forward approach. inserting one time and checking if that value is there or not. Also understanding the difference that stacks always refer to the top node and in queues they refer to the first item added, LIFO vs FIFO.
Time: O(1)
Space: O(1)
## API
<!-- Description of each method publicly available to your Stack and Queue-->
push: Adds a new node to top of stack <br>
pop: removes node from top of stack <br>
peek: returns value of top of stack <br>
is empty: checks to see if stack / queue is empty <Br>
enqueue: adds node to queueu<br>
dequeue: removes front node to queueu
