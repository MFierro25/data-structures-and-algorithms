# Challenge Summary
<!-- Description of the challenge -->
Create a function that takes in two linked lists and returns one merged list. The returned list zips or alternates between both. 
## Whiteboard Process
<!-- Embedded whiteboard image -->

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
i went with the iterative approach. i ran a loop through the positions inserted the nodes by alternating pointers. 
Space = O(1) - the space does not grow with the function. the length of the final merged list is list one + list two so the final space is the same as the space going in
Time = O(n) - the algorithm i used goes one by one alternating between lists so it grows linearly with more nodes added
## Solution
<!-- Show how to run your code, and examples of it in action --> 
insert two desired lists within the function and it will start at the head of first_lst

```python
    def merge_lists(self, first_lst, second_lst):
        
        first_cur = first_lst.head
        sec_cur = second_lst.head
        
        while first_cur != None and sec_cur != None:
            first_next = first_cur.next
            sec_next = sec_cur.next
            
            sec_cur.next = first_next
            first_cur.next = sec_cur
            
            first_cur = first_next
            sec_cur = sec_next
            second_lst.head = sec_cur
```
