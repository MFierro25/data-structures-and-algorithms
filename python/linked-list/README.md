# Singly Linked List
<!-- Short summary or background information -->
 the simplest type of linked list in which every node contains some data and a pointer to the next node of the same data type

## Challenge
<!-- Description of the challenge -->
Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node. test throughout the way to accomplish these tests: <br>

- Can successfully instantiate an empty linked list
- Can properly insert into the linked list
- The head property will properly point to the first node in the linked list
- Can properly insert multiple nodes into the linked list
- Will return true when finding a value within the linked list that exists
- Will return false when searching for a value in the linked list that does not exist
- Can properly return a collection of all the values that exist in the linked list

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
i started of by listing all my tests that i needed to include in my code.
after that i wrote out my code and then did my first test. i would comment out any unneccessaary code and focus on passing the first test. then i would uncomment more code and work my way the tests to complete code. For big O space this is O(n). this is because for each item added it will grow proportional to that item. As far as time goes it is O(1). it is O(1) because the time is constant no matter the growth of the list

## API
<!-- Description of each method publicly available to your Linked List -->
init - initializes the linked list
inserts - this allows to insert elements into the linked list
includes - this searches the linked list for keywords