# import pytest 
from pseudo_queue.pseudo_queue import PseudoQueue


def test_enqueue_to_empty_stack():
    queue = PseudoQueue()
    queue.enqueue(5)
    
    assert queue.stack1.peek()==5

def test_enqueue_multi_element_to_stack():
    queue = PseudoQueue()
    queue.enqueue(20)
    queue.enqueue(15)
    queue.enqueue(10)
    queue.enqueue(5)

    assert queue.stack1.peek()==5

def test_dequeue_from_stack_scenario1():
    queue = PseudoQueue()
    queue.enqueue(20)
    queue.enqueue(15)
    queue.enqueue(10)
    queue.enqueue(5)
    
    assert queue.dequeue()==20

def test_dequeue_from_stack_scenario2():
    queue = PseudoQueue()
    queue.enqueue(15)
    queue.enqueue(10)
    queue.enqueue(5)
    
    assert queue.dequeue()==15