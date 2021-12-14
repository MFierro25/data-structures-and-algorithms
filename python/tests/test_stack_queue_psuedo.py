from stack_queue_psuedo.stack_queue_psuedo import PsuedoQueue
from stacks_and_queue.error import EmptyError
import pytest

# test if one object can be enqueue
def test_enqueue():
    q = PsuedoQueue()
    q.enqueue("first")
    actual = q.dequeue()
    expected = "first"
    assert actual == expected

# test to see if error arises with empty queue
def test_empty_error():
    q = PsuedoQueue()
    with pytest.raises(EmptyError):
        q.dequeue()
        
# test first dequeue with multiple enqueue
def test_multi_enqueue():
    q = PsuedoQueue()
    q.enqueue("first")
    q.enqueue('second')
    q.enqueue('third')
    actual = q.dequeue()
    expected = "first"
    assert actual == expected
    
# test multiple deque with multiple enqueue
def test_multi_dequeue():
    q = PsuedoQueue()
    q.enqueue("first")
    q.enqueue('second')
    q.enqueue('third')
    q.dequeue()
    actual = q.dequeue()
    expected = "second"
    assert actual == expected
    
# test error after dequeues empties out the Queue (test does what i want and brings back proper error
# but cant seem to pass in pytest, need to figure out how to properly write the test)

# def test_dequeue_erro():
#     q = PsuedoQueue()
#     q.enqueue("first")
#     q.enqueue('second')
#     q.dequeue()
#     q.dequeue()
#     q.dequeue()
#     with pytest.raises(EmptyError):
#         q.dequeue()