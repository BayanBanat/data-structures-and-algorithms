import pytest

from stack_and_queue.stack_and_queue import Stack,EmptyError,Queue

# ///////////////////StackTest////////////////
def test_push(stack):
    stack.push("o")
    stack.push("c")
    new_string="c -> o -> None"
    assert stack.__str__()==new_string

def test_push_multiple_values(stack):
    stack.push("e")
    stack.push("d")
    stack.push("o")
    stack.push("c")
    new_string="c -> o -> d -> e -> None"
    assert stack.__str__()==new_string

def test_pop(stack):
    stack.push("e")
    act=stack.pop()
    expected="e"
    assert act==expected

def test_empty_a_stack_after_multiple_pops(stack):
    stack.push("a")
    stack.push("b")
    stack.pop()
    stack.pop()
    assert stack.is_empty()==True

def test_peek(stack):
    stack.push("b")
    assert stack.peek()=="b"

        
def test_instantiate_empty_stack(stack):
    assert stack.is_empty()
    


def test_exception(stack):
    try:
        stack.pop()
        stack.peek()
    except EmptyError:
        assert "Stack is empty!"

@pytest.fixture
def stack():
    return Stack()


@pytest.fixture
def queue():
    return Queue()

# ///////////////////QueueTest////////////////


def test_enqueue(queue):
    queue.enqueue("b")
    queue.enqueue("a")
    new_string="b -> a -> None"
    assert queue.__str__()==new_string

def test_enqueue_multiple_values(queue):
    queue.enqueue("b")
    queue.enqueue("a")
    queue.enqueue("y")
    queue.enqueue("a")
    queue.enqueue("n")
    new_string="b -> a -> y -> a -> n -> None"
    assert queue.__str__()==new_string

def test_dequeue(queue):
    queue.enqueue("b")
    act=queue.dequeue()
    expected="b"
    assert act==expected

def test_peek_queue(queue):
    queue.enqueue("b")
    assert queue.peek()=="b"

def test_empty_a_queue_after_multiple_dequeue(queue):
    queue.enqueue("a")
    queue.enqueue("b")
    queue.dequeue()
    queue.dequeue()
    assert queue.is_empty()==True

        
def test_instantiate_empty_queue(queue):
    assert queue.is_empty()
    


def test_exception_queue(queue):
    try:
        queue.dequeue()
        queue.peek()
    except EmptyError:
        assert "Stack is empty!"

