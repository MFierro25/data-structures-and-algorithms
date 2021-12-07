class Node:
    def __init__ (self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

class LinkedList:
    def __init__(self, head=None):
        self.head = head
        
    def insert(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.nextNode != None:
                current = current.nextNode
            current.nextNode = node
        return self.head

    def includes(self, value):
        
        currentNode = self.head
        while currentNode:
            if currentNode.value == value:
                return True
            currentNode = currentNode.next
        return False

print(LinkedList)