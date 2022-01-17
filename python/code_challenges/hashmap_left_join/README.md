# Hashmap LEFT JOIN
<!-- Short summary or background information -->
Combine the key and corresponding values (if they exist) into a new data structure. 
LEFT JOIN means all the values in the first hashmap are returned, and if values exist in the “right” hashmap, they are appended to the result row.
If no values exist in the right hashmap, then some flavor of NULL should be appended to the result row.

## Challenge
<!-- Description of the challenge -->

Write a function called left join <br>

Arguments: two hash maps
The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values. <br>
The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.


Return: The returned data structure that holds the results is up to you

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Space: O(n) <br>
Time: O(n)

## Solution
<!-- Embedded whiteboard image -->

![Join Left](https://github.com/MFierro25/data-structures-and-algorithms/blob/f9e4d5303e96d881fa97712639c03d40c0f72a9e/python/code_challenges/hashmap_left_join/join_left.png)
