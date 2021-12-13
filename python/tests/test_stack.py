import pytest

from stacks_and_queue.stacks import Stack
from stacks_and_queue.error import EmptyError

# Can successfully push onto a stack
def test_push():
    stack = Stack()
    stack.push('first')
    actual = stack.top.value
    expected = 'first'
    assert actual == expected 
    
# Can successfully push multiple values onto a stack
def test_push_mult():
    stack = Stack()
    stack.push('uno')
    stack.push('dos')
    stack.push('tres')
    actual = stack.top.value
    expected = 'tres'
    assert actual == expected
    
# Can successfully pop off the stack
def test_pop():
    stack = Stack()
    stack.push('car')
    actual = stack.pop()
    expected = 'car'
    assert actual == expected 
    
# Can successfully empty a stack after multiple pops
def test_pop_mult():
    stack = Stack()
    stack.push('uno')
    stack.push('dos')
    stack.push('tres')
    
    stack.pop()
    actual = stack.top.value
    expected = 'dos'
    assert actual == expected
    
# Can successfully peek the next item on the stack
def test_peek():
    stack = Stack()
    stack.push('car')
    stack.push('truck')
    actual = stack.peek()
    expected = 'truck'
    assert actual == expected 

# Calling pop or peek on empty stack raises exception

def test_pop_error():
    stack = Stack()
    with pytest.raises(EmptyError):
        stack.pop()
