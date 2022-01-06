# Challenge Summary
<!-- Description of the challenge -->
Review the pseudocode below, then trace the algorithm by stepping through the process with the provided sample array. Document your explanation by creating a blog article that shows the step-by-step output after each iteration through some sort of visual.

```
  InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp
```

## Whiteboard Process
<!-- Embedded whiteboard image -->
![Insertion Sort](/python/assets/insertion_sort.png)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Time: O(n)
SPace: O(1)

## Solution
<!-- Show how to run your code, and examples of it in action -->
![Blog that explains the code](/python/code_challenges/insertion_sort/BLOG.md) <br>
![Code](/python/code_challenges/insertion_sort/insertion_sort.py)
