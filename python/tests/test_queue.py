import pytest 
from stacks_and_queue.queue import Queue
from stacks_and_queue.error import EmptyError

# Can successfully enqueue into a queue
def test_enqueue():
    q = Queue()
    q.enqueue("first")
    actual = q.front.value
    expected = "first"
    assert actual == expected
    
# Can successfully enqueue multiple values into a queue
def test_enqueue_multi():
    q = Queue()
    q.enqueue("first")
    q.enqueue('second')
    q.enqueue('third')
    actual = q.front.value
    expected = "first"
    assert actual == expected
# Can successfully dequeue out of a queue the expected value
def test_dequeue():
    q = Queue()
    q.enqueue("first")
    q.enqueue("second")
    actual = q.dequeue()
    expected = "first"
    assert actual == expected

# Can successfully peek into a queue, seeing the expected value
def test_peek():
    q = Queue()
    q.enqueue("first")
    q.enqueue("second")
    actual = q.peek()
    expected = "first"
    assert actual == expected
    
# Can successfully empty a queue after multiple dequeues
def test_multiple_deq():
    q = Queue()
    q.enqueue("first")
    q.enqueue("second")
    q.dequeue()
    q.dequeue()
    actual = q.is_empty()
    expected = True
    assert actual == True

# Calling dequeue or peek on empty queue raises exception
def test_peek_error():
    q = Queue()
    with pytest.raises(EmptyError):
        q.peek()