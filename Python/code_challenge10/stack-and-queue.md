# Stacks and Queues


## Approach & Efficiency

For the **Stack** class:

**push()**: The push has a constant **time complexity**  O(1) because it only updating the top reference.
and the **space complexity** is also o(1) because it is creating a new node.

**pop():** The pop operation also has a constant **time complexity** O(1) because it removing frome the top reference.
and the **space complexity** is also o(1) because it is creating a new node.

**peek():** The peek operation has constant **time complexity and space complexity** O(1) because it only returns the value of the top element.

**is_empty():**  The is_empty operation has a constant **time complexity and space complexity** O(1) because it only checks if the top reference is None.


For the **Queue** class:

**enqueue():** The enqueue operation has a constant **time complexity and space complexity** O(1) beecause it only creating a new node and updating the back reference.

**dequeue():** The dequeue operation also has a constant **time complexity and space complexity** O(1) because it updating the front reference.

**peek():** The peek operation has a constant **time complexity and space complexity** O(1) because it only returns the value of the front element.

**is_empty():** The is_empty operation has a constant **time complexity and space complexity** O(1) because it only checks if the front reference is None.



## Solution

python Python/code_challenge10/stack_and_queue/stack_and_queue.py   >>>>  run the main

pytest Python/code_challenge10/tests/test_stack_and_queue.py        >>>>   pytest

```python
if __name__ == "__main__":

# ////////////Stack///////////
    stack_1=Stack()
    try:
        stack_1.push("e")
        stack_1.push("d")
        stack_1.push("o")
        stack_1.push("c")
        print(stack_1.pop())
        # stack_1.pop()
        # stack_1.pop()
        # stack_1.pop() # raise EmptyError exception
        print(stack_1)
        print(stack_1.is_empty())
        print(stack_1.peek())
        
    except EmptyError:
        print("Stack is empty!")

 # ////////////Queue///////////
    queue_1=Queue()
    try:
       queue_1.enqueue("b")
       queue_1.enqueue("a")
       queue_1.enqueue("y")
       queue_1.enqueue("a")
       queue_1.enqueue("n")
       print(queue_1)
       print(queue_1.dequeue())
       queue_1.dequeue()
       print("111",queue_1.peek())
       print(queue_1.is_empty())

    except EmptyError:
        print("Stack is empty!")
```