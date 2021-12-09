# Challenge Summary
<!-- Description of the challenge -->
write a method "Kth From end" that given an argument, "k" it will return the nodes value at that place from the tail. 

## Whiteboard Process
<!-- Embedded whiteboard image -->
![Kth from N Whiteboard](assets/kth_from_end.png)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
First instinct is to get the length of the list which i did, and then from that use (length - k + 1) to sort through my list until i got to my desired value entered. and return the value at that point. <br>
Also made sure to apply errors in case of entering too large of a value that is longer than the list or if a negative was entered <br>
Time Complex - O(n) the n is the length of the linked and as the list grows, n grows linearly.
SPace Complex - O(1) the list does not change or grow and stays the same the entire time.
## Solution
<!-- Show how to run your code, and examples of it in action -->

inside of kth_From_End enter the desired amount of nodes you want to search from tail and it will return the value inside that node. 

```python
  def kth_From_End(self, k):
        cur = self.head
        
        length = 0
        
        while cur is not None:
            cur = cur.next
            length += 1
         
        if k < 0:
            raise ValueError('Please enter a valid positive number')
           
        if k > length:
            raise ValueError('Value is greater than length of List')
        
        cur = self.head
        for _ in range(0, length - k):
            cur = cur.next
        return cur.value
```