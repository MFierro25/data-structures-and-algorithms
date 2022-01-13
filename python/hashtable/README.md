# Hashtables
<!-- Short summary or background information -->
"Hashtables are a data structure that utilize key value pairs. This means every Node or Bucket has both a key, and a value." [codefellow hash basics](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-30/resources/Hashtables.html)

## Challenge
<!-- Description of the challenge -->
Implement a Hashtable Class with the following methods:

add<br>
get<br>
contains<br>
hash<br>

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Time: O(n) <br>
Space: O(n)

## API
<!-- Description of each method publicly available in each of your hashtable -->
add - <br>
- Arguments: key, value
- Returns: nothing
- This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

get - <br>
- Arguments: key
- Returns: Value associated with that key in the table

contains - <br>
- Arguments: key
- Returns: Boolean, indicating if the key exists in the table already.

hash<br>
- Arguments: key
- Returns: Index in the collection for that key


## Sources

[basics](https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/)
[codefellow hash basics](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-30/resources/Hashtables.html)
[Hashtable article](https://stephenagrice.medium.com/how-to-implement-a-hash-table-in-python-1eb6c55019fd)